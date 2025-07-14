
# 📰 Fake News Detection using Passive Aggressive Classifier and TF-IDF

## 🧠 Overview

This project presents a machine learning-based classifier for detecting fake news articles using natural language processing (NLP) techniques. We employ a Passive Aggressive Classifier trained on TF-IDF vector representations of news text. The system demonstrates strong performance (92% accuracy), and is deployed as a user-friendly Streamlit web app for real-time classification.

The goal of this research-style application is to explore the feasibility of rapid, high-accuracy misinformation detection with lightweight models, enabling scalable deployment for content moderation and media verification tasks.

## 🧪 Methodology

### 🔎 Dataset
- Source: [Kaggle - Fake News Dataset](https://www.kaggle.com/datasets/hassanamin/textdb3/data)
- Structure: Binary classification of articles labeled as **fake** or **reliable**

### ⚙️ Text Preprocessing
- Lowercasing
- Stopword removal
- Stemming
- TF-IDF vectorization

### 🔧 Model
- Classifier: Passive Aggressive Classifier (`scikit-learn`)
- Training Data: TF-IDF vectors of preprocessed news articles
- Accuracy: **~92.4%** on test data

---

## 🧱 Project Structure

```bash
.
├── app.py               # Streamlit web app
├── vectorizer.pkl       # Serialized TF-IDF vectorizer
├── pac.pkl              # Serialized trained model
├── requirements.txt
└── README.md
```

---

## 🖥️ Streamlit Web App

We created a simple interface for real-time fake news detection.

### 🔄 How to Run

```bash
# 1. Clone the repository
git clone https://github.com/ravina029/FakeNewsClassifier.git
cd FakeNewsClassifier

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the app
streamlit run app.py
```

---

## 📸 App Screenshots

| Input Example | Prediction |
|---------------|------------|
| ![Fake News](../../Downloads/Fake.png) | Fake |
| ![Reliable News](../../Downloads/reliable.png) | Reliable |

---


## 🎯 Key Features

- Passive Aggressive Classifier with high test accuracy (>92%)
- TF-IDF based feature extraction
- Clean and responsive Streamlit UI
- Rapid text input and classification pipeline
- Fully open-source and reproducible

---

## 📈 Results

- Accuracy: **92.4%** on held-out test set
- Demonstrates robustness of linear models for text classification
- Highlights feasibility of using fast learners for misinformation detection

---

## 🔬 Research Extensions

This project could be developed into a more rigorous research prototype through:

- Comparison with other models: Logistic Regression, Naive Bayes, BERT
- Human-in-the-loop validation (crowd-sourced annotations)
- Temporal drift analysis: Does fake news evolve in language style?
- Explainability: LIME/SHAP for model interpretation

---

## 🔄 Future Work

- Integrate additional linguistic features (n-grams, syntactic parsing)
- Improve model generalization to cross-domain articles
- Expand dataset coverage across time and geography
- Enhance UI with feedback logging and usage analytics

---












