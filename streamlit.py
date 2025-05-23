import streamlit as st

# Must be the first Streamlit command in your script
st.set_page_config(page_title="Sentiment Analysis", layout="centered")

import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import TreebankWordTokenizer
import base64

# Download nltk resources (only first run needed)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Load your model and vectorizer
model = joblib.load("sentiment_model.pkl")          # MultinomialNB
vectorizer = joblib.load("count_vectorizer.pkl")     # CountVectorizer

tokenizer = TreebankWordTokenizer()

def preprocess(text):
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = text.lower()
    tokens = tokenizer.tokenize(text)
    stop_words = set(stopwords.words('english'))
    # **THIS IS THE CRUCIAL CHANGE**
    # Initialize WordNetLemmatizer inside the function
    # This ensures it's properly loaded each time preprocess is called
    lemmatizer = WordNetLemmatizer()
    cleaned = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return ' '.join(cleaned)

# Function to set background image from local file
def set_background(local_img_file):
    with open(local_img_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set your background image (replace with your actual path)
set_background("background.png")

# Streamlit UI
st.title("📝 Sentiment Analysis App")
st.write("Enter a review and the model will predict whether it's **Positive** or **Negative**.")

user_input = st.text_area("Your Review")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        cleaned_text = preprocess(user_input)
        vect_text = vectorizer.transform([cleaned_text])
        prediction = model.predict(vect_text)[0]
        sentiment = "🟢 Positive" if prediction == 1 else "🔴 Negative"
        st.success(f"Predicted Sentiment: {sentiment}")