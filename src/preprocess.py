import string
from nltk.corpus import stopwords

def preprocess_text(text):

    lower = text.lower()

    clean = lower.translate(
        str.maketrans(
            '',
            '',
            string.punctuation
        )
    )

    tokens = clean.split()

    filtered_words = []

    for word in tokens:

        if word not in stopwords.words('english'):

            filtered_words.append(word)

    return filtered_words