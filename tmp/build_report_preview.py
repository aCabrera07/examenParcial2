from pathlib import Path
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    Image,
    KeepTogether,
    ListFlowable,
    ListItem,
)


ROOT = Path(r"C:\Users\aleja\AndroidStudioProjects\examenParcial2")
PROJECT = ROOT / "entrega" / "reporte_overleaf"
OUTPUT = PROJECT / "reporte_vista_previa.pdf"
TEX = PROJECT / "main.tex"

pdfmetrics.registerFont(TTFont("Arial", r"C:\Windows\Fonts\arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", r"C:\Windows\Fonts\arialbd.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Italic", r"C:\Windows\Fonts\ariali.ttf"))

body = ParagraphStyle(
    "Body",
    fontName="Arial",
    fontSize=12,
    leading=24,
    alignment=TA_LEFT,
    firstLineIndent=1.25 * cm,
    spaceAfter=3,
    allowWidows=0,
    allowOrphans=0,
)
section = ParagraphStyle(
    "Section",
    parent=body,
    fontName="Arial-Bold",
    fontSize=14,
    leading=17,
    firstLineIndent=0,
    spaceBefore=14,
    spaceAfter=10,
)
subsection = ParagraphStyle(
    "Subsection",
    parent=body,
    fontName="Arial-Bold",
    fontSize=12,
    leading=15,
    firstLineIndent=0,
    spaceBefore=12,
    spaceAfter=7,
)
caption = ParagraphStyle(
    "Caption",
    parent=body,
    fontSize=10.5,
    leading=13,
    alignment=TA_CENTER,
    firstLineIndent=0,
    spaceBefore=5,
    spaceAfter=10,
)
cover = ParagraphStyle(
    "Cover",
    fontName="Arial",
    fontSize=12,
    leading=18,
    alignment=TA_CENTER,
)
cover_bold = ParagraphStyle(
    "CoverBold",
    parent=cover,
    fontName="Arial-Bold",
    fontSize=14,
    leading=19,
)
toc_main = ParagraphStyle(
    "TocMain",
    parent=body,
    fontName="Arial-Bold",
    leading=19,
    firstLineIndent=0,
    leftIndent=0,
)
toc_sub = ParagraphStyle(
    "TocSub",
    parent=body,
    leading=18,
    firstLineIndent=0,
    leftIndent=0.8 * cm,
)
reference = ParagraphStyle(
    "Reference",
    parent=body,
    fontSize=10,
    leading=16,
    firstLineIndent=0,
    leftIndent=1.0 * cm,
    rightIndent=0.5 * cm,
    splitLongWords=True,
)


def clean_tex(text: str) -> str:
    text = text.strip()
    text = re.sub(r"\\textit\{([^{}]*)\}", r"<i>\1</i>", text)
    text = text.replace(r"C\#", "C#")
    text = text.replace(r"\&", "&")
    text = text.replace(r"\\", "")
    text = re.sub(r"\\url\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\[A-Za-z]+\*?(?:\[[^\]]*\])?\{([^{}]*)\}", r"\1", text)
    return text


def page_number(canvas, doc):
    if doc.page > 3:
        canvas.saveState()
        canvas.setFont("Arial", 10)
        canvas.drawRightString(A4[0] - 2.5 * cm, A4[1] - 1.5 * cm, str(doc.page - 3))
        canvas.restoreState()


story = []
story.append(Spacer(1, 1.0 * cm))
logo = Image(str(PROJECT / "imagenes" / "logo_upp.png"), width=4.0 * cm, height=4.0 * cm)
logo.hAlign = "CENTER"
story.extend([
    logo,
    Spacer(1, 0.7 * cm),
    Paragraph("Universidad Politécnica de Pachuca", cover_bold),
    Spacer(1, 0.55 * cm),
    Paragraph("Desarrollo de Aplicaciones Móviles", cover_bold),
    Spacer(1, 0.55 * cm),
    Paragraph("Perfil profesional con Jetpack Compose", cover_bold),
    Paragraph("Examen Parcial 2", cover),
    Spacer(1, 0.8 * cm),
    Paragraph("<b>Autor:</b>", cover),
    Paragraph("Cabrera Bardales Edgar Alejandro", cover),
    Paragraph("2531126226", cover),
    Spacer(1, 0.45 * cm),
    Paragraph("<b>Profesor:</b>", cover),
    Paragraph("Ing. Montoya Cerro Miguel Ángel", cover),
    Spacer(1, 0.45 * cm),
    Paragraph("<b>Grupo:</b>", cover),
    Paragraph("TIID 04-01", cover),
    Spacer(1, 2.2 * cm),
    Paragraph("Zempoala, Hidalgo, México a 06 de noviembre de 2026", cover),
    PageBreak(),
    Paragraph("Índice", section),
])

toc = [
    ("Introducción", False), ("Objetivos", False), ("Objetivo central", True),
    ("Objetivos específicos", True), ("Justificación", False),
    ("Estructura del documento", False), ("Marco teórico", False),
    ("Jetpack Compose y organización de la interfaz", True),
    ("Listas desplazables", True), ("Estado, botón flotante y navegación inferior", True),
    ("Google Maps en Compose", True), ("Desarrollo", False),
    ("Revisión de la pantalla inicial", True), ("Ajuste de la portada", True),
    ("Creación del encabezado superior", True), ("Superposición de la fotografía", True),
    ("Organización de los datos personales", True), ("Incorporación de la biografía", True),
    ("Lista de lenguajes de programación", True), ("Configuración de Google Maps", True),
    ("Creación del marcador", True), ("Implementación del botón flotante", True),
    ("Despliegue de la barra inferior", True), ("Conclusiones", False),
    ("Recomendaciones", False), ("Anexo", False), ("Referencias", False),
]
for label, is_sub in toc:
    story.append(Paragraph(label, toc_sub if is_sub else toc_main))

story.extend([PageBreak(), Paragraph("Índice de imágenes", section)])
figure_captions = [
    "Pantalla inicial", "Ajuste de portada", "Encabezado superior", "Perfil superpuesto",
    "Datos del perfil", "Biografía del usuario", "Lenguajes agregados",
    "Configuración del mapa", "Marcador en el mapa", "Botón flotante",
    "Barra inferior desplegada",
]
for number, label in enumerate(figure_captions, 1):
    story.append(Paragraph(f"Figura {number}. {label}", toc_sub))
story.append(PageBreak())

lines = TEX.read_text(encoding="utf-8").splitlines()
start = next(i for i, line in enumerate(lines) if line.strip() == r"\section{Introducción}")
lines = lines[start:]

figure_number = 0
pending_image = None
in_figure = False
in_itemize = False
items = []

for raw in lines:
    line = raw.strip()
    if not line or line in {r"\end{document}", r"\setstretch{1.5}", r"\setlength{\parindent}{0pt}"}:
        continue
    if line == r"\clearpage":
        story.append(PageBreak())
        continue
    if line.startswith(r"\section{"):
        title = re.match(r"\\section\{(.+)\}", line).group(1)
        story.append(Paragraph(title, section))
        continue
    if line.startswith(r"\subsection{"):
        title = re.match(r"\\subsection\{(.+)\}", line).group(1)
        story.append(Paragraph(title, subsection))
        continue
    if line.startswith(r"\begin{itemize}"):
        in_itemize = True
        items = []
        continue
    if line.startswith(r"\end{itemize}"):
        in_itemize = False
        story.append(ListFlowable([ListItem(Paragraph(x, body)) for x in items], bulletType="bullet", leftIndent=24))
        continue
    if in_itemize and line.startswith(r"\item"):
        items.append(clean_tex(line[5:].strip()))
        continue
    if line.startswith(r"\begin{figure}"):
        in_figure = True
        pending_image = None
        continue
    if in_figure and r"\includegraphics" in line:
        pending_image = re.search(r"\{([^{}]+\.png)\}", line).group(1)
        continue
    if in_figure and line.startswith(r"\caption{"):
        figure_number += 1
        label = re.match(r"\\caption\{(.+)\}", line).group(1)
        path = PROJECT / "imagenes" / pending_image
        img = Image(str(path), width=16.0 * cm, height=9.0 * cm)
        img.hAlign = "CENTER"
        story.append(KeepTogether([img, Paragraph(f"<b>Figura {figure_number}.</b> {label}", caption)]))
        continue
    if line.startswith(r"\end{figure}"):
        in_figure = False
        continue
    if line.startswith(r"\vspace{"):
        match = re.search(r"\{([0-9.]+)cm\}", line)
        if match:
            story.append(Spacer(1, float(match.group(1)) * cm))
        continue
    if in_figure:
        continue
    if line.startswith("Android Developers.") or line.startswith("Google Maps Platform."):
        story.append(Paragraph(clean_tex(line), reference))
        continue
    if line.startswith(r"\url{"):
        url = clean_tex(line).replace("/", "/&#8203;").replace("-", "-&#8203;")
        story.append(Paragraph(url, reference))
        continue
    if line.startswith("\\"):
        continue
    story.append(Paragraph(clean_tex(line), body))

doc = SimpleDocTemplate(
    str(OUTPUT),
    pagesize=A4,
    rightMargin=2.5 * cm,
    leftMargin=2.5 * cm,
    topMargin=2.5 * cm,
    bottomMargin=2.5 * cm,
    title="Perfil profesional con Jetpack Compose",
    author="Cabrera Bardales Edgar Alejandro",
)
doc.build(story, onFirstPage=page_number, onLaterPages=page_number)
print(OUTPUT)
