import os
from dataclasses import dataclass
from datetime import datetime
from signLanguage.constant.training_pipeline import *

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

@dataclass
class TrainingPipelineConfig:
    artifacts_dir: str = os.path.join(ARTIFACTS_DIR, TIMESTAMP)


training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()


@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(
        training_pipeline_config.artifacts_dir,
        DATA_INGESTION_DIR_NAME
    )

    feature_store_file_path: str = os.path.join(
        data_ingestion_dir,
        DATA_INGESTION_FEATURE_STORE_DIR
    )

    data_download_url: str = DATA_DOWNLOAD_URL


@dataclass
class DataValidationConfig:
    data_validation_dir: str = os.path.join(
        training_pipeline_config.artifacts_dir,
        DATA_VALIDATION_DIR_NAME
    )

    valid_status_file_dir: str = os.path.join(
        data_validation_dir,
        DATA_VALIDATION_STATUS_FILE
    )

    required_dir_list = DATA_VALIDATION_ALL_REQUIRED_DIRS

from dataclasses import dataclass
import os
from signLanguage.constant.training_pipeline import *

@dataclass
class ModelTrainerConfig:
    model_trainer_dir: str = os.path.join(
        training_pipeline_config.artifacts_dir,
        MODEL_TRAINER_DIR_NAME
    )

    trained_model_path: str = os.path.join(
        model_trainer_dir,
        MODEL_TRAINER_TRAINED_MODEL_DIR,
        MODEL_TRAINER_WEIGHTS_NAME
    )

    epochs: int = MODEL_TRAINER_EPOCHS
    batch_size: int = MODEL_TRAINER_BATCH_SIZE
    image_size: int = MODEL_TRAINER_IMAGE_SIZE


