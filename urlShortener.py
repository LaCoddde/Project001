import os
from typing import Final
import requests

API_KEY: Final[str] = os.environ.get("CUTTLY_API_KEY")
BASE_URL: Final[str] = "https://cutt.ly/api/api.php"


def shorten_link(full_link: str):
    payload: dict = {"key": API_KEY, "short": full_link}
    request = requests.get(BASE_URL, params=payload)
    data: dict = request.json()

    if url_data := data.get("url"):
        if url_data["status"] == 7:
            short_link: str = url_data["shortLink"]
            print("Link: ", short_link)
        else:
            print("Error status: ", url_data["status"])


def main():
    if API_KEY is None:
        print("API key not provided. Set the CUTTLY_API_KEY environment variable.")
        return

    input_link: str = input("Enter a link: ")
    shorten_link(input_link)


if __name__ == '__main__':
    main()
