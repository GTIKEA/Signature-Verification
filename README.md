# Signature Verification System

A Flask and Machine Learning based handwritten Signature Verification System developed using Python, OpenCV, Scikit-image, TensorFlow/Keras, and feature extraction techniques.

The application analyzes signature images, extracts geometric and statistical features, and verifies whether a signature is genuine or forged.

---

# Project Overview

This project implements an offline signature verification pipeline using image preprocessing and handcrafted feature extraction.

## The system:

- Reads signature images
- Converts RGB images to grayscale
- Performs binary thresholding
- Crops signature regions
- Extracts signature characteristics
- Compares features from genuine and forged signatures
- Uses machine learning logic for verification
- Provides a Flask-based interface for testing

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Flask | Web application framework |
| OpenCV | Image processing |
| NumPy | Numerical operations |
| Pandas | Dataset processing |
| Matplotlib | Visualization |
| Scikit-image | Feature extraction |
| SciPy | Image filtering |
| TensorFlow v1 | ML backend |
| Keras | Neural network utilities |
| Jupyter Notebook | Experimentation and training |

---

# Project Structure

```bash
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
```

---

# Core Functionalities

## 1. Image Preprocessing

The system preprocesses signature images using:

- RGB to grayscale conversion
- Gaussian filtering
- Otsu thresholding
- Binary image generation
- Signature region extraction

### Implemented Functions

```python
rgbgrey()
greybin()
preproc()
```

---

## 2. Feature Extraction

The application extracts multiple handwritten signature characteristics.

### Extracted Features

| Feature | Description |
|---|---|
| Ratio | White pixel ratio |
| Centroid | Signature center coordinates |
| Eccentricity | Shape elongation |
| Solidity | Signature density |
| Skewness | Distribution asymmetry |
| Kurtosis | Distribution sharpness |

### Implemented Functions

```python
Ratio()
Centroid()
EccentricitySolidity()
SkewKurtosis()
getFeatures()
```

---

## 3. Dataset Support

The repository contains:

### Genuine Signatures

Stored inside:

```bash
real/
```

### Forged Signatures

Stored inside:

```bash
forged/
```

The dataset includes multiple signature samples for each user.

### Example

```bash
001001_000.png
001001_001.png
```

---

# Flask Application

The Flask application provides a lightweight interface for signature verification.

## Main Flask Files

| File | Purpose |
|---|---|
| app.py | Main Flask application and ML logic |
| controller.py | Handles request routing |
| model.py | Form validation |

---

# Installation Guide

## Clone Repository

```bash
git clone https://github.com/GTIKEA/Signature-Verification.git
cd Signature-Verification
```

---

# Create Virtual Environment

## Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install flask numpy pandas matplotlib scipy scikit-image opencv-python tensorflow keras wtforms
```

---

# Running the Project

## Run Testing Script

```bash
python test.py
```

---

## Run Flask Application

```bash
cd flask_app
python app.py
```

### Default Flask Server

```bash
http://127.0.0.1:5000/
```

---

# Machine Learning Workflow

```text
Input Signature
        ↓
Image Preprocessing
        ↓
Feature Extraction
        ↓
Feature Comparison
        ↓
Verification Result
```

---

# Important Implementation Details

## TensorFlow Compatibility

The project uses:

```python
tensorflow.compat.v1
```

and disables TensorFlow v2 behavior:

```python
tf.disable_v2_behavior()
```

---

# Existing Limitations

- Hardcoded dataset paths exist in `app.py`
- No database integration
- No Docker support
- No authentication system
- TensorFlow v1 dependency
- Limited frontend implementation

---

# Recommended Improvements

## Infrastructure Enhancements

- Docker containerization
- CI/CD integration
- REST API architecture
- Cloud deployment
- Kubernetes deployment

## ML Enhancements

- CNN-based verification
- Siamese neural networks
- Deep learning embeddings
- Improved accuracy benchmarking
- Real-time signature comparison

## Security Enhancements

- User authentication
- Secure file uploads
- API validation
- Input sanitization

---

# Sample Commands

## Git Setup

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/GTIKEA/Signature-Verification.git
git push -u origin main
```

---

# Author

## Geethika Chowdary Tunga

Data Analyst

---

# License

This project is intended for educational, research, and academic purposes.
