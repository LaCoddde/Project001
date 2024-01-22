import random


def roll_dice(amount: int = 2) -> list[int]:
    if amount <= 0:
        raise ValueError

    rolls: list[int] = []

    for i in range(amount):
        random_roll: int = random.randint(1, 6)
        rolls.append(random_roll)

    return rolls


def main():
    while True:
        try:
            user_input: str = input("How many dice? ")

            if user_input.lower() == "exit":
                print("Thanks for playing.")
                break

            result = roll_dice(int(user_input))
            print(*result, sep=", ")
            print(f"Sum of dice: {str(sum(result))}")
        except ValueError:
            print("Enter a valid number.")


if __name__ == '__main__':
    main()
