from random import randint

# lower_num, higher_num = 1, 10
lower_num = int(input("Enter a lower bound: "))
higher_num = int(input("Enter an upper bound: "))
random_number = randint(lower_num, higher_num)

print()

guess = 5

print(f"Guess number in range of {lower_num} and {higher_num}")

while guess > 0:
    try:
        user_guess: int = int(input("Guess: "))
    except ValueError as e:
        print("Please enter a valid number.")
        continue

    if user_guess > random_number:
        print(f"{user_guess} is higher than Magic Number")
    elif user_guess < random_number:
        print(f"{user_guess} is lower than Magic Number")
    else:
        print(f"You guessed it! {user_guess} is the correct answer.")
        break
    print()

    guess = guess - 1
    print(f"Number of guesses left: {guess}")

if guess < 1:
    print("Out of guesses. Game Over!")
