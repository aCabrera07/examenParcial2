from pathlib import Path
from shutil import copy2
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(r"C:\Users\aleja\AndroidStudioProjects\examenParcial2")
OUT = ROOT / "entrega" / "reporte_overleaf"
IMAGES = OUT / "imagenes"
IMAGES.mkdir(parents=True, exist_ok=True)

sources = [
    (r"C:\Users\aleja\OneDrive\Imágenes\Capturas de pantalla\Captura de pantalla 2026-11-05 231633.png", "figura_01.png"),
    (r"C:\Users\aleja\OneDrive\Imágenes\Capturas de pantalla\Captura de pantalla 2026-11-05 233206.png", "figura_02.png"),
    (r"C:\Users\aleja\OneDrive\Imágenes\Capturas de pantalla\Captura de pantalla 2026-11-05 233514.png", "figura_03.png"),
    (r"C:\Users\aleja\OneDrive\Imágenes\Capturas de pantalla\Captura de pantalla 2026-11-05 234502.png", "figura_04.png"),
    (r"C:\Users\aleja\OneDrive\Imágenes\Capturas de pantalla\Captura de pantalla 2026-11-05 235201.png", "figura_05.png"),
    (r"C:\Users\aleja\OneDrive\Imágenes\Capturas de pantalla\Captura de pantalla 2026-11-05 235442.png", "figura_06.png"),
    (r"C:\Users\aleja\OneDrive\Imágenes\Capturas de pantalla\Captura de pantalla 2026-11-06 000255.png", "figura_07.png"),
    (r"C:\Users\aleja\OneDrive\Imágenes\Capturas de pantalla\Captura de pantalla 2026-11-06 003551.png", "figura_08.png"),
    (r"C:\Users\aleja\OneDrive\Imágenes\Capturas de pantalla\Captura de pantalla 2026-11-06 003852.png", "figura_09.png"),
    (r"C:\Users\aleja\OneDrive\Imágenes\Capturas de pantalla\Captura de pantalla 2026-11-06 004146.png", "figura_10.png"),
    (r"C:\Users\aleja\OneDrive\Imágenes\Capturas de pantalla\Captura de pantalla 2026-11-06 004224.png", "figura_11.png"),
]

for source, target in sources:
    copy2(source, IMAGES / target)

copy2(
    r"C:\Users\aleja\Documents\Codex\2026-11-03\referenced-chatgpt-conversation-this-is-an\work\listas_enlazadas_overleaf\logo_upp.png",
    IMAGES / "logo_upp.png",
)

# La octava captura mostraba la clave de Google Maps en el editor. Se conserva
# la evidencia, pero se cubre únicamente el valor sensible antes de empaquetarla.
image_path = IMAGES / "figura_08.png"
image = Image.open(image_path).convert("RGB")
draw = ImageDraw.Draw(image)
draw.rounded_rectangle((963, 510, 1374, 548), radius=5, fill=(31, 31, 31))
try:
    font = ImageFont.truetype(r"C:\Windows\Fonts\arial.ttf", 18)
except OSError:
    font = ImageFont.load_default()
draw.text((982, 518), "CLAVE OCULTA POR SEGURIDAD", fill=(225, 225, 225), font=font)
image.save(image_path, quality=95)

print(OUT)
