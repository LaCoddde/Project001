from textblob import TextBlob
from dataclasses import dataclass


@dataclass
class Mood:
    emoji: str
    sentiment: float


def get_mood(input_text: str, *, sensitivity: float) -> Mood:
    """This function returns a mood. The * in the function parameters forces user to explicitly type the
       word after it. In this case, user must explicitly type the word sensitivity when calling function.
       E.x. get_mood(user_input, sensitivity=0.3)
    """
    polarity: float = TextBlob(input_text).sentiment.polarity

    friendly_threshold: float = sensitivity
    hostile_threshold: float = -sensitivity

    if polarity >= friendly_threshold:
        return Mood("🤗", polarity)
    elif polarity <= hostile_threshold:
        return Mood("🤬", polarity)
    else:
        return Mood("😐", polarity)


def run_bot():
    print("Enter some text for sentiment analysis: ")
    while True:
        user_input: str = input("You: ")
        mood: Mood = get_mood(user_input, sensitivity=0.3)

        print(f"Bot: {mood.emoji} ({mood.sentiment})")


if __name__ == '__main__':
    run_bot()
