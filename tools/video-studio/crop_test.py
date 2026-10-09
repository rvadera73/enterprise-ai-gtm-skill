from PIL import Image
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
src = Image.open(HERE / "pipeline-full.png")
print("full size:", src.size)

crops = {
    "crop_beat1": (270, 580, 1290, 900),      # cards 1 Development + 2 CI Pipeline
    "crop_beat4": (270, 1080, 1260, 1650),    # card 4 Dispatch Engine, both tracks incl Live: lines
    "crop_beat5": (270, 1080, 1260, 1650),    # same region -- Live: lines are inside it
    "crop_footer": (270, 2320, 1690, 2420),   # roadmap footer line
}
for name, box in crops.items():
    src.crop(box).save(HERE / f"{name}.png")
    print(name, box)
