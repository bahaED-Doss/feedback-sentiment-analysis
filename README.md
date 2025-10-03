# Customer Feedback Sentiment Analysis

This project is a **mini feedback management system** with **AI sentiment analysis**.
It simulates how companies (Uber, Food Delivery, etc.) analyze customer reviews.

## Features
- Add customer feedback with name, service, and text.
- Sentiment analysis via Hugging Face API (Positive / Negative / Neutral).
- **Fallback with TextBlob** if API is unavailable.
- Dashboard view (list of feedbacks with quick summary).
- Detailed view of full feedback entry.

## Installation
1. Clone this repo:
   ```bash
   git clone https://github.com/yourname/feedback_sentiment.git
   cd feedback_sentiment
2. Install dependencies:
l
pip install -r requirements.txt


Add your Hugging Face API token inside ai_api.py:

HF_HEADERS = {"Authorization": "Bearer YOUR_HF_TOKEN"}

## Usage : 

Run the program:

python main.py


## Menu options:

1: Add feedback

2: List feedbacks

3: View full feedback

4: Exit

## Example
=== Customer Feedback System ===
1. Add new feedback
2. List feedbacks
3. View full feedback
4. Exit
Choose an option: 1

Enter your name: Sarah
Enter service: Uber
Enter your feedback: The ride was late but the driver was kind
Feedback added! Sentiment = POSITIVE

## Dependencies

- requests
- textblob

