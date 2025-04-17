

# Spam Email Detection using Machine Learning

This repository contains the code and resources for our group project for DSA4263: Sense Case Making Analysis (Business & Commerce) at NUS. Our project focuses on building a robust spam email classifier using various NLP and machine learning techniques to enhance cybersecurity and improve email filtering.

---

##  Project Overview

Spam emails pose a significant risk to both individuals and organizations, contributing to fraud, phishing, and loss of confidential data. Our solution leverages classical machine learning and deep learning models to accurately classify emails as spam or non-spam, with a strong emphasis on model interpretability and deployment readiness.

---

##  Dataset

We used a combination of public datasets sourced from:
- Enron Corpus
- Ling-Spam Dataset
- SpamAssassin Corpus
- TREC, CEAS, and Nazario Spam Corpora
- Kaggle Email Datasets

All datasets were consolidated and cleaned to retain only English email bodies and binary spam labels.

---

##  Data Preprocessing

- Language filtering with `langdetect`
- Removal of headers, URLs, whitespace, and duplicates
- Tokenization, stopword removal, and lemmatization using `NLTK`
- Final dataset: 126,008 emails (cleaned, labeled, and tokenized)

---

##  Exploratory Analysis

Three key hypotheses were tested:
1. **Contextual semantics (Word2Vec)** – Rejected (worsened model performance)
2. **Lexical semantics (Monetary terms)** – Accepted (spam commonly contains monetary language)
3. **URL structural patterns** – Rejected (URL-based features did not improve performance)

---

##  Feature Engineering

We engineered features from:
- **BoW** and **TF-IDF** vectors (word/char n-grams)
- **Part-of-speech sequences**
- Combined features into a unified sparse matrix for model training

---

##  Models & Performance


| Model               | Accuracy | Precision | Recall  | F1 Score | AUC    |
|---------------------|----------|-----------|---------|----------|--------|
| Logistic Regression | 97.98%   | 97.35%    | 98.40%  | 97.87%   | 0.9955 |
| Naive Bayes         | 95.25%   | 95.21%    | 94.73%  | 94.97%   | 0.9818 |
| Model Ensemble      | 96.99%   | 94.95%    | **98.90%**  | 96.89%   | 0.9808 |
| Deep Learning       | **98.37%** | **98.66%**  | 97.90%  | **98.28%** | **0.9983** |




---

##  Model Explainability

- **Logistic Regression:** Top words influencing spam classification visualized.
- **Naive Bayes:** Log-probability differences of influential features.
- **Deep Learning (FFNN):** LIME used for local explanations of predictions.

---

##  Deployment Proposal

1. Email preprocessing pipeline
2. Feature extraction
3. Ensemble classifier with confidence logic
4. Final decision routing to inbox/quarantine
5. Admin dashboard for feedback and auditing

---

##  Limitations & Future Work

- Model currently supports only **English** emails
- Future exploration of **time series spam patterns**
- Consideration of metadata (sender, timestamp) for spoof detection
- Expansion into **multilingual spam detection**

---

##  Authors

- Chua Yong Yaw Louis 
- Kang Qi Ying 
- Tang Xitong 
- Vijayakumar Sabarina 
- Yong Hui Qi 

---

##  License

MIT License 
---

##  References

All references used in this project are cited in the final report located in `/docs/Group_Paper_Writeup.pdf`.



