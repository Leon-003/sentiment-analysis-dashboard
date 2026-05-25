import streamlit as st

from src.preprocess import preprocess_text
from src.emotion_detector import detect_emotions
from src.sentiment import analyze_sentiment
from src.visualize import create_graph

st.title("Sentiment Analysis Dashboard")

user_input = st.text_area(
    "Enter Text"
)

if st.button("Analyze"):

    words = preprocess_text(
        user_input
    )

    emotions = detect_emotions(
        words
    )

    sentiment = analyze_sentiment(
        user_input
    )

    create_graph(emotions)

    st.subheader(
        f"Sentiment: {sentiment}"
    )

    st.write(emotions)

    st.image(
        'outputs/graphs/emotion_graph.png'
    )