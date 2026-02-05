import streamlit as st
from PIL import Image
import os
import torch


st.set_page_config(
    page_title="ASL Sign Language Detection",
    layout="centered"
)

st.title("ASL Sign Language Detection")
st.write("YOLOv5 based ASL alphabet detection")

MODEL_PATH = "artifacts/02_05_2026_14_18_32.log/model_trainer/trained_model/best.pt"

@st.cache_resource
def load_model():
    model = torch.hub.load(
        "ultralytics/yolov5",
        "custom",
        path=MODEL_PATH,
        force_reload=False
    )
    model.conf = 0.4
    return model

model = load_model()

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Detect Sign"):
        with st.spinner("Running YOLOv5 inference..."):
            results = model(image)

        st.success("Detection Completed")

        rendered_img = results.render()[0]
        st.image(rendered_img, caption="Detection Result", use_column_width=True)

        detections = results.pandas().xyxy[0]
        if detections.empty:
            st.warning("No signs detected")
        else:
            st.subheader("Detected Signs")
            st.dataframe(detections[["name", "confidence"]])
