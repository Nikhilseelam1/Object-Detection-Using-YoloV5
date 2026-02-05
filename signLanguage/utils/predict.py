import torch
from PIL import Image

class ASLPredictor:
    def __init__(self, model_path: str):
        self.model = torch.hub.load(
            "ultralytics/yolov5",
            "custom",
            path=model_path,
            force_reload=False
        )
        self.model.conf = 0.4

    def predict(self, image: Image.Image):
        results = self.model(image)
        return results
