from cs50 import get_int

"""
1. prompt user input < expected: between 1 and 8. inclusive>
2. Pyramid width is same as user input
3. If user fails to provide required int. re-prompt
4. Generate pyramid
"""

while True:
    try:
        height: int = get_int("Enter Pyramid height: ")
        if height < 1 or height > 8:
            print("Pyramid height can only be b/w 1 and 8")
        else:
            break
    except ValueError:
        pass

print(height)

for i in range(1, height + 1):
    print(" " * (height - i) + "#" * i + "  " + "#" * i)
