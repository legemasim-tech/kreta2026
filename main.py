from pathlib import Path
import importlib.util

from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML


BASE_DIR = Path(__file__).parent.resolve()
CONTENT_DIR = BASE_DIR / "content"
IMAGE_DIR = BASE_DIR / "images"


BOOK = {
    "title": "KRETA 2026",
    "subtitle": "Unser Reisebuch",
    "location": "Villa Pericles · Sfinari · Westkreta",
    "people": "Petra • Thomas • Gerti • Markus • Yvonne • Florian • Leo",
    "dates": "08.08.2026 – 22.08.2026",
}

COVER_IMAGE = "Villa Perikles (1).avif"


def image_uri(filename: str | None) -> str | None:
    if not filename:
        return None
    path = IMAGE_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"Bild nicht gefunden: {path}")
    return path.as_uri()


def load_content_pages() -> list[dict]:
    pages = []

    for file_path in sorted(CONTENT_DIR.glob("*.py")):
        if file_path.name.startswith("__"):
            continue

        module_name = file_path.stem
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        pages.append({
            "title": getattr(module, "TITLE"),
            "text": getattr(module, "TEXT"),
            "image": image_uri(getattr(module, "IMAGE", None)),
        })

    return pages


def build_pdf() -> None:
    output_dir = BASE_DIR / "output"
    output_dir.mkdir(exist_ok=True)

    css = (BASE_DIR / "styles" / "style.css").read_text(encoding="utf-8")

    env = Environment(loader=FileSystemLoader(BASE_DIR / "templates"))
    template = env.get_template("book.html")

    html = template.render(
        book=BOOK,
        cover_image=image_uri(COVER_IMAGE),
        pages=load_content_pages(),
        css=css,
    )

    pdf_path = output_dir / "Kreta_2026_Reisebuch.pdf"
    HTML(string=html, base_url=str(BASE_DIR)).write_pdf(str(pdf_path))

    print(f"PDF erstellt: {pdf_path}")


if __name__ == "__main__":
    build_pdf()