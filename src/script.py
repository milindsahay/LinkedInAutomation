from selenium import webdriver
from dotenv import load_dotenv
import os

# convert to absolute path
load_dotenv("../.env")

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

website_url = "https://linkedin.com"

chromedriver_path = "../../ChromeDriver/chromedriver"

browser = webdriver.Chrome(chromedriver_path)


def login_to_linkedin(browser):
    browser.get(website_url)
    login_button = browser.find_element_by_class_name('nav__button-secondary')
    login_button.click()

    username = browser.find_element_by_id("username")
    username.send_keys(USERNAME)

    password = browser.find_element_by_id("password")
    password.send_keys(PASSWORD)

    browser.find_element_by_css_selector(".login__form_action_container .btn__primary--large.from__button--floating").click()


if __name__ == "__main__":
    login_to_linkedin(browser)
