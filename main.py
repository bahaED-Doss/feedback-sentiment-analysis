from ai_api import analyze_sentiment_api
from feedback import add_feedback, list_feedbacks, view_feedback

def main():
    while True:
        print("\n=== Customer Feedback System ===")
        print("1. Add new feedback")
        print("2. List feedbacks")
        print("3. View full feedback")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter your name: ")
            service = input("Enter service (Uber, Food, Ride, etc.): ")
            feedback_text = input("Enter your feedback: ")
            sentiment = analyze_sentiment_api(feedback_text)
            add_feedback(name, service, feedback_text, sentiment)
            print(f"Feedback added! Sentiment = {sentiment}")

        elif choice == "2":
            list_feedbacks()

        elif choice == "3":
            try:
                index = int(input("Enter feedback number: ")) - 1
                view_feedback(index)
            except ValueError:
                print("Invalid number.")

        elif choice == "4":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
