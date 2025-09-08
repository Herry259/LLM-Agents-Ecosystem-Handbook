"""
Breakup Recovery Agent
----------------------

This agent simulates a supportive friend who listens to your feelings and
offers encouragement.  It uses simple keyword matching to detect
common themes (sadness, anger, guilt) and responds with empathetic
messages.  You can expand this logic or integrate a sentiment analysis
library for richer interactions.
"""

def generate_response(user_input: str) -> str:
    text = user_input.lower()
    if any(word in text for word in ["sad", "down", "heartbroken", "depressed"]):
        return (
            "I'm sorry you're feeling this way. It's completely normal to feel sad after a breakup. "
            "Give yourself time to heal and remember that it's okay to lean on friends and family for support."
        )
    if any(word in text for word in ["angry", "mad", "upset"]):
        return (
            "Anger is a natural reaction. Try to channel that energy into something positive—exercise, hobbies, or talking with someone you trust."
        )
    if any(word in text for word in ["guilty", "fault", "blame"]):
        return (
            "It's easy to blame yourself, but relationships are complex and both people play a role. "
            "Focus on what you've learned and how you can grow from this experience."
        )
    # Default response
    return (
        "Breakups are tough, and everyone's journey is different. Be kind to yourself, "
        "surround yourself with supportive people and take things one day at a time."
    )


def main() -> None:
    print("Welcome to the Breakup Recovery Agent. Share how you're feeling or type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if not user_input:
            continue
        if user_input.strip().lower() in {"quit", "exit"}:
            print("Agent: Take care. Remember, you're not alone.")
            break
        response = generate_response(user_input)
        print(f"Agent: {response}")


if __name__ == "__main__":
    main()