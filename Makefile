
# Makefile for spam_email_detection project

.PHONY: install preprocess features model-deep model-logreg model-nb model-ensemble all clean

install:
	pip install -r requirements.txt

preprocess:
	jupyter nbconvert --to notebook --execute "notebooks/data cleaning and preprocessing FINAL.ipynb" --output "output/preprocessing_output.ipynb"

features:
	jupyter nbconvert --to notebook --execute "notebooks/feature engineering - ngrams.ipynb" --output "output/features_ngrams_output.ipynb"

model-deep:
	jupyter nbconvert --to notebook --execute "Models/Deep Learning.ipynb" --output "output/deep_learning_output.ipynb"

model-logreg:
	jupyter nbconvert --to notebook --execute "Models/Logistic Regression.ipynb" --output "output/logreg_output.ipynb"

model-nb:
	jupyter nbconvert --to notebook --execute "Models/NaiveBayes.ipynb" --output "output/naive_bayes_output.ipynb"

model-ensemble:
	jupyter nbconvert --to notebook --execute "Models/Model ensemble.ipynb" --output "output/ensemble_output.ipynb"

all: install preprocess features model-deep model-logreg model-nb model-ensemble

clean:
	rm -rf __pycache__ *.pyc output/
