# Installation Guide

## Prerequisites

- Python 3.11
- Google Chrome / Microsoft Edge
- Git

## Clone Repository

```bash
git clone https://github.com/yourusername/Phishing-URL-Interceptor.git
```

## Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

Run

```bash
python app.py
```

Server

```
http://127.0.0.1:5000
```

## Load Extension

Open

```
chrome://extensions
```

Enable Developer Mode

Load Unpacked

Select

```
extension/
```