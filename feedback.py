feedbacks = []  # global storage

def add_feedback(name, service, feedback_text, sentiment):
    """
    Store feedback in memory.
    """
    entry = {
        "name": name,
        "service": service,
        "feedback": feedback_text,
        "sentiment": sentiment
    }
    feedbacks.append(entry)


def list_feedbacks():
    """
    Display all feedbacks in summary mode.
    """
    print("\n=== Feedback Dashboard ===")
    for i, fb in enumerate(feedbacks, 1):
        print(f"{i}. {fb['name']} | {fb['service']} | {fb['sentiment']}")


def view_feedback(index):
    """
    Show full feedback details.
    """
    if 0 <= index < len(feedbacks):
        fb = feedbacks[index]
        print("\n--- Full Feedback ---")
        print(f"Name: {fb['name']}")
        print(f"Service: {fb['service']}")
        print(f"Feedback: {fb['feedback']}")
        print(f"Sentiment: {fb['sentiment']}")
    else:
        print("Invalid index.")
