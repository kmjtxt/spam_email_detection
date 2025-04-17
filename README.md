# spam_email_detection

## Abstract

With the prominence of technology throughout the decades, spam emails have become more pertinent and a more accessible avenue for scam attempts to occur. Spam emails can result in financial losses and the compromise of personal and confidential information for both individuals and companies. Yet, we do not have the luxury of time to individually review our emails and deduce if they are a spam or non-spam email. Thus, our project aims to model an effective machine learning solution to filter spam emails, to minimise the odds of becoming a victim of these virtual scam practices and protect individuals in both a personal and corporate setting and improve user experience. Our dataset collected from Kaggle and Zenodo are used to supplement our models – a logistic regression model utilising Bag-of-Words, TF-IDF and n-grams features served as our baseline, while Naive Bayes and deep learning models were further implemented as challengers. Our models are then evaluated vis-a-vis their F1-score due to its balance between precision and recall. Our project was not met without any challenges – from deciding the steps taken for the preprocessing of our dataset to balance between providing sufficient information and reducing noise for model training and extracting the relevant features that produces ideal results. From our model, the error-based ensemble model we constructed by combining Naive Bayes and Logistic regression produced the most optimal results, with potential to further pipeline in fraud detection and email security systems. 

 

## Problem Statement 
 

With a record high of $1.1 billion loss to scams and an estimated 7.2 billion spam emails sent out daily in Singapore in 2024, emails remain an easy and scalable medium for scammers to prey on victims, leading to unprecedented financial losses. The dynamic nature of spam emails presents an ongoing challenge of filtering spam emails to deter access to them. 

 

Our solution aims to filter such malicious spam emails to minimise damages. Through such direct communication, scammers can extract confidential information, resulting in scams like account takeovers and identity theft. Filtering spam content also enhances user experience by reducing inbox clutter. Our finalised dataset contains two key columns – label (spam or not) and the email content. The spam emails considered include phishing attempts, promotional contents and personal information extraction. 

 

This project primarily benefits email providers (e.g., Gmail, Outlook) and the financial institutions. Building on the existing spam filtering techniques adopted by email providers, our project aims to minimise spam while preserving legitimate emails to minimise disruption for users. This is essential to prevent loss of important emails due to false positives, which are still prevalent in today’s filtering algorithms. Additionally, financial institutions are key targets of phishing attempts so stronger spam filtering techniques can minimise financial loss for both the institutions and their customers.

## Structure of our repository
```
├── LICENSE                   # Open-source license if one is chosen
├── Makefile                 # Makefile with convenience commands like `make data` or `make train`
├── README.md                # The top-level README for developers using this project
├── data/
│   ├── processed/           # Our processed and cleaned files stored in a publicly accessible Google Drive folder
│   └── raw/                 # Our raw files stored in a publicly accessible Google Drive folder
├── docs/                    # A default mkdocs project for documentation (see www.mkdocs.org)
├── models/                  # Trained and serialized models
├── notebooks/               # Jupyter notebooks; naming convention includes ordering, creator’s initials, and a short description
├── references/              # Data dictionaries, manuals, and other explanatory materials
├── reports/                 # Generated analysis in formats like HTML, PDF, LaTeX
├── figures/                 # Generated graphics and figures for reporting
├── requirements.txt         # Requirements file (generated with `pip freeze > requirements.txt`)
├── setup.cfg                # Configuration file for flake8
└── {{cookiecutter.module_name}}/
    ├── __init__.py          # Initializes the Python module
    ├── config.py            # Stores useful variables and configuration
    ├── dataset.py           # Scripts to download or generate data
    ├── features.py          # Code to create features for modeling
    └── modeling/
        ├── __init__.py      # Initializes the modeling subpackage
        ├── predict.py       # Code to run model inference with trained models
        ├── train.py         # Code to train models
        └── plots.py         # Code to create visualizations
```
