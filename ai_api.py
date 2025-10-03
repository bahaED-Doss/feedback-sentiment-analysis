import requests
from textblob import TextBlob

# Hugging Face API endpoint
HF_API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
HF_HEADERS = {"Authorization": "Bearer YOUR_HF_TOKEN"}  # replace with your HF token


def analyze_sentiment_api(text):
    """
    Try to analyze sentiment using Hugging Face API.
    Returns: "POSITIVE", "NEGATIVE", "NEUTRAL"
    """
    try:
        payload = {"inputs": text}
        response = requests.post(HF_API_URL, headers=HF_HEADERS, json=payload, timeout=5)
        response.raise_for_status()
        result = response.json()

        if isinstance(result, list) and len(result) > 0:
            label = result[0][0]['label']
            return label
        return "NEUTRAL"
    except Exception as e:
        print(f"[API ERROR] {e} → Using fallback (TextBlob)")
        return analyze_sentiment_fallback(text)


def analyze_sentiment_fallback(text):
    """
    Fallback sentiment analysis using TextBlob.
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "POSITIVE"
    elif polarity < 0:
        return "NEGATIVE"
    else:
        return "NEUTRAL"
