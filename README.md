#  Sign Language Detection using YOLOv5

An end-to-end **object detection system** for recognizing **American Sign Language (ASL) alphabets** using **YOLOv5**.  
This project converts a classification-based ASL dataset into YOLO object detection format, trains a deep learning model, and deploys it through an interactive user interface.

---

##  Project Motivation

Communication barriers faced by the deaf and hard-of-hearing community inspired this project.  
While many sign language datasets exist, most are designed for **image classification**, not **real-time detection**.

The motivation behind this project is to:
- Bridge the gap between **static classification** and **real-time object detection**
- Build an **accessible AI system** capable of detecting ASL signs from images
- Demonstrate a **complete machine learning pipeline**, from data ingestion to deployment

---

##  Problem Statement

Most publicly available ASL datasets:
- Are structured for **classification**
- Do not contain bounding box annotations
- Cannot be directly used with object detection models like YOLO

This limits their usability in real-world applications such as live camera-based sign detection.

---

##  Solution Overview

This project solves the problem by:

1. **Ingesting raw ASL dataset** using a structured data ingestion pipeline  
2. **Validating dataset integrity** before training  
3. **Converting classification data into YOLO format** by auto-generating bounding boxes  
4. **Training a YOLOv5 model** using transfer learning  
5. **Deploying the trained model** via a Streamlit-based interface for inference  

The system follows an **end-to-end modular pipeline** approach, making it scalable and reproducible.

---

##  About the Model

- **Model Architecture:** YOLOv5 (You Only Look Once)
- **Learning Type:** Supervised Object Detection
- **Training Strategy:** Transfer Learning using pretrained YOLOv5 weights
- **Classes Detected:**  
  - ASL Alphabets (A–Z)  
  - Special tokens: `space`, `nothing`, `del`
- **Bounding Boxes:** Auto-generated during dataset conversion
- **Inference:** Image-based detection with confidence scores

YOLOv5 was chosen due to its **real-time performance**, **accuracy**, and **production readiness**.

---

##  Tech Stack

- **Programming Language:** Python  
- **Deep Learning Framework:** PyTorch  
- **Object Detection Model:** YOLOv5  
- **Data Processing:** NumPy, OpenCV  
- **Visualization & UI:** Streamlit  
- **Experiment Tracking:** Artifact-based pipeline  
- **Development Environment:** Google Colab / Local Machine  

---

##  Future Enhancements

-  Real-time webcam-based ASL detection  
-  Video stream inference support  
-  Sentence-level sign language recognition  
-  Model optimization for edge devices  
-  Deployment using Docker and cloud platforms  
-  Integration with speech or text translation systems  

---

##  Author

**Nikhil Seelam**  
Aspiring AI / GenAI Engineer  
Passionate about Computer Vision, Deep Learning, and building real-world AI systems
