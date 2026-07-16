from pathlib import Path
from urllib.parse import quote
import importlib.util
import shutil

from jinja2 import Environment, FileSystemLoader, select_autoescape

import main as pdf_engine


BASE_DIR = Path(__file__).parent.resolve()
CONTENT_DIR = BASE_DIR / "content"
IMAGE_DIR = BASE_DIR / "images"

APP_DIR = BASE_DIR / "app"
TEMPLATE_DIR = APP_DIR / "templates"
STATIC_DIR = APP_DIR / "static"

OUTPUT_DIR = BASE_DIR / "output" / "app"
OUTPUT_IMAGE_DIR = OUTPUT_DIR / "images"
OUTPUT_STATIC_DIR = OUTPUT_DIR / "static"


def image_path(filename: str | None) -> str | None:
    """
    Erzeugt einen relativen Bildpfad für die Web-App.

    Anders als image_uri() aus main.py wird hier keine file://-Adresse
    verwendet, damit die Bilder später auch über GitHub Pages funktionieren.
    """
    if not filename:
        return None

    path = IMAGE_DIR / filename

    if not path.exists():
        raise FileNotFoundError(f"Bild nicht gefunden: {path}")

    return f"images/{quote(filename)}"


def load_images(image_list) -> list[dict]:
    """
    Unterstützt beide vorhandenen Bildformate:

    "Foto.jpg"

    oder

    {
        "file": "Foto.jpg",
        "caption": "Beschreibung",
        "style": "contain"
    }
    """
    images = []

    for item in image_list:
        if isinstance(item, str):
            images.append({
                "src": image_path(item),
                "caption": "",
                "style": "cover",
            })
        else:
            images.append({
                "src": image_path(item.get("file")),
                "caption": item.get("caption", ""),
                "style": item.get("style", "cover"),
            })

    return images


def load_module(file_path: Path):
    spec = importlib.util.spec_from_file_location(
        file_path.stem,
        file_path,
    )

    if spec is None or spec.loader is None:
        raise ImportError(f"Konnte Modul nicht laden: {file_path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module


def load_content_pages() -> list[dict]:
    pages = []

    content_files = sorted(CONTENT_DIR.glob("*.py"))

    for file_path in content_files:
        if file_path.name.startswith("__"):
            continue

        module = load_module(file_path)

        quote_after_images = getattr(
            module,
            "QUOTE_AFTER_IMAGES",
            False,
        )

        text, quote_text = pdf_engine.split_quote(
            getattr(module, "TEXT", ""),
            quote_after_images,
        )

        pages.append({
            "slug": file_path.stem,
            "title": getattr(module, "TITLE", file_path.stem),
            "text": text,
            "quote": quote_text,
            "image": image_path(
                getattr(module, "IMAGE", None)
            ),
            "image_style": getattr(
                module,
                "IMAGE_STYLE",
                "cover",
            ),
            "top_images": load_images(
                getattr(module, "TOP_IMAGES", [])
            ),
            "bottom_images": load_images(
                getattr(module, "BOTTOM_IMAGES", [])
            ),
            "extra_images": load_images(
                getattr(module, "EXTRA_IMAGES", [])
            ),
            "photo_style": getattr(
                module,
                "PHOTO_STYLE",
                "double",
            ),
        })

    return pages


def prepare_output() -> None:
    """
    Löscht nur die bisher erzeugte App.

    Die PDF-Datei im übergeordneten output-Ordner bleibt bestehen.
    """
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)

    OUTPUT_DIR.mkdir(parents=True)
    OUTPUT_IMAGE_DIR.mkdir()
    OUTPUT_STATIC_DIR.mkdir()

    shutil.copytree(
        IMAGE_DIR,
        OUTPUT_IMAGE_DIR,
        dirs_exist_ok=True,
    )

    shutil.copytree(
        STATIC_DIR,
        OUTPUT_STATIC_DIR,
        dirs_exist_ok=True,
    )


def build_app() -> None:
    prepare_output()

    env = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        autoescape=select_autoescape(["html", "xml"]),
    )

    index_template = env.get_template("index.html")
    chapter_template = env.get_template("chapter.html")

    pages = load_content_pages()

    index_html = index_template.render(
        book=pdf_engine.BOOK,
        cover_image=image_path(pdf_engine.COVER_IMAGE),
        pages=pages,
    )

    (OUTPUT_DIR / "index.html").write_text(
        index_html,
        encoding="utf-8",
    )

    for index, page in enumerate(pages):
        previous_page = pages[index - 1] if index > 0 else None
        next_page = (
            pages[index + 1]
            if index < len(pages) - 1
            else None
        )

        chapter_html = chapter_template.render(
            book=pdf_engine.BOOK,
            page=page,
            chapter_number=index + 1,
            previous_page=previous_page,
            next_page=next_page,
        )

        output_path = OUTPUT_DIR / f"{page['slug']}.html"

        output_path.write_text(
            chapter_html,
            encoding="utf-8",
        )

    print(f"App erstellt: {OUTPUT_DIR / 'index.html'}")
    print(f"Kapitel erstellt: {len(pages)}")


if __name__ == "__main__":
    build_app()