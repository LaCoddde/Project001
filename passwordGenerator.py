import string
import secrets


def contains_upper(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True

    return False


def contains_symbols(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True

    return False


# using string library makes it easier for us get alphabets and symbols
# print(string.punctuation, string.ascii_uppercase)

def generate_password(length: int, symbols: bool, uppercase: bool) -> str:
    combination: str = string.ascii_lowercase + string.digits

    if symbols:
        combination += string.punctuation

    if uppercase:
        combination += string.ascii_uppercase

    combination_length = len(combination)
    new_password: str = ""

    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]
    if contains_symbols(new_password) and contains_upper(new_password):
        return new_password
    else:
        return generate_password(length, symbols, uppercase)


if __name__ == '__main__':
    pass_length: int = int(input(f"Enter Password Length: "))
    while pass_length < 6:
        print("Password length must be at least 6 characters.")
        pass_length = int(input(f"Enter Password Length: "))

    for i in range(1, 6):
        new_pass: str = generate_password(length=pass_length, symbols=True, uppercase=True)
        specs: str = f"U: {contains_upper(new_pass)}, S: {contains_symbols(new_pass)}"
        print(f"{i} -> {new_pass} ({specs})")
