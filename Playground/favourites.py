import csv
from collections import Counter

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    counts = Counter()

    for row in reader:
        favorite = row["problem"]
        counts[favorite] += 1

    # counts = {}
    #
    # for row in reader:
    #     favorite = row["language"]
    #     if favorite in counts:
    #         counts[favorite] += 1
    #     else:
    #         counts[favorite] = 1

# for lang in sorted(counts, key=counts.get, reverse=True):  # sort dictionary by values
#     print(f"{lang}: {counts[lang]}")

problem = input("Enter favorite problem: ")
print(f"{problem}: {counts[problem]}")

for lang, count in counts.most_common():  # sort dictionary by values
    print(f"{lang}: {counts[lang]}")

print("-" * 20)

for lang, count in counts.items():
    print(f"{lang}: {count}")

#     scratch, c, python = 0, 0, 0
#
#     for i, row in enumerate(reader, 1):
#         print(i, ": ", row["language"])
#
#         if row["language"] == "Scratch":
#             scratch += 1
#         elif row["language"] == "C":
#             c += 1
#         elif row["language"] == "Python":
#             python += 1
#
#
#
# print()
# print(f"Scratch: {scratch}")
# print(f"C: {c}")
# print(f"Python: {python}")
