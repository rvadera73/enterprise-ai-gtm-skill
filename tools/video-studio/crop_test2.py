from PIL import Image
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
src = Image.open(HERE / "pipeline-full.png")

crops = {
    "crop_beat5": (270, 1400, 1260, 1600),
    "crop_footer": (270, 1740, 1690, 1860),
    "crop_wide_bottom": (270, 1650, 1690, 1900),  # fallback search band if footer still misses
}
for name, box in crops.items():
    src.crop(box).save(HERE / f"{name}.png")
