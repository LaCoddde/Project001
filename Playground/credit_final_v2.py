def checksum(credit: str) -> bool:
    total = 0
    for i, digit in enumerate(reversed(credit)):
        num = int(digit)
        if i % 2 == 0:  # Double every other digit
            num *= 2
            num = num // 10 + num % 10 if num >= 10 else num
        total += num
    return total % 10 == 0


def card_type(cc: str):
    if cc.startswith("4") and len(cc) == 16:
        print("VISA")
    elif cc.startswith(("34", "37")) and len(cc) == 15:
        print("AMEX")
    elif cc.startswith(("51", "52", "53", "54", "55")) and len(cc) == 16:
        print("MASTERCARD")
    else:
        print("Unregistered")


if __name__ == '__main__':
    while True:
        card = input("Number: ").lower()

        if card == "exit":
            break

        if card.isdigit():
            if checksum(card):
                card_type(card)
            else:
                print("Invalid")
        else:
            print("Please enter a valid numeric card number.")
