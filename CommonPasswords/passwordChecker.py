def check_password(password: str):
    with open('passwords.txt', 'r') as file:
        common_passwords: list[str] = file.read().splitlines()
        # print(common_passwords)

    for i, common_passwords in enumerate(common_passwords, start=1):
        if password == common_passwords:
            print(f"{password}: ❌ (#{i})")
            return

    print(f"{password}: ✅ (Unique)")


def main():
    while True:
        user_password = input("Enter a password: ")
        if user_password != "":
            break
        else:
            print("Password cannot be empty; try again...")

    print(user_password)
    check_password(user_password)


if __name__ == '__main__':
    main()
