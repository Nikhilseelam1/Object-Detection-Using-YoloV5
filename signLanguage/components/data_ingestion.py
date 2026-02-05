import os
import sys
import zipfile
import gdown

from signLanguage.logger import logging
from signLanguage.exception import SignException
from signLanguage.entity.config_entity import DataIngestionConfig
from signLanguage.entity.artifacts_entity import DataIngestionArtifact


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise SignException(e, sys)

    def download_data(self) -> str:
       
        try:
            dataset_url = self.data_ingestion_config.data_download_url
            zip_download_dir = self.data_ingestion_config.data_ingestion_dir

            os.makedirs(zip_download_dir, exist_ok=True)

            zip_file_path = os.path.join(
            zip_download_dir, "archive (6).zip"
            )


            logging.info("Downloading dataset from Google Drive...")
            gdown.download(dataset_url, zip_file_path, quiet=False)
            logging.info(f"Dataset downloaded at: {zip_file_path}")

            return zip_file_path

        except Exception as e:
            raise SignException(e, sys)

    def extract_zip_file(self, zip_file_path: str) -> str:
       
        try:
            feature_store_path = self.data_ingestion_config.feature_store_file_path
            os.makedirs(feature_store_path, exist_ok=True)

            with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
                zip_ref.extractall(feature_store_path)

            logging.info(
                f"Extracted zip file {zip_file_path} into {feature_store_path}"
            )

            return feature_store_path

        except Exception as e:
            raise SignException(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        logging.info("Starting Data Ingestion process")
        try:
            zip_file_path = self.download_data()
            feature_store_path = self.extract_zip_file(zip_file_path)

            data_ingestion_artifact = DataIngestionArtifact(
                data_zip_file_path=zip_file_path,
                feature_store_path=feature_store_path
            )

            logging.info("Data Ingestion completed successfully")
            logging.info(f"Data Ingestion Artifact: {data_ingestion_artifact}")

            return data_ingestion_artifact

        except Exception as e:
            raise SignException(e, sys)
