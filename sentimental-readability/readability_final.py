import re
import string


def get_grade(user_input: str):
    count_letter: int = 0

    # counting letters in user input
    for letter in user_input:
        for _ in string.ascii_letters:
            if letter == _:
                count_letter += 1

    # counting words
    words: list[str] = [word.strip(string.punctuation) for word in user_input.split()]
    count_words = len(words)

    # counting sentences
    sentences = re.split(r'(?<=[.!?]) +', user_input)
    count_sentences = len(sentences)

    L = (count_letter / count_words) * 100
    S = (count_sentences / count_words) * 100

    coleman_index = round((0.0588 * L) - (0.296 * S) - 15.8)

    if coleman_index < 1:
        print("Before Grade 1")
    elif coleman_index >= 16:
        print("Grade 16+")
    else:
        print("Grade " + str(coleman_index))


if __name__ == '__main__':
    while True:
        prompt = input("Text: ")

        if prompt.lower() == "exit":
            break
        else:
            get_grade(prompt)
