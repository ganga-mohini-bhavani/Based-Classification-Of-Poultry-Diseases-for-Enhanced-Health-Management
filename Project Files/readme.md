# 🐔 PoultryDetect: Poultry Disease Classification Using Transfer Learning

This repository contains the trained deep learning model (`poultry_disease_model.h5`) and the Flask application (`app.py`) used for classifying poultry diseases from images.

Developed as part of a SmartBridge-guided AI/ML internship, this project applies **Transfer Learning** to classify diseases such as **Coccidiosis**, **New Castle Disease**, **Salmonella**, and identify **Healthy** poultry.

## 📁 Project Files

| File/Folder              | Description                                  |
|--------------------------|----------------------------------------------|
| `poultry_disease_model.h5` | Trained deep learning model file (MobileNetV2) |
| `app.py`                  | Flask web application to run predictions     |

## 🚀 How to Run the Application

1. Clone or download the repository.
2. Make sure Python and required libraries are installed (`TensorFlow`, `Flask`, etc.).
3. Place your test images in a folder (or use upload in the UI).

🧠 Model Details

* Architecture: MobileNetV2 (Transfer Learning)

* Input Shape: 224 x 224 x 3

* Output Classes: Coccidiosis, New Castle Disease, Salmonella, Healthy

* Accuracy: ~90%+ on validation data

📝 Notes

* This folder is focused on deployment. For training code and dataset, refer to the full project repository (if applicable).

* Make sure to run app.py from the directory where poultry_disease_model.h5 is located.
