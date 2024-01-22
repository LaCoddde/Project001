# def decode(message_file: str) -> str:
#     # Read the pyramid structure from the file
with open('t1.txt', 'r') as file:
    pyramid_lines = file.readlines()

    print(*pyramid_lines)
    print(pyramid_lines[1])

# Create a dictionary from the lines
pyramid_numbers = {int(line.split()[0]): line.split()[1].strip() for line in pyramid_lines}

print(pyramid_numbers)


def find_pyramid(n: int) -> int:
    res = (n * (n + 1)) // 2  # Use integer division to ensure the result is an integer
    return res


maxKey = max(pyramid_numbers.keys())
num_pairs = len(pyramid_numbers)

start = 1
final = []
while start <= num_pairs:  # Adjusted the loop condition for completeness

    op = find_pyramid(start)
    if op > maxKey:
        break
    if op in pyramid_numbers:
        final.append(pyramid_numbers[op])

    print(op)
    start += 1

# Print the final result after the loop completes
print("Final List:", *final)
