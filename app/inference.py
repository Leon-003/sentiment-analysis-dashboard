from src.preprocess import preprocess_text
from src.emotion_detector import detect_emotions
from src.sentiment import analyze_sentiment

def run_inference(text):

    words = preprocess_text(text)

    emotions = detect_emotions(words)

    sentiment = analyze_sentiment(text)

    return {
        "sentiment": sentiment,
        "emotions": emotions
    }