from PIL import Image, ImageOps
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "assets_v2"
OUT.mkdir(exist_ok=True)

full = Image.open(HERE / "pipeline-full.png")
healthcheck = Image.open(HERE / "beat-healthcheck.png")
mechanism = Image.open(HERE / "beat4-mechanism.png")

# tight-crop the inset source panels out of their padded 1600x900 canvases
healthcheck_inset = healthcheck.crop((295, 300, 1300, 595))
mechanism_inset = mechanism.crop((95, 215, 1505, 665))


def with_shadow_border(img, border=3):
    return ImageOps.expand(img, border=border, fill=(16, 27, 45, 255))


def paste_inset(bg, inset, scale, pos):
    w, h = inset.size
    resized = inset.resize((int(w * scale), int(h * scale)))
    bordered = with_shadow_border(resized)
    canvas = bg.convert("RGBA")
    canvas.alpha_composite(bordered.convert("RGBA"), pos)
    return canvas


TARGET = (1600, 900)


def fit_to_target(img):
    """Scale+letterbox (paper-colored) an arbitrary crop onto the 1600x900 canvas."""
    w, h = img.size
    scale = min(TARGET[0] / w, TARGET[1] / h)
    new_w, new_h = int(w * scale), int(h * scale)
    resized = img.resize((new_w, new_h))
    canvas = Image.new("RGBA", TARGET, (238, 241, 245, 255))
    canvas.paste(resized, ((TARGET[0] - new_w) // 2, (TARGET[1] - new_h) // 2))
    return canvas


# Beat 1: cards 1+2 backdrop (NO inset baked in -- animated in via ffmpeg fade)
beat1_bg = full.crop((270, 580, 1290, 900))
fit_to_target(beat1_bg).convert("RGB").save(OUT / "beat1-bg.png")

# Beat 4: dispatch-engine card backdrop (no inset baked in)
beat4_bg = full.crop((270, 1080, 1260, 1650))
fit_to_target(beat4_bg).convert("RGB").save(OUT / "beat4-bg.png")

# Beat 5: Live: lines backdrop (no inset baked in)
beat5_bg = full.crop((270, 1400, 1260, 1600))
fit_to_target(beat5_bg).convert("RGB").save(OUT / "beat5-bg.png")

# The two real insets, tight-cropped + bordered, saved standalone (RGBA, for
# ffmpeg overlay with a fade-in -- these get animated ON TOP of the backdrops
# above, not baked in statically)
hc_small = with_shadow_border(healthcheck_inset.resize((520, int(520 * healthcheck_inset.height / healthcheck_inset.width))))
hc_small.convert("RGBA").save(OUT / "inset-healthcheck.png")
yaml_small = with_shadow_border(mechanism_inset.resize((560, int(560 * mechanism_inset.height / mechanism_inset.width))))
yaml_small.convert("RGBA").save(OUT / "inset-yaml.png")
hc_small2 = with_shadow_border(healthcheck_inset.resize((640, int(640 * healthcheck_inset.height / healthcheck_inset.width))))
hc_small2.convert("RGBA").save(OUT / "inset-healthcheck-big.png")

# Beat 6: full page reveal (trim the excess blank canvas below real content)
beat6_bg = full.crop((0, 0, 2000, 1900))
beat6 = fit_to_target(beat6_bg)
beat6.convert("RGB").save(OUT / "beat6-full-reveal.png")

print("done:", list(OUT.glob("*.png")))
