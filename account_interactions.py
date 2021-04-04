from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from random import choice,randint
from account_actions_instagram import *

def send_message(browser=None, username_to_message=None, message_to_send=None):
    if not browser:
        raise ValueError('Browser session cannot be none')
    if not username_to_message:
        raise ValueError('Username to message cannot be empty')
    if not message_to_send:
        raise ValueError('Message to send cannot be empty')

    direct_button = browser.find_element_by_class_name('xWeGp')
    direct_button.click()

    sleep(randint(5, 10))

    new_message_button = browser.find_element_by_class_name('QBdPU ')
    new_message_button.click()

    sleep(randint(1, 10))

    mbox = browser.find_element_by_tag_name('input')
    mbox.send_keys(username_to_message)
    # mbox.send_keys(Keys.RETURN)

    sleep(randint(1, 10))


def unfollow_users(username=None, password=None, users_to_unfollow=None, number_of_users = None, unfollow_by_link=False):
    # max por dia/sessão = 90
    # max por hora = 9
    if not username:
        raise ValueError('username must not be empty')
    if not password:
        raise ValueError('password must not be empty')
    if not users_to_unfollow:
        raise ValueError('Users to unfollow must not be empty')
    if isinstance(users_to_unfollow, str):
        users_to_unfollow = [users_to_unfollow]


    number_of_users_to_unfollow = len(users_to_unfollow)
    required_hours_to_unfollow = number_of_users_to_unfollow / 5
    number_of_hours = choice([3, 4, 5, 6])
    unfollowed_users =[]
    if not unfollow_by_link:
        for i in range(number_of_hours):
            number_of_users_to_unfollow = choice([5, 6, 7, 8, 9])
            unfollowed_users.append(unfollow_users_session(username=username, password=password, number_of_users_to_unfollow=number_of_users_to_unfollow))

    return unfollowed_users