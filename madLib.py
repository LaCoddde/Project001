def get_input(word_type: str):
    user_input: str = input(f"Enter a {word_type}: ")
    return user_input


noun1 = get_input("noun")
verb1 = get_input('verb')
noun2 = get_input("noun")
verb2 = get_input("verb")

story = f"""
STORY:
Once upon a time, there was a {noun1} who loved to {verb1} all day.

One day, {noun2} walked into the room and caught {noun1} in the act.

"""

print(story)
