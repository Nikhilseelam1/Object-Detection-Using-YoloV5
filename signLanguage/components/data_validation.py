import os
import sys
import shutil
from signLanguage.logger import logging
from signLanguage.exception import SignException
from signLanguage.entity.config_entity import DataValidationConfig
from signLanguage.entity.artifacts_entity import (DataIngestionArtifact,DataValidationArtifact)


class DataValidation:
    def __init__(
        self,
        data_ingestion_artifact: DataIngestionArtifact,
        data_validation_config: DataValidationConfig,
    ):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
        except Exception as e:
            raise SignException(e, sys)

    def validate_yolo_directories(self) -> bool:
        try:
            project_root = os.getcwd()
            missing_dirs = []

            for required_dir in self.data_validation_config.required_dir_list:
                dir_path = os.path.join(project_root, "data", required_dir)
                if not os.path.exists(dir_path):
                    missing_dirs.append(required_dir)

            os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)

            if missing_dirs:
                validation_status = False
                logging.error(f"Missing YOLO directories: {missing_dirs}")
            else:
                validation_status = True
                logging.info("YOLO dataset validation successful")

            with open(self.data_validation_config.valid_status_file_dir, "w") as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            raise SignException(e, sys)

    def initiate_data_validation(self) -> DataValidationArtifact:
        logging.info("Entered initiate_data_validation method of DataValidation class")
        try:
            status = self.validate_yolo_directories()

            data_validation_artifact = DataValidationArtifact(
                validation_status=status
            )

            logging.info("Exited initiate_data_validation method of DataValidation class")
            logging.info(f"Data validation artifact: {data_validation_artifact}")

            if status:
                shutil.copy(
                    self.data_ingestion_artifact.data_zip_file_path,
                    os.getcwd()
                )

            return data_validation_artifact

        except Exception as e:
            raise SignException(e, sys)
