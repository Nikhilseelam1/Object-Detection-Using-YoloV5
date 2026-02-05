from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    data_zip_file_path: str
    feature_store_path: str


@dataclass
class DataValidationArtifact:
    validation_status: bool

from dataclasses import dataclass

@dataclass
class ModelTrainerArtifact:
    trained_model_path: str