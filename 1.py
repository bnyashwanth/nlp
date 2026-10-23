
import re, nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

text = "Natural Language Processing is a fascinating field of AI. It involves processing human languages, like English!"

# Tokenization
t = word_tokenize(text)
print("Tokens:", t)

# Filtration
t = [re.sub(r'[^\w\s]', '', x) for x in t]
t = [x for x in t if x.isalpha()]
print("Filtered:", t)

# Script Validation
t = [x for x in t if re.match(r'^[a-zA-Z]+$', x)]
print("Validated:", t)

# Stop Word Removal
stop_words = set(stopwords.words('english'))
t = [x for x in t if x.lower() not in stop_words]
print("Without Stopwords:", t)

# Stemming
stemmer = PorterStemmer()
t = [stemmer.stem(x) for x in t]
print("Stemmed:", t)
