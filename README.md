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
```
Visualizations of top words are available for both positive and negative reviews, including:
- Bar charts of most frequent words.
- WordClouds for both sentiment categories.
![download (2)](https://github.com/user-attachments/assets/9e232531-82cc-4f15-9ee5-fc8a37e7399c)
![download (1)](https://github.com/user-attachments/assets/2ab0734c-cc0e-4747-8172-d21575a3e478)
![download](https://github.com/user-attachments/assets/91825f61-bcd5-4a37-a4a1-c5447ad45abc)
![download (5)](https://github.com/user-attachments/assets/3adf3705-d5c8-4c19-8ca0-3f58724d862e)
![download (4)](https://github.com/user-attachments/assets/58c6510b-260e-421a-96a1-188d4bf9cdfa)

---
## Models Evaluation:
![Accuracy](https://github.com/user-attachments/assets/a50ce125-5537-44f7-bbc1-1c9efe77a779)
![Recall](https://github.com/user-attachments/assets/df019da5-f5bf-4501-a79b-05b214cc3d3d)
![precision](https://github.com/user-attachments/assets/5c235e4b-ec41-4384-9e1a-e200f47eea7e)
![f1_score](https://github.com/user-attachments/assets/72054e9b-b98e-47ca-942a-0a1f6ab40939)
![comparizon](https://github.com/user-attachments/assets/f095b675-3939-4e2b-b731-c608aa2a2079)
---

## 🚀 Running the App

The Streamlit application allows users to input reviews and receive real-time sentiment predictions using the trained model.

To run the app locally, use the following command:

```bash
streamlit run streamlit.py  # Replace with your actual Streamlit app script
```


---

## 📸 Streamlit App Screenshots


#  Negative
![WhatsApp Image 2025-05-18 at 09 04 23_00f78de0](https://github.com/user-attachments/assets/367dd336-65ba-41e5-a8a4-af55b06d08f3)


#  Positive
![8](https://github.com/user-attachments/assets/48867581-b548-438b-a5fb-33562e519652)

---

## 👥 Contributors

This project was developed as part of the **Natural Language Processing (NLP)** course at the **Faculty of Computers and Information, Ain Shams University**.  
The system is tailored specifically for **movie reviews sentiment analysis**.

- **مهاب محمد سيد عبدالغني** (20201700871)  
- **سندس وائل منصور عبد المنعم** (2021170242)  
- **فرح حسین محمد سالم** (2021170391)  
- **فاطمه الزهراء محمود حامد** (2021170385)  
- **جهاد السيد محمود عبدالمجيد** (2021170145)  
- **مريم سيد أحمد** (2021170506)

---




