from collections import Counter

def detect_emotions(words):

    emotions = []

    with open(
        "lexicon/emotion.txt",
        'r'
    ) as file:

        for line in file:

            clear_line = line.replace(
                "\n",''
            ).replace(
                ",",''
            ).replace(
                "'",''
            ).strip()

            word, emotion = clear_line.split(':')

            if word in words:

                emotions.append(emotion)

    return Counter(emotions)