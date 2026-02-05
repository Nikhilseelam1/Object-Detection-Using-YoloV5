import os
import shutil
from pathlib import Path
from sklearn.model_selection import train_test_split

SOURCE_DIR = (
    "artifacts/02_05_2026_00_10_17/"
    "data_ingestion/feature_store/"
    "asl_alphabet_train/asl_alphabet_train"
)

BASE_DIR = Path("data")
IMAGES_TRAIN = BASE_DIR / "images/train"
IMAGES_VAL = BASE_DIR / "images/val"
LABELS_TRAIN = BASE_DIR / "labels/train"
LABELS_VAL = BASE_DIR / "labels/val"

for d in [IMAGES_TRAIN, IMAGES_VAL, LABELS_TRAIN, LABELS_VAL]:
    d.mkdir(parents=True, exist_ok=True)

classes = sorted(os.listdir(SOURCE_DIR))
class_to_id = {cls: idx for idx, cls in enumerate(classes)}

all_images = []

for cls in classes:
    class_path = Path(SOURCE_DIR) / cls
    if not class_path.is_dir():
        continue
    for img in class_path.glob("*.jpg"):
        all_images.append((img, class_to_id[cls]))

train_imgs, val_imgs = train_test_split(
    all_images, test_size=0.2, random_state=42
)

def convert(images, img_dir, label_dir):
    for img_path, class_id in images:
        shutil.copy(img_path, img_dir / img_path.name)

        label_path = label_dir / f"{img_path.stem}.txt"
        with open(label_path, "w") as f:
            f.write(f"{class_id} 0.5 0.5 1.0 1.0\n")

convert(train_imgs, IMAGES_TRAIN, LABELS_TRAIN)
convert(val_imgs, IMAGES_VAL, LABELS_VAL)

print("converted to YOLO format")
print("Class mapping:", class_to_id)
