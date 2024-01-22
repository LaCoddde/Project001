from random import choice


def run_game():
    word: str = choice(["umbrella", "secret", "pythonista", "love"])

    username: str = input("Enter your name >> ")
    print(f"Welcome to hangman, {username.title()}")

    # Setup
    guessed: str = ""
    tries: int = 4

    while tries > 0:
        blanks: int = 0

        # print(word)
        print("Secret Word: ", end='')
        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print('_', end='')
                blanks += 1

        print()

        if blanks == 0:
            print("You got it!")
            break

        guess: str = input("Enter a letter: ").lower()

        if guess in guessed:
            print(f"You already used {guess}. Try another letter")
            continue

        guessed += guess

        if guess not in word:
            tries -= 1
            print(f"{guess} not in word... Number of tries remaining: {tries}")

            if tries == 0:
                print("No more tries; Game Over!")
                break


if __name__ == '__main__':
    run_game()
