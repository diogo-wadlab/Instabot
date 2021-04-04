from time import sleep
from selenium import webdriver
from files_manipulation import read_users, write_users
from account_actions_instagram import account_login_instagram_to_account
import random


def view_follower_profile(browser, follower, search_element):
    login_button = browser.find_element_by_xpath("//a[text()='" + follower + "']")
    login_button.click()


def search_in_followers(browser=webdriver.Firefox(),username=None, password=None, users_list=None, search_element=None):
    #nao funciona
    search_match_users = []
    follower = 'marianasantos222'

    account_login_instagram_to_account(browser, username, password)

    login_button = browser.find_element_by_xpath("//span[text()='10.9k']")
    login_button.click()

    sleep(random.randint(1, 10))
    # login_button = browser.find_element_by_xpath("//h1[text()='Followers']")
    # login_button.click()
    # view_follower_profile(browser, follower, search_element)
    sleep(5)
    # browser.close()


def get_profile_page_source_without_login(browser=None, profile_username=None):
    browser_none = False
    if not profile_username:
        raise ValueError('Function needs username of profile to check')
    if not browser:
        browser = webdriver.Firefox()
        browser_none = True
    sleep(random.randint(1, 10))

    instagram_link = 'https://www.instagram.com/'
    browser.get(instagram_link + profile_username)

    sleep(random.randint(1, 10))

    cookies_accept = browser.find_element_by_xpath("//button[text()='Accept']")
    cookies_accept.click()

    sleep(random.randint(1, 10))

    page_source = browser.page_source
    if browser_none:
        browser.close()
    return page_source