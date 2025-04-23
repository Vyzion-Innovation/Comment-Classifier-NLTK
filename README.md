# 🧠 Comment Classifier (Django + NLTK)

This is a Django web app that classifies user-submitted comments as **"good"** or **"bad"** using **NLTK's SentimentIntensityAnalyzer (VADER)**.

---

## 🔧 Features

- Submit comments via a simple HTML form
- Automatically analyze sentiment using NLTK
- Store comments in a SQLite database
- Separate and display classified **good** and **bad** comments

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Vyzion-Innovation/Comment-Classifier-NLTK.git
cd Comment-Classifier-NLTK


###  python3 -m venv env
source env/bin/activate

### Install Dependencies
pip install -r requirements.txt

### Download VADER Lexicon
import nltk
nltk.download('vader_lexicon')

###   python manage.py migrate

###  python manage.py runserver
