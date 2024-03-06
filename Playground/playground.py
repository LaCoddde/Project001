import math

doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
keyword = "Casino"

keyword = keyword.lower()
found = []
my_dict = {}

for i, doc in enumerate(doc_list):
    print(i)
    doc_split = [word.strip(",.") for word in doc.lower().split()]
    if keyword in doc_split:
        if len(keyword) == len(doc_split[doc_split.index(keyword)]):
            found.append(i)

print(found)

my_dict["pl"] = ["loop", "flu"]

print(my_dict)

print(math.log(32, 2))

z = 5290.846
print(f"{z:.5f}")
