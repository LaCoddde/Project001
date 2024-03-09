def checksum(credit: str) -> bool:
    card_list: list[int] = [int(number) for number in credit]
    valid_list: list[int] = [number for number in card_list[-2::-2]]
    rem_list: list[int] = [number for number in card_list[-1::-2]]

    valid_hold: list[int] = [number * 2 for number in valid_list]

    singles: list[int] = []

    for num in valid_hold:
        digits = [int(digit) for digit in str(num)]
        singles.extend(digits)

    singles_sum = sum(singles)
    rem_sum = sum(rem_list)

    return True if ((singles_sum + rem_sum) % 10 == 0) else False


def card_type(cc: str):
    if cc.startswith("4") and len(cc) in [16, 13]:
        print("VISA")

    # elif (card[:2] in [[3, 7], [3, 4]]) and len(card) == 15:
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
            print("Enter numbers only!")
