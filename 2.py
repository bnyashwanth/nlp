import nltk
from nltk.util import ngrams
from collections import Counter, defaultdict

nltk.download('punkt')
nltk.download('punkt_tab')

sentences = [
    "The quick brown fox jumps over the lazy dog",
    "The quick brown fox is quick"
]

unigram_counts = Counter()
bigram_counts = Counter()
trigram_counts = Counter()

bigram_context = defaultdict(int)
trigram_context = defaultdict(int)

for sentence in sentences:
    tokens = nltk.word_tokenize(sentence.lower())

    unigrams = list(ngrams(tokens, 1))
    bigrams = list(ngrams(tokens, 2))
    trigrams = list(ngrams(tokens, 3))

    unigram_counts.update(unigrams)
    bigram_counts.update(bigrams)
    trigram_counts.update(trigrams)

    for bigram in bigrams:
        bigram_context[bigram[0]] += 1

    for trigram in trigrams:
        trigram_context[trigram[:2]] += 1

print("Unigram Counts:")
print(unigram_counts)

print("\nBigram Counts:")
print(bigram_counts)

print("\nTrigram Counts:")
print(trigram_counts)

print("\nUnigram Probabilities:")
total_unigrams = sum(unigram_counts.values())

for unigram, count in unigram_counts.items():
    print(unigram, ":", count / total_unigrams)

print("\nBigram Probabilities:")

for bigram, count in bigram_counts.items():
    probability = count / bigram_context[bigram[0]]
    print(bigram, ":", probability)

print("\nTrigram Probabilities:")

for trigram, count in trigram_counts.items():
    probability = count / trigram_context[trigram[:2]]
    print(trigram, ":", probability)
