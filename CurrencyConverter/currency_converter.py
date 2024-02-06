import json
from typing import Final
import requests
import os

BASE_URL: Final[str] = "http://api.exchangeratesapi.io/v1/latest"
API_KEY: Final[str] = os.environ.get("EXCHANGERATESKEY")


def get_rates(mock: bool = False) -> dict:
    if mock:
        with open("rates.json", "r") as file:
            return json.load(file)

    payload: dict = {"access_key": API_KEY}
    request = requests.get(url=BASE_URL, params=payload)
    data = request.json()

    return data


#  print(get_rates(mock=True))


def get_currency(currency: str, rates: dict) -> float:
    currency: str = currency.upper()
    if currency in rates.keys():
        return rates.get(currency)
    else:
        raise ValueError(f"{currency} not recognized!")


def convert_currency(amount: float, base: str, vs: str, rates: dict) -> float:
    base_rate: float = get_currency(base, rates)
    vs_rate: float = get_currency(vs, rates)

    conversion: float = round((vs_rate / base_rate) * amount, 2)
    print(f"{amount:,.2f} ({base}) is: {conversion:,.2f} ({vs})")

    return conversion


def main():
    data: dict = get_rates(mock=True)
    while True:
        try:
            input_amount: float = float(input("Enter amount to convert: "))
            base_currency: str = input("Enter base currency: ").upper()
            target_currency: str = input("Enter target currency: ").upper()
            rates: dict = data.get("rates")

            convert_currency(input_amount, base_currency, target_currency, rates=rates)
            if input("Do you want to convert another currency: ").lower() in ["no", "n", "exit"]:
                break
        except ValueError:
            print("Invalid entry")


if __name__ == '__main__':
    main()
