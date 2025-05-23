# ✍️ Sentiment Analysis Pipeline

This project implements a comprehensive Sentiment Analysis Pipeline designed to preprocess raw text data from a dataset (specifically review columns) in preparation for Natural Language Processing (NLP) tasks such as sentiment analysis or text classification. The pipeline covers various stages from data cleaning and transformation to vectorization and visualization, culminating in a deployable Streamlit application.

---

## 🌟 Features

- ✅ **Preprocessing Steps**: Includes downloading NLTK resources (tokenizers, POS taggers, stopwords, WordNet), using a manually defined slang and abbreviation dictionary, detecting unknown words with `SpellChecker`, and a robust text preprocessing function.
- 📊 **Data Exploration**: Overview of the `prepared_reviews.csv` dataset, including sample count, missing values, duplicates, review length analysis, and sentiment distribution.
- ⚙️ **Preprocessing Functions**: Two distinct preprocessing functions (`preprocess_text()` for lemmatization and `preprocess_text_modified()` for stemming) used for different stages.
- 🏷️ **Label Encoding**: Converts categorical labels ('positive', 'negative') to numerical (1, 0).
- ✂️ **Train-Test Split**: Divides data into training and testing sets (80/20 split) with stratification.
- 🔢 **Vectorization**: Supports both Count Vectorizer and TF-IDF Vectorizer for text representation.
- 📈 **Visualization**: Generates histograms for review lengths, bar charts for top frequent words in positive/negative reviews, and word clouds for both sentiment categories.
- 🚀 **Streamlit Deployment**: A web application allowing users to input a review and get a sentiment prediction.

---

## 🧪 Requirements

Install the required packages using:

```bash
pip install -r requirements.txt
pandas
matplotlib
seaborn
nltk
scikit-learn
pyspellchecker
wordcloud
joblib
streamlit
```
---

## 🧠 Model Details
This pipeline prepares text data for machine learning models by transforming raw reviews into numerical features.  
The `review_preprocessing_2` (stemming version) column is specifically used for training.

### Feature Extraction
- **Count Vectorizer:** Transforms text into a matrix of token counts.  
- **TF-IDF Vectorizer:** Transforms text into TF-IDF features, configured with `min_df=7`, `max_df=0.5`, `sublinear_tf=True`, and `max_features=5000`.

### Classification (Example)
While the project focuses on the preprocessing pipeline, the prepared vectorized data can be used with various classification models (e.g., Logistic Regression, Naive Bayes, SVM) from scikit-learn.

## 📤 Input Format
The script is designed to preprocess raw text data from a dataset, specifically the `review` column in a DataFrame (`df`).  
The expected dataset file is `prepared_reviews.csv`.

## 🔁 Processing Steps

### Preprocessing
- **NLTK Resources:** Downloads necessary components like punkt tokenizer, POS taggers, stopwords, and WordNet.  
- **Slang and Abbreviation Expansion:** Replaces informal terms with standard forms using a predefined dictionary (`slang_dict`).  
- **Unknown Word Detection:** Identifies words not in the dictionary using SpellChecker.  
- **Text Cleaning:** Removes special characters and single letters, normalizes spaces, tokenizes, removes stopwords and short tokens, and performs POS tagging and lemmatization.

### Data Preparation
- **Label Encoding:** Maps `'positive'` to `1` and `'negative'` to `0`.  
- **Data Splitting:** Divides the `review_preprocessing_2` column and `numerical_label` into `X_train`, `X_test`, `y_train`, `y_test`.

### Vectorization
Applies `CountVectorizer` and `TfidfVectorizer` to transform text data into numerical features for model input.

## 🎯 Sentiment Distribution
The project analyzes the distribution of sentiments in the dataset:

```python
df['label'].value_counts()

