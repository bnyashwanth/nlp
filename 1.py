
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

text = "Natural Language Processing is a fascinating field of AI. It involves processing human languages, like English!"

tokens = word_tokenize(text)
print("Tokens:", tokens)

filtered_tokens = [re.sub(r'[^\w\s]', '', token) for token in tokens]
filtered_tokens = [token for token in filtered_tokens if token]
print("Filtered Tokens:", filtered_tokens)

validated_tokens = [
    token for token in filtered_tokens
    if re.match(r'^[a-zA-Z]+$', token)
]
print("Validated Tokens:", validated_tokens)

stop_words = set(stopwords.words('english'))
filtered_tokens = [
    token for token in validated_tokens
    if token.lower() not in stop_words
]
print("Stopword Removed Tokens:", filtered_tokens)

stemmer = PorterStemmer()
stemmed_tokens = [
    stemmer.stem(token) for token in filtered_tokens
]
print("Stemmed Tokens:", stemmed_tokens)
