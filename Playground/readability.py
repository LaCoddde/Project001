import re
import string

"""
Coleman-Liau index = 0.0588 * L - 0.296 * S - 15.8
    where: L is the average number of letters per 100 words
           S is the average number of sentences per 100 words in the text

- Get user input and output answer

- Count the number of letters, words, and sentences in the text
    Letter = ascii__lowercase or ascii__uppercase
    Word = sequence of characters separated by spaces <---> .split()
    Sentence = indicated by the occurrence of a period, exclamation or question mark.

- Output "Grade X"
    where: X is the grade level computed by the Coleman-Liau formula, rounded to the nearest integer

- If the resulting index number is 16 or higher (>= a senior undergrad reading), output -> "Grade 16+" != "Grade 16"

- If index is less than 1, output -> "Before Grade 1"
"""

"""
SOLUTION;
1. Get input
2. Count letters, words, and sentences
3. Compute index using formula
4. Output Grade properly

Testing:
Text? Good morning, people. and Hello World!
"""

prompt: str = input("Text: ")

count_letter: int = 0
count_words = 0
count_sentences = 0

for letter in prompt:
    for _ in string.ascii_letters:
        if letter == _:
            count_letter += 1

print(f"Number of letters: {count_letter}")

words: list[str] = [word.strip(string.punctuation) for word in prompt.split()]
count_words = len(words)
print(words)
print(f"Number of words: {count_words}")

sentences = re.split(r'(?<=[.!?]) +', prompt)
count_sentences = len(sentences)
print(sentences)
print(f"Number of sentences: {count_sentences}")

L = (count_letter / count_words) * 100
S = (count_sentences / count_words) * 100

print(f"Average number of letters/100 words is: {L}")
print(f"Average number of sentence/100 words is: {S}")

coleman_index = round((0.0588 * L) - (0.296 * S) - 15.8)

print(f"Coleman index is: {coleman_index}")

grade = ""

if coleman_index < 1:
    grade = "Before Grade 1"
elif coleman_index >= 16:
    grade = "Grade 16+"
else:
    grade = "Grade " + str(coleman_index)

print(f"Coleman Liau index is: {grade}")
