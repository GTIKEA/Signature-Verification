Signature Verification System
A Flask and Machine Learning based handwritten Signature Verification System developed using Python, OpenCV, Scikit-image, TensorFlow/Keras, and feature extraction techniques.
The application analyzes signature images, extracts geometric and statistical features, and verifies whether a signature is genuine or forged.
________________________________________
Project Overview
This project implements an offline signature verification pipeline using image preprocessing and handcrafted feature extraction.
The system:
•	Reads signature images
•	Converts RGB images to grayscale
•	Performs binary thresholding
•	Crops signature regions
•	Extracts signature characteristics
•	Compares features from genuine and forged signatures
•	Uses machine learning logic for verification
•	Provides a Flask-based interface for testing
________________________________________
Technologies Used
Technology	Purpose
Python	Core programming language
Flask	Web application framework
OpenCV	Image processing
NumPy	Numerical operations
Pandas	Dataset processing
Matplotlib	Visualization
Scikit-image	Feature extraction
SciPy	Image filtering
TensorFlow v1	ML backend
Keras	Neural network utilities
Jupyter Notebook	Experimentation and training
________________________________________
Project Structure
Signature-Verification/
│
├── flask_app/
│   ├── app.py
│   ├── controller.py
│   └── model.py
│
├── real/
│   └── Genuine signature dataset
│
├── forged/
│   └── Forged signature dataset
│
├── TestFeatures/
│   └── testcsv.csv
│
├── main.ipynb
├── test.py
└── README.md
________________________________________
Core Functionalities
1. Image Preprocessing
The system preprocesses signature images using:
•	RGB to grayscale conversion
•	Gaussian filtering
•	Otsu thresholding
•	Binary image generation
•	Signature region extraction
Implemented in:
rgbgrey()
greybin()
preproc()
________________________________________
2. Feature Extraction
The application extracts multiple handwritten signature characteristics.
Extracted Features
Feature	Description
Ratio	White pixel ratio
Centroid	Signature center coordinates
Eccentricity	Shape elongation
Solidity	Signature density
Skewness	Distribution asymmetry
Kurtosis	Distribution sharpness
Implemented in:
Ratio()
Centroid()
EccentricitySolidity()
SkewKurtosis()
getFeatures()
________________________________________
3. Dataset Support
The repository contains:
Genuine Signatures
Stored inside:
real/
Forged Signatures
Stored inside:
forged/
The dataset includes multiple signature samples for each user.
Example:
001001_000.png
001001_001.png
________________________________________
Flask Application
The Flask application provides a lightweight interface for signature verification.
Main Flask Files
File	Purpose
app.py	Main Flask application and ML logic
controller.py	Handles request routing
model.py	Form validation
________________________________________
Installation Guide
Clone Repository
git clone https://github.com/GTIKEA/Signature-Verification.git
cd Signature-Verification
________________________________________
Create Virtual Environment
Linux / macOS
python3 -m venv venv
source venv/bin/activate
Windows
python -m venv venv
venv\Scripts\activate
________________________________________
Install Dependencies
pip install flask numpy pandas matplotlib scipy scikit-image opencv-python tensorflow keras wtforms
________________________________________
Running the Project
Run Testing Script
python test.py
________________________________________
Run Flask Application
cd flask_app
python app.py
Default Flask server:
http://127.0.0.1:5000/
________________________________________
Machine Learning Workflow
Input Signature
        ↓
Image Preprocessing
        ↓
Feature Extraction
        ↓
Feature Comparison
        ↓
Verification Result
________________________________________
Important Implementation Details
TensorFlow Compatibility
The project uses:
tensorflow.compat.v1
and disables TensorFlow v2 behavior:
tf.disable_v2_behavior()
________________________________________
Existing Limitations
•	Hardcoded dataset paths exist in app.py
•	No database integration
•	No Docker support
•	No authentication system
•	TensorFlow v1 dependency
•	Limited frontend implementation
________________________________________
Recommended Improvements
Infrastructure Enhancements
•	Docker containerization
•	CI/CD integration
•	REST API architecture
•	Cloud deployment
•	Kubernetes deployment
ML Enhancements
•	CNN-based verification
•	Siamese neural networks
•	Deep learning embeddings
•	Improved accuracy benchmarking
•	Real-time signature comparison
Security Enhancements
•	User authentication
•	Secure file uploads
•	API validation
•	Input sanitization
________________________________________
Sample Commands
Git Setup
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/GTIKEA/Signature-Verification.git
git push -u origin main
________________________________________
Author
Geethika Chowdary Tunga
Data Analyst
________________________________________
License
This project is intended for educational, research, and academic purposes.

