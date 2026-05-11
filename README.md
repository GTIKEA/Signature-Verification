
Signature Verification System - README

Signature Verification System

A Flask and Machine Learning based handwritten Signature Verification System developed using Python, OpenCV, Scikit-image, TensorFlow/Keras, and feature extraction techniques.

The application analyzes signature images, extracts geometric and statistical features, and verifies whether a signature is genuine or forged.

Project Overview

This project implements an offline signature verification pipeline using image preprocessing and handcrafted feature extraction.

Technologies Used
- Python
- Flask
- OpenCV
- NumPy
- Pandas
- Matplotlib
- Scikit-image
- SciPy
- TensorFlow v1
- Keras
- Jupyter Notebook

Core Functionalities
1. Image Preprocessing
2. Feature Extraction
3. Signature Verification
4. Flask-based Testing Interface

Dataset Support
- Genuine Signatures stored in real/
- Forged Signatures stored in forged/

Installation

git clone https://github.com/GTIKEA/Signature-Verification.git
cd Signature-Verification

Install dependencies:
pip install flask numpy pandas matplotlib scipy scikit-image opencv-python tensorflow keras wtforms

Run Flask Application:
cd flask_app
python app.py

Machine Learning Workflow
Input Signature → Image Preprocessing → Feature Extraction → Feature Comparison → Verification Result

Recommended Improvements
- Docker containerization
- CI/CD integration
- CNN-based verification
- REST API architecture
- Cloud deployment
- Secure authentication

Author
Geethika Chowdary Tunga

License
Educational and research purposes only.

