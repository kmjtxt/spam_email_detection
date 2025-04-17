## Data Cleaning & Preprocessing

Summary of steps taken during cleaning and processing
1. Lowercase
2. Remove email headers
3. Remove URLs
4. Remove new line indicators "\n"
5. Remove excessive white space
6. Remove non-English characters
7. Filter for emails in English (as detected by `langdetect` package
8. Remove duplicated rows
9. Tokenization
10. Remove stopwords
11. Lemmatization

## Hypotheses

Hypothesis 1 - Contextual Semantics: Words carry different semantic meanings depending on the context, differing between spam and non-spam. 
Hypothesis 2 - Lexical Semantics: Spam content is more likely to have monetary terms.
Hypothesis 3 - Structural Features: Spam emails exhibit distinct structural characteristics in their URLs compared to non-spam emails.

## Feature Engineering

1. ngrams
2. BoW & TF-IDF
