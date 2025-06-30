# 🖼️ Static Assets - Poultry Project

This folder contains static files used in the web application, primarily for UI/UX and testing purposes.

## 📷 Hen Images Included

The following sample poultry images are included here for demonstration and testing:

- 🐔 Coccidiosis-infected Hen
- 🐓 Hen with New Castle Disease
- 🐥 Healthy Hen
- 🐤 Hen with Salmonella

These images are used for:

- Display on the homepage (`index.html`)
- Prediction testing through the model interface
- Visual enhancement of the web application

## 📁 Folder Purpose

The `static/` directory is typically used in Flask web applications to store:

- Images (`.jpg`, `.png`)
- Stylesheets (`.css`)
- JavaScript files (`.js`)
- Uploads

## 🔗 Reference in HTML

These images can be referenced in your HTML like so:

```html
<img src="{{ url_for('static', filename='coccidiosis.jpg') }}" alt="Coccidiosis Hen">

