# Based-Classification-Of-Poultry-Diseases-for-Enhanced-Health-Management
🐔 PoultryDetect: Transfer Learning-Based Classification of Poultry Diseases
This project is developed as part of a SmartBridge-guided AI/ML internship focused on applying deep learning to real-world agricultural challenges. Using Transfer Learning with MobileNetV2, the system classifies poultry diseases from images to assist farmers and veterinarians in early detection and enhanced health management.

🚀 Features

🧠 Transfer Learning using MobileNetV2 for efficient image classification

🐔 Classifies Poultry Diseases like Coccidiosis, New Castle Disease, Salmonella, and Healthy

📷 Upload an image of a chicken and get instant prediction results

🌐 Flask-based web app with user-friendly interface

🎨 Modern, responsive design with pages for Home, Prediction

🛠 Technologies Used

* Python
  
* TensorFlow & Keras

* Transfer Learning (MobileNetV2)

* Flask (Web Framework)

* HTML, CSS, Bootstrap

* Jupyter Notebook

* Git & GitHub

📁 Folder Structure

poultry_project/

├── app.py                       # Flask web application

├── poultry_disease_model.h5     # Trained CNN model

├── static/                      # Static assets (images, uploads)

│   └── sample_image.jpg

├── templates/                   # HTML templates

│   ├── index.html

│   └── predict.html

📷 Sample Usage

* Train or load the model (poultry_disease_model.h5)

* Run the Flask app:

* python app.py

* Open your browser and go to http://127.0.0.1:5003/

* Navigate to the prediction page and upload an image of a chicken

* The system will display the predicted disease label instantly

📌 Notes

* The dataset is from Kaggle: Poultry Diseases Dataset

* Ensure poultry_disease_model.h5 is present in the root project folder before running the app

* You can use the small_dataset folder for faster experimentation


