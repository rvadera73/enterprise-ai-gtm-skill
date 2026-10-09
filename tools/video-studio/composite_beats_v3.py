from PIL import Image, ImageFilter, ImageEnhance
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "assets_v3"
OUT.mkdir(exist_ok=True)

full = Image.open(HERE / "pipeline-full-v2.png")
TARGET = (1600, 900)


def fit_to_target(img):
    w, h = img.size
    scale = min(TARGET[0] / w, TARGET[1] / h)
    new_w, new_h = int(w * scale), int(h * scale)
    resized = img.resize((new_w, new_h))
    canvas = Image.new("RGBA", TARGET, (238, 241, 245, 255))
    canvas.paste(resized, ((TARGET[0] - new_w) // 2, (TARGET[1] - new_h) // 2))
    return canvas


# Regenerate beat6's full reveal from the CORRECTED render (Unified Case
# Management System, not the stale "Intelligent Case Portal")
beat6_bg = full.crop((0, 0, 2000, 1900))
fit_to_target(beat6_bg).convert("RGB").save(OUT / "beat6-full-reveal.png")

# Ambient backdrop for beats 2 & 3: the masthead + context-panel band,
# dimmed/blurred so it reads as background texture (same visual "world" as
# every other beat) without competing with the foreground card's own text.
top_band = full.crop((0, 0, 2000, 780))
bg = fit_to_target(top_band).convert("RGB")
bg = bg.filter(ImageFilter.GaussianBlur(2.5))
bg = ImageEnhance.Brightness(bg).enhance(1.04)
bg = ImageEnhance.Contrast(bg).enhance(0.9)
bg.save(OUT / "ambient-backdrop.png")

print("done")
