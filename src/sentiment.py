from nltk.sentiment.vader import (
    SentimentIntensityAnalyzer
)

def analyze_sentiment(text):

    score = SentimentIntensityAnalyzer(
    ).polarity_scores(text)

    neg = score['neg']
    pos = score['pos']

    if neg > pos:

        return "Negative"

    elif pos > neg:

        return "Positive"

    else:

        return "Neutral"