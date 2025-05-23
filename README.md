<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sentiment Analysis Pipeline - README</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Custom font for a clean look */
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f3f4f6; /* Light gray background */
        }
    </style>
</head>
<body class="p-4 sm:p-8 md:p-12 lg:p-16">
    <div class="max-w-4xl mx-auto bg-white rounded-xl shadow-lg p-6 sm:p-8 md:p-10 lg:p-12">
        <header class="mb-8 text-center">
            <h1 class="text-3xl sm:text-4xl font-extrabold text-gray-900 mb-2">Sentiment Analysis Pipeline</h1>
            <p class="text-md sm:text-lg text-gray-600">Documentation and Project Overview</p>
        </header>

        <section class="mb-8">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-800 mb-4 border-b-2 border-blue-500 pb-2">1. Project Description</h2>
            <p class="text-gray-700 leading-relaxed">
                This project implements a comprehensive Sentiment Analysis Pipeline designed to preprocess raw text data
                from a dataset (specifically review columns) in preparation for Natural Language Processing (NLP) tasks
                such as sentiment analysis or text classification. The pipeline covers various stages from data cleaning
                and transformation to vectorization and visualization, culminating in a deployable Streamlit application.
            </p>
        </section>

        <section class="mb-8">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-800 mb-4 border-b-2 border-blue-500 pb-2">2. Pipeline Components & Features</h2>

            <h3 class="text-xl sm:text-2xl font-semibold text-gray-700 mb-3 mt-6">2.1. Preprocessing Steps</h3>
            <ul class="list-disc list-inside text-gray-700 space-y-2 ml-4">
                <li><strong>NLTK Resources Download:</strong> Includes tokenizers (punkt), POS taggers, stopword lists, and WordNet for lemmatization.</li>
                <li><strong>Slang and Abbreviation Dictionary:</strong> A manually defined dictionary (`slang_dict`) to map informal abbreviations and internet slang to standard forms.</li>
                <li><strong>Unknown Word Detection:</strong> Utilizes `SpellChecker` to identify potentially misspelled or slang words.</li>
                <li><strong>Text Preprocessing Function:</strong>
                    <ul class="list-circle list-inside ml-6 mt-1 space-y-1">
                        <li>Removal of special characters and single letters.</li>
                        <li>Normalization of spaces.</li>
                        <li>Expansion of slang/abbreviations.</li>
                        <li>Tokenization.</li>
                        <li>Removal of stopwords and short tokens.</li>
                        <li>POS Tagging and Lemmatization.</li>
                    </ul>
                </li>
            </ul>

            <h3 class="text-xl sm:text-2xl font-semibold text-gray-700 mb-3 mt-6">2.2. Data Exploration</h3>
            <p class="text-gray-700 leading-relaxed mb-2">
                Analysis of the `prepared_reviews.csv` dataset, including:
            </p>
            <ul class="list-disc list-inside text-gray-700 space-y-2 ml-4">
                <li>Dataset overview (number of samples, missing values for reviews and labels).</li>
                <li>Detection of duplicate entries.</li>
                <li>Review length analysis (min/max characters, distribution).</li>
                <li>Sentiment distribution (`positive` vs. `negative` labels).</li>
            </ul>

            <h3 class="text-xl sm:text-2xl font-semibold text-gray-700 mb-3 mt-6">2.3. Preprocessing Functions</h3>
            <ul class="list-disc list-inside text-gray-700 space-y-2 ml-4">
                <li><code>preprocess_text()</code>: Lemmatization-based cleaning with POS tagging and slang replacement.</li>
                <li><code>preprocess_text_modified()</code>: Stemmer-based cleaning (using Porter Stemmer), primarily used for vectorization and model input.</li>
                <li>Creation of sample columns: <code>review_preprocessing_1</code> (Lemmatization) and <code>review_preprocessing_2</code> (Stemming, used for training).</li>
            </ul>

            <h3 class="text-xl sm:text-2xl font-semibold text-gray-700 mb-3 mt-6">2.4. Label Encoding</h3>
            <p class="text-gray-700 leading-relaxed">
                Conversion of categorical labels ('positive', 'negative') into numerical representations (1, 0) for model training.
            </p>

            <h3 class="text-xl sm:text-2xl font-semibold text-gray-700 mb-3 mt-6">2.5. Train-Test Split</h3>
            <p class="text-gray-700 leading-relaxed">
                Splitting the preprocessed data into training and testing sets (80% train, 20% test) with stratification to maintain label distribution.
            </p>

            <h3 class="text-xl sm:text-2xl font-semibold text-gray-700 mb-3 mt-6">2.6. Vectorization</h3>
            <ul class="list-disc list-inside text-gray-700 space-y-2 ml-4">
                <li><strong>Count Vectorizer:</strong> Transforms text data into a matrix of token counts. The fitted vectorizer is saved using `joblib`.</li>
                <li><strong>TF-IDF Vectorizer:</strong> Transforms text data into TF-IDF features, considering `min_df`, `max_df`, `sublinear_tf`, and `max_features`.</li>
            </ul>

            <h3 class="text-xl sm:text-2xl font-semibold text-gray-700 mb-3 mt-6">2.7. Visualization</h3>
            <ul class="list-disc list-inside text-gray-700 space-y-2 ml-4">
                <li><strong>Distribution of Review Lengths:</strong> Histogram showing the frequency of different review lengths.</li>
                <li><strong>Top Words (Bar Charts):</strong> Bar charts displaying the top 20 most frequent words in both positive and negative reviews after preprocessing.</li>
                <li><strong>Word Clouds:</strong> Visual representation of word frequencies for all positive and all negative reviews.</li>
            </ul>

            <h3 class="text-xl sm:text-2xl font-semibold text-gray-700 mb-3 mt-6">2.8. Streamlit Deployment</h3>
            <p class="text-gray-700 leading-relaxed">
                The project includes a Streamlit application for interactive sentiment analysis, allowing users to enter a review and get a prediction (Positive or Negative) from the trained model.
            </p>
        </section>

        <section class="mb-8">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-800 mb-4 border-b-2 border-blue-500 pb-2">3. Tools & Libraries Used</h2>
            <ul class="list-disc list-inside text-gray-700 space-y-2 ml-4">
                <li><code>pandas</code>: For data manipulation and analysis.</li>
                <li><code>matplotlib</code>: For creating static, interactive, and animated visualizations.</li>
                <li><code>seaborn</code>: For statistical data visualization.</li>
                <li><code>nltk</code> (Natural Language Toolkit): For tokenization, lemmatization, stemming, and stopword removal.</li>
                <li><code>re</code>: Python's regular expression module for text pattern matching.</li>
                <li><code>string</code>: For common string operations.</li>
                <li><code>sklearn</code> (scikit-learn): For machine learning utilities, including `train_test_split`, `CountVectorizer`, and `TfidfVectorizer`.</li>
                <li><code>pyspellchecker</code>: For spell correction and detecting unknown words.</li>
                <li><code>WordCloud</code>: For generating word cloud visualizations.</li>
                <li><code>joblib</code>: For saving and loading Python objects, specifically vectorizers.</li>
            </ul>
        </section>

        <section class="mb-8">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-800 mb-4 border-b-2 border-blue-500 pb-2">4. Contributors</h2>
            <ul class="list-disc list-inside text-gray-700 space-y-2 ml-4">
                <li>مهاب محمد سيد عبدالغني (20201700871)</li>
                <li>سندس وائل منصور عبد المنعم (2021170242)</li>
                <li>فرح حسین محمد سالم (2021170391)</li>
                <li>فاطمه الزهراء محمود حامد (2021170385)</li>
                <li>جهاد السيد محمود عبدالمجيد (2021170145)</li>
                <li>مريم سيد أحمد (2021170506)</li>
            </ul>
        </section>

        <footer class="text-center text-gray-500 text-sm mt-8 pt-4 border-t border-gray-200">
            &copy; 2025 Sentiment Analysis Pipeline. All rights reserved.
        </footer>
    </div>
</body>
</html>
