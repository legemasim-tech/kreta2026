from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from content import willkommen

BASE_DIR = Path(__file__).parent

BOOK = {
    "title": "KRETA 2026",
    "subtitle": "Unser Reisebuch",
    "location": "Villa Pericles · Sfinari · Westkreta",
    "people": "Petra • Thomas • Gerti • Markus • Yvonne • Florian • Leo",
    "dates": "08.08.2026 – 22.08.2026",
}

IMAGES = {
    "cover": "images/Villa Perikles von oben (2).png",
    "welcome": "images/Kreta_Westkueste_02_Sfinari_Bucht_Kissamos.jpg",
}

env = Environment(loader=FileSystemLoader(BASE_DIR / "templates"))
template = env.get_template("book.html")

html = template.render(
    book=BOOK,
    title=willkommen.TITLE,
    text=willkommen.TEXT,
    images=IMAGES,
)

output_dir = BASE_DIR / "output"
output_dir.mkdir(exist_ok=True)

html_path = output_dir / "book.html"
pdf_path = output_dir / "Kreta_2026_Reisebuch_Punkt_1.pdf"

html_path.write_text(html, encoding="utf-8")

HTML(filename=str(html_path), base_url=str(BASE_DIR)).write_pdf(str(pdf_path))

print(f"PDF erstellt: {pdf_path}")
