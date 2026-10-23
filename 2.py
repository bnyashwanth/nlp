import nltk
from nltk.util import ngrams
from collections import Counter

nltk.download('punkt')
nltk.download('punkt_tab')

sentences = [
    "The quick brown fox jumps over the lazy dog",
    "The dog barks at the fox",
    "The fox is quick and the dog is lazy",
    "The quick dog jumps over the lazy fox"
]

words = [nltk.word_tokenize(s.lower()) for s in sentences]

for n in [1, 2, 3]:
    count = Counter()
    prev = Counter()

    for sentence in words:
        count.update(ngrams(sentence, n))
        if n > 1:
            prev.update(ngrams(sentence, n - 1))

    print("\n", n, "-Gram Probabilities:")

    for gram, frequency in count.items():
        if n == 1:
            probability = frequency / sum(count.values())
        else:
            probability = frequency / prev[gram[:-1]]

        print(" ".join(gram), ":", round(probability, 4))