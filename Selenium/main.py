import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Browser:
    def __init__(self, driver: str):
        print("Starting up...")
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service)

    def open_page(self, url: str):
        print(f"Opening: {url}")
        self.browser.get(url)

    def close_browser(self):
        print("Closing browser...")
        self.browser.close()


if __name__ == '__main__':
    browser = Browser('./chromedriver')

    browser.open_page("https://www.python.org")
    time.sleep(5)

    # New selenium update... making it easy to drive browsers without additional installations
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    print(driver.title)
    time.sleep(5)
