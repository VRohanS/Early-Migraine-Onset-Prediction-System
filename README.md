# Early Migraine Onset Prediction System

An intelligent **Machine Learning-based Early Migraine Prediction System** that continuously monitors migraine-related indicators and predicts the likelihood of an early migraine episode. The system combines **computer vision**, **audio processing**, **keystroke dynamics**, and **machine learning** to provide real-time migraine risk prediction and alert users before symptoms become severe.

The application runs in the background while monitoring environmental and behavioral factors, performs real-time analysis using a trained **Random Forest Classifier**, and displays prediction history through a Flask-based web application.

---

## Project Overview

Migraines are often preceded by early symptoms such as:

- Photophobia (Light Sensitivity)
- Phonophobia (Sound Sensitivity)
- Changes in typing behavior due to reduced concentration and motor coordination

This project automatically monitors these indicators and predicts whether the user is at risk of experiencing a migraine attack.

Instead of waiting for severe symptoms, the system provides an **early warning notification**, allowing users to take preventive measures.

---

# Features

- Real-time Light Sensitivity Detection using Webcam
- Environmental Sound Level Detection using Microphone
- Keystroke Dynamics Analysis
- Machine Learning-based Migraine Prediction
- Flask Web Dashboard
- Prediction History Storage
- SQLite Database Integration
- Background Monitoring
- High Migraine Risk Notification
- Responsive User Interface

---


# Technology Stack

## Programming Language

- Python 3.12

## Machine Learning

- Scikit-learn
- Random Forest Classifier
- Pandas
- NumPy

## Computer Vision

- OpenCV

## Audio Processing

- SoundDevice
- NumPy Audio Processing

## Keyboard Monitoring

- pynput

## Backend

- Flask

## Database

- SQLite

## Frontend

- HTML
- CSS
- JavaScript
- Bootstrap

---

# Machine Learning Pipeline

## 1. Data Collection

The system collects three major migraine-related factors.

### Light Sensitivity (Photophobia)

Captured using:

- Webcam
- OpenCV

The webcam continuously captures image frames and computes environmental brightness.

Extracted Feature:

- Average Brightness

---

### Audio Sensitivity (Phonophobia)

Captured using:

- Microphone

Extracted Feature:

- Sound Intensity
- RMS Value
- Approximate Decibel Level

---

### Typing Pattern

Captured using:

- Keyboard Events

Extracted Features:

- Typing Speed
- Keystroke Timing
- Typing Frequency
- Backspace Frequency

---

## 2. Feature Engineering

Raw sensor values are converted into numerical features.

These features become the input for the machine learning model.

---

## 3. Data Preprocessing

The dataset undergoes:

- Missing Value Handling
- Label Encoding
- Feature Scaling
- Data Cleaning
- Train-Test Split

---

## 4. Machine Learning Model

Algorithm Used:

**Random Forest Classifier**

Reason for choosing Random Forest:

- High Accuracy
- Robust to Noise
- Handles Mixed Features
- Reduces Overfitting
- Fast Prediction
- Suitable for Medical Classification Problems

---

# Dataset Information

This project combines information from two publicly available datasets.

---

## 1. Migraine Dataset

Used for migraine symptom prediction.

Contains symptoms such as:

- Photophobia
- Phonophobia
- Nausea
- Vomiting
- Migraine Intensity
- Migraine Frequency

Target Variable:

```
Migraine
```

Binary Classification

- 1 → Migraine
- 0 → No Migraine

---

## 2. CMU Keystroke Dynamics Dataset

Dataset:

**DSL-StrongPasswordData**

Source:

Carnegie Mellon University

Used to obtain realistic typing behavior.

Features include:

- Hold Time
- Flight Time
- Typing Duration
- Key Timing

The extracted typing characteristics are integrated with migraine symptoms for prediction.

---

# Background Monitoring

The monitoring modules run continuously while the application is active.

The system:

- Captures webcam brightness
- Measures microphone sound level
- Records typing dynamics
- Generates feature vectors
- Predicts migraine risk
- Saves prediction history

---

# Web Dashboard

The Flask application provides:

- User Login
- Real-Time Prediction
- Prediction History
- Recorded Sensor Values
- Migraine Risk Status
- Database Records

---

# Database

SQLite stores:

- Date
- Time
- Brightness
- Audio Level
- Typing Speed
- Migraine Prediction
- Prediction Confidence

---

# Notification System

When the predicted migraine probability exceeds the predefined threshold, the system immediately displays an alert recommending preventive actions.

---

# Applications

- Early Migraine Detection
- Personal Health Monitoring
- Smart Healthcare Systems
- Remote Patient Monitoring
- AI-assisted Medical Decision Support

---

# Future Improvements

- Deep Learning-based Prediction Models
- Wearable Device Integration
- Heart Rate Monitoring
- Sleep Pattern Analysis
- Mobile Application
- Cloud Deployment
- Personalized Migraine Risk Profiles
- Real-time Analytics Dashboard

---

