import re
from typing import Final

from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.options import Options

EMAIL_REGEX: Final[str] = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


class Browser:
    def __init__(self):
        print("Starting up browser...")
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')  # Run chrome without opening it up
        self.chrome_options.add_argument('--disable-extensions')
        self.chrome_options.add_argument('--disable-gpu')

        self.browser = webdriver.Chrome(options=self.chrome_options)

    def scrape_emails(self, url: str) -> set:
        try:
            print(f"Scrapping: '{url}' for emails")
            self.browser.get(url)
            page_source: str = self.browser.page_source

            list_of_emails: set = set()
            for re_match in re.finditer(EMAIL_REGEX, page_source):
                list_of_emails.add(re_match.group())

            return list_of_emails
        except WebDriverException as e:
            print(f"Error: {e}")
            return set()

    def close_browser(self):
        print("Closing browser...")
        self.browser.close()


def main():
    browser = Browser()

    emails = browser.scrape_emails("https://www.randomlists.com/email-addresses?qty=50")

    for i, email in enumerate(emails, start=1):
        print(f"{i:3}: {email}")


if __name__ == '__main__':
    main()
