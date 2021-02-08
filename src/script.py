from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
from time import sleep
import os

# convert to absolute path
load_dotenv("../.env")

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

website_url = "https://linkedin.com"

chromedriver_path = "../../ChromeDriver/chromedriver"

browser = webdriver.Chrome(chromedriver_path)


def check_exists_by_class(class_name):
    try:
        element = browser.find_element_by_class_name(class_name)
    except NoSuchElementException:
        return False
    return element


def login_to_linkedin(browser):
    browser.get(website_url)
    login_button = browser.find_element_by_class_name('nav__button-secondary')
    login_button.click()
    sleep(2)
    username = browser.find_element_by_id("username")
    username.send_keys(USERNAME)

    password = browser.find_element_by_id("password")
    password.send_keys(PASSWORD)

    browser.find_element_by_css_selector(
        ".login__form_action_container .btn__primary--large.from__button--floating").click()


def open_invitations(browser):
    browser.find_element_by_id("ember24").click()
    all_invitations = check_exists_by_class("ember-view mn-invitations-preview__manage-all artdeco-button artdeco-button--tertiary  artdeco-button--muted artdeco-button--2")

    print(all_invitations)
    if all_invitations != False:
        all_invitations.click()


if __name__ == "__main__":
    login_to_linkedin(browser)
    open_invitations(browser)
