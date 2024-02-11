from weather_api import get_weather, get_weather_details, Weather


def main():
    user_city: str = input("Enter target city: ").lower()

    # Get current weather details
    try:
        current_weather: dict = get_weather(user_city, mock=False)
        weather_details: list[Weather] = get_weather_details(current_weather)

        # Get the current days
        dfmt: str = "%d/%m/%y"
        days: list[str] = sorted({f'{date.date:{dfmt}}' for date in weather_details})
        # days: list[str] = sorted(list({f'{date.date:{dfmt}}' for date in weather_details}))  <- does same as above
        # print(days)

        for day in days:
            print(day)
            print("-------")

            grouped: list[Weather] = [current for current in weather_details if f"{current.date:{dfmt}}" == day]
            for element in grouped:
                print(element)

            print()
    except Exception:
        print("Please enter a valid city name.")
        main()


if __name__ == '__main__':
    main()
