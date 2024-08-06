import os
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def read_txt_files(directory):
    texts = []
    try:
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                file_path = os.path.join(directory, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    texts.append(file.read())
    except Exception as e:
        print(f"Error reading files: {e}")
    return texts

def clean_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)  # Keeps alphanumeric characters and whitespace, removes special characters
    # Tokenization
    tokens = word_tokenize(text)
    
    # Custom stop words
    stop_words = set(stopwords.words('english'))
    # Add any domain-specific stop words here
    custom_stop_words = {'etc', 'also', 'including', 'however'}
    stop_words.update(custom_stop_words)
    
    # Lemmatization instead of stemming
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    
    # Join tokens back into a single string
    cleaned_text = ' '.join(tokens)
    return cleaned_text

def clean_texts(texts):
    return [clean_text(text) for text in texts]

def write_combined_text_to_file(texts, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for text in texts:
            file.write(text + "\n")

# Main execution
directory = r'A:\SDD\Final Year Projects\AyurAI\data\Ayurveda Dataset\ayurveda_books\ayurveda books text'
texts = read_txt_files(directory)
cleaned_texts = clean_texts(texts)
output_file = 'combined_preprocessed_text.txt'
write_combined_text_to_file(cleaned_texts, output_file)
