# spam_email_detection

## Problem Statement
Mainly, the telecommunications industry can benefit from this solution, as SMS spam messages have been a long ongoing problem. With a strong model to predict and hence filter spam messages, customer experience and satisfaction can be enhanced as this adds a layer of protection against potential scam attempts. Additionally, the banking industry would also greatly benefit from such a solution, reducing financial loss to phishing attempts done via SMS. This is especially so as all parties – scam victims, telcos and banks – bear the consequences of in some way.  
 

## Dataset
We have selected a SMS Spam Collection dataset, which contains a total of 5574 text messages, labelled ham (real) or spam (fraudulent). The dataset is a combination of data from UK forum Grumbletext, NUS SMS Corpus, data collected by Dr Caroline Tagg for her PhD thesis, and the SMS Spam Corpus v.0.1 Big by José María Gómez Hidalgo.  


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
