import os
import numpy as np
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Load trained model
model = load_model('poultry_disease_model.h5')

# Class labels (adjust if your classes are different)
labels = ['Coccidiosis', 'Healthy', 'New Castle Disease', 'Salmonella']

# Flask app setup
app = Flask(__name__)

# Home page route (index)
@app.route('/')
def home():
    return render_template('index.html')

# Route for GET STARTED button -> opens prediction page
@app.route('/upload')
def predict_page():
    return render_template('predict.html')

# Route to handle image prediction
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file uploaded", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    if file:
        # Save file to /static/
        filepath = os.path.join('static', file.filename)
        file.save(filepath)

        # Load and preprocess image
        img = load_img(filepath, target_size=(224, 224))
        x = img_to_array(img) / 255.0
        x = np.expand_dims(x, axis=0)

        # Predict
        preds = model.predict(x, verbose=0)
        pred_class = labels[np.argmax(preds)]

        # Return prediction to the HTML page
        return render_template('predict.html', prediction=pred_class, image_path=filepath)

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5003)
