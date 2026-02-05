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
