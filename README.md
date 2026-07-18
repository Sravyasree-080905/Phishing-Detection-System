# 🛡️ Phishing URL Interceptor

> A Machine Learning powered browser extension that detects and blocks phishing websites in real time.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-Backend-green)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-orange)
![Chrome Extension](https://img.shields.io/badge/Chrome-Extension-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📌 Overview

Phishing URL Interceptor is a browser extension integrated with a Flask backend and a Machine Learning model to detect phishing websites in real time.

Whenever a user opens a webpage, the extension securely sends the URL to the backend API. The backend extracts phishing-related URL features and predicts whether the website is **SAFE** or **PHISHING** using a trained Machine Learning model.

If a phishing website is detected, the extension immediately blocks access and displays a security warning page, helping users avoid credential theft and online scams.

## ✨ Features

- 🔍 Real-time phishing URL detection
- 🌐 Browser extension for automatic website monitoring
- 🤖 Machine Learning based URL classification
- ⚡ Flask REST API for prediction
- 🛑 Automatic blocking of malicious websites
- 📊 Feature extraction from URLs
- 🔒 Helps protect users from phishing attacks

## 🛠️ Tech Stack

### Frontend
- HTML
- CSS
- JavaScript
- Chrome Extension (Manifest V3)

### Backend
- Python
- Flask
- Flask-CORS

### Machine Learning
- Scikit-learn
- Joblib
- Pandas

### Deployment
- Render (Flask REST API)
- Microsoft Edge Extension

## 📂 Project Structure

```
Phishing-URL-Interceptor
│
├── backend/
│   ├── app.py
│   ├── feature_extractor.py
│   ├── phishing_model.pkl
│   ├── requirements.txt
│   └── runtime.txt
│
├── extension/
│   ├── manifest.json
│   ├── background.js
│   ├── block.html
│
├── screenshots/
├── docs/
├── architecture/
│
├── README.md
├── LICENSE
└── .gitignore
```

## 🏗️ System Architecture

![Architecture](architecture/architecture_diagram.png)
