

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

All datasets were consolidated and cleaned to retain only English email bodies and binary spam labels. Due to storage constraints, all of our raw datasets have been saved in a google drive folder instead. 

---

##  Data Preprocessing

- Language filtering with `langdetect`
- Removal of headers, URLs, whitespace, and duplicates
- Tokenization, stopword removal, and lemmatization using `NLTK`
- Final dataset: 126,008 emails (cleaned, labeled, and tokenized)

Cleaned dataset has been stored in a google drive folder. 

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


Alsaleh, M., & Alarifi, A. (2016). Analysis of web spam for Non-English content: Toward more effective language-based classifiers. PLOS ONE, 11(11), e0164383. https://doi.org/10.1371/journal.pone.0164383  

Androutsopoulos, I., Koutsias, J., Chandrinos, K. V., & Spyropoulos, C. D. (2000). An experimental comparison of naive Bayesian and keyword-based anti-spam filtering with personal e-mail messages. In Proceedings of the 23rd Annual International ACM SIGIR Conference on Research and Development in Information Retrieval (pp. 160–167). ACM. 

Bholen, S. (2024, November 22). How to spot and mitigate phishing lures: A complete guide to protecting yourself and your... Medium. https://medium.com/@scottbolen/how-to-spot-and-mitigate-phishing-lures-a-complete-guide-to-protecting-yourself-and-your-a0b3bde081a6 

Bhowmick, A., & Hazarika, S. M. (2016, June 3). Machine learning for e-mail spam filtering: Review, techniques and trends. arXiv. https://arxiv.org/abs/1606.01042 

CEAS Spam Track. (2008). CEAS Spam Track Corpus. Conference on Email and Anti-Spam (CEAS). https://www.ceas.cc/ 

Champa, A. I., Rabbi, M. F., & Zibran, M. F. (2024). Curated datasets and feature analysis for phishing email detection with machine learning. In Proceedings of the 3rd IEEE International Conference on Computing and Machine Intelligence (ICMI) (pp. 1–7). IEEE. 

Champa, A. I., Rabbi, M. F., & Zibran, M. F. (2024). Why phishing emails escape detection: A closer look at the failure points. In Proceedings of the 12th International Symposium on Digital Forensics and Security (ISDFS) (pp. 1–6). IEEE. 

Chia, O. (2023, June 27). 8,500 phishing cases in Singapore in 2022; more than 80% spoofed a bank or financial service. The Straits Times. https://www.straitstimes.com/tech/phishing-attempts-doubled-in-2022-as-scams-ransomware-attacks-continue-to-plague-s-pore-csa 

Chua, N. (2025, February 25). Scam victims in Singapore lose record $1.1 billion in 2024; highest number of cases ever reported. The Straits Times. https://www.straitstimes.com/singapore/scam-victims-in-spore-lose-record-1-1-billion-in-2024-highest-number-of-cases-ever-reported 

Cofense. (2023, February 23). URLs 4x more likely than phishing attachments to reach users. https://cofense.com/blog/urls-4x-more-likely-than-phishing-attachments-to-reach-users/ 

Ferrara, E. (2019). The history of digital spam. Communications of the ACM, 62(8), 82–91. https://doi.org/10.1145/3299768 

George, M. S., Teunisse, A. K., & Case, T. I. (2020). Gotcha! Behavioural validation of the gullibility scale. Personality and Individual Differences, 162, 110034. https://doi.org/10.1016/j.paid.2020.110034 

Georgiou, E., Dikaiakos, M. D., & Stassopoulou, A. (2008). On the properties of spam-advertised URL addresses. Journal of Network and Computer Applications, 31(4), 966–985. https://doi.org/10.1016/j.jnca.2007.01.003 

Klimt, B., & Yang, Y. (2004). The Enron corpus: A new dataset for email classification research. In Machine Learning: ECML 2004 (pp. 217–226). Springer. https://doi.org/10.1007/978-3-540-30115-8_22 

Licato, J. (2024, November 22). AI-generated spam may soon be flooding your inbox. The Straits Times. https://www.straitstimes.com/opinion/ai-generated-spam-may-soon-be-flooding-your-inbox 

McAfee. (2020, October 25). Short-URL services may hide threats. McAfee Blog. https://www.mcafee.com/blogs/other-blogs/mcafee-labs/short-url-services-may-hide-threats/ 

Nazario, J. (2008). Phishing Corpus. https://monkey.org/~jose/phishing/ 

Petrosyan, A. (2024, December 9). Highest number of daily spam e-mails by country 2024. Statista. https://www.statista.com/statistics/1270488/spam-emails-sent-daily-by-country/ 

Rajivan, P., & Gonzalez, C. (2018). Creative persuasion: A study on adversarial behaviors and strategies in phishing attacks. Frontiers in Psychology, 9, 135. https://doi.org/10.3389/fpsyg.2018.00135 

SpamAssassin Public Corpus. (2006). SpamAssassin Public Corpus. Apache Software Foundation. http://spamassassin.apache.org/publiccorpus/ 

The University of British Columbia. (2024, September 17). Don’t be fooled: Understanding the risks of quid pro quo cyber attacks. Privacy Matters @ UBC. https://privacymatters.ubc.ca/quid-pro-quo 

TREC Public Spam Track. (2007). TREC Public Spam Track Corpus. National Institute of Standards and Technology. https://plg.uwaterloo.ca/~gvcormac/treccorpus/ 


