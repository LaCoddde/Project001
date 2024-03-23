import string


def reverse_vowels(prompt: str):
    pass


user_input = "social"
vowels = "aeiouAEIOU"

user_vowels = [vowel for vowel in user_input[-1::-1] if vowel in vowels]

print(user_vowels)
print(user_input[2])

j = 0
result = ""

for char in user_input:
    if char in vowels:
        result += user_vowels[j]
        j += 1
    else:
        result += char

print(result)
