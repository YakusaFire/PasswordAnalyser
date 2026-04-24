import nltk
nltk.download("cess_fra")  # Corpus français

from nltk.corpus import cess_fra
mots = list(set(cess_fra.words()))
print(mots[:10])