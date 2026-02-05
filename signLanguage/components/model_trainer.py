import os
import sys
import shutil
import subprocess
from signLanguage.logger import logging
from signLanguage.exception import SignException
from signLanguage.entity.config_entity import ModelTrainerConfig
from signLanguage.entity.artifacts_entity import ModelTrainerArtifact

class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerConfig):
        try:
            self.model_trainer_config = model_trainer_config
        except Exception as e:
            raise SignException(e, sys)

    def initiate_model_trainer(self) -> ModelTrainerArtifact:
       
        logging.info("Starting YOLOv5 Model Training")

        try:
            os.makedirs(
                os.path.dirname(self.model_trainer_config.trained_model_path),
                exist_ok=True
            )
            train_command = [
                "python", "yolov5/train.py",
                "--img", str(self.model_trainer_config.image_size),
                "--batch", str(self.model_trainer_config.batch_size),
                "--epochs", str(self.model_trainer_config.epochs),
                "--data", "data.yaml",
                "--weights", "yolov5s.pt",
                "--name", "asl_yolov5"
            ]

            logging.info(f"Training command: {' '.join(train_command)}")
            subprocess.run(train_command, check=True)
            source_model_path = os.path.join(
                "yolov5",
                "runs",
                "train",
                "asl_yolov5",
                "weights",
                "best.pt"
            )
            shutil.copy(
                source_model_path,
                self.model_trainer_config.trained_model_path
            )
            logging.info("Model training completed successfully")
            return ModelTrainerArtifact(
                trained_model_path=self.model_trainer_config.trained_model_path
            )
        except Exception as e:
            raise SignException(e, sys)
