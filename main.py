from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

from content import willkommen

env = Environment(
    loader=FileSystemLoader("templates")
)

template = env.get_template("book.html")

html = template.render(

title=willkommen.TITLE,

text=willkommen.TEXT

)

with open("output/book.html","w",encoding="utf8") as f:
    f.write(html)

HTML(string=html,base_url=".").write_pdf(
    "output/Kreta2026.pdf"
)

print("PDF erstellt.")
