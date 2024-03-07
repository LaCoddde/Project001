"""
AMEX - 15 Digits; starts with 34 or 37
MASTER - 16 Digits; starts with 51, 52, 53, 54, or 55
VISA - 13/16 Digits; starts with 4

All credit cards have a checksum built in as follows:
1. Multiply every other digit by 2, starting with the number’s second-to-last digit,
    and then add those products’ digits together.
2. Add the sum to the sum of the digits that weren’t multiplied by 2.
3. If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0),
    the number is valid!
Example: Given Visa card: 4003600000000014
    solution:
     4003600000000014 --> 4_0_6_0_0_0_0_1_
     multiply by 2
     1•2 + 0•2 + 0•2 + 0•2 + 0•2 + 6•2 + 0•2 + 4•2  --> 2 + 0 + 0 + 0 + 0 + 12 + 0 + 8

     Now let’s add those products’ digits (i.e., not the products themselves) together:
     2 + 0 + 0 + 0 + 0 + 1 + 2 + 0 + 8 = 13

     Now let’s add that sum (13) to the sum of the digits that weren’t multiplied by 2 (starting from the end):
     13 + 4 + 0 + 0 + 0 + 0 + 0 + 3 + 0 = 20

     Check: 20 % 10 == 0  <-- Valid credit card
"""

# def checksum():
#     card = input("Number: ")
#     pass
# 4098930284824
# 0123456789
# 4003600000000014
"""
    list_d = [0, 2, 12, 7, 25, 8]
    new_list = [0, 2, 1, 2, 7, 2, 5, 8]
    out_list = []
    
    for i in list_d:
        if len(str(i)) > 1:
            for j in range(len(str(i))):
                out_list.append(int(str(i)[j]))
        else:
            out_list.append(i)
"""
card = input("Number: ")

card_list: list[int] = [int(number) for number in card]
valid_list: list[int] = [number for number in card_list[-2::-2]]
# rem_list: list[int] = [number for number in card_list if number not in valid_list] <-- wrong
rem_list: list[int] = [number for number in card_list[-1::-2]]

valid_hold: list[int] = [number * 2 for number in valid_list]

# singles: list[int] = [int(str(number)[0]) for number in valid_hold]  <-- wrong

singles: list[int] = []

for num in valid_hold:
    digits = [int(digit) for digit in str(num)]
    singles.extend(digits)

singles_sum = sum(singles)
rem_sum = sum(rem_list)

print(f"Number: {card_list}")
print(f"Valid: {valid_list}")
print(f"Rem: {rem_list}")
print(f"Valid holding: {valid_hold}")
print(f"Single Valid: {singles}")
print(f"Single sum: {singles_sum}")
print(f"Rem list sum: {rem_sum}")

print(f"{singles_sum} + {rem_sum} % 10 == 0; Valid" if ((singles_sum + rem_sum) % 10 == 0)
      else f"{singles_sum} + {rem_sum} % 10 != 0; Invalid")
