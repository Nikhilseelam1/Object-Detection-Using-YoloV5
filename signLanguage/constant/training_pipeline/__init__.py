import os

ARTIFACTS_DIR: str = "artifacts"

DATA_INGESTION_DIR_NAME: str = "data_ingestion"

DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"

DATA_DOWNLOAD_URL: str = (
    "https://drive.google.com/uc?id=1iuW6dfj-M4PvbEE7keZIrTpo9JuAxjfP"
)


DATA_VALIDATION_DIR_NAME: str = "data_validation"

DATA_VALIDATION_STATUS_FILE: str = "status.txt"

DATA_VALIDATION_ALL_REQUIRED_DIRS = [
    "images/train",
    "images/val",
    "labels/train",
    "labels/val",
]



MODEL_TRAINER_DIR_NAME: str = "model_trainer"

MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"

MODEL_TRAINER_WEIGHTS_NAME: str = "best.pt"

MODEL_TRAINER_EPOCHS: int = 20

MODEL_TRAINER_BATCH_SIZE: int = 8

MODEL_TRAINER_IMAGE_SIZE: int = 416

