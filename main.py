import zhuzi_files
from account_actions_instagram import *
import random
import time
import helpers
import files_manipulation
import zhuzi_files
from datetime import date
from search_in_page_source import *
from instapy import InstaPy
import selenium
import account_actions_instagram
# username="diogo.almeida96", password="(!!Md140403!!)"
username = "zhuzi.toothbrush"
password = "ZHUZILAB!!##"

def follow_session(username=None, password=None, user_to_follow_followers=None, number_of_users_to_follow=None):
    number_to_follow = random.randint(round(number_of_users_to_follow * 0.8),
                                      round(number_of_users_to_follow * 1.20))

    browser = selenium.webdriver.Firefox()

    time.sleep(random.randint(5, 10))

    browser = account_actions_instagram.account_login_instagram(browser=browser, username=username, password=password)

    time.sleep(random.randint(5, 10))

    account_actions_instagram.search_on_instagram(browser=browser, username_to_search=user_to_follow_followers,
                                                  number_of_users_to_follow=number_to_follow)

    time.sleep(random.randint(5, 10))

    browser = account_actions_instagram.account_sign_off_instagram(browser=browser)

    time.sleep(random.randint(5, 10))

    browser.close()

    time.sleep(random.randint(1200, 2100))


def unfollow_session(users={}, number_of_users_to_unfollow=None):
    users_keys = users.keys()
    for key in users_keys:
        username = key
        password = users[key]

        number_to_unfollow = random.randint(round(number_of_users_to_unfollow * 0.8),
                                            round(number_of_users_to_unfollow * 1.20))

        #followed = files_manipulation.read_users(filename=zhuzi_files.folders[username] + "\\followed.txt")
        #follow_back = files_manipulation.read_users(filename=zhuzi_files.folders[username] + "\\follow_back.txt")
        #forbidden_unfollows = files_manipulation.read_users(
           # filename=zhuzi_files.folders[username] + "\\forbidden_unfollows.txt")

        browser = selenium.webdriver.Firefox()

        time.sleep(random.randint(5, 10))

        browser = account_actions_instagram.account_login_instagram(browser=browser, username=username,
                                                                    password=password)

        time.sleep(random.randint(5, 10))

        browser, followed, follow_back, profile_followers = account_actions_instagram.unfollow_on_instagram(
            browser=browser, number_to_unfollow=number_to_unfollow)

        time.sleep(random.randint(5, 10))

        browser = account_actions_instagram.account_sign_off_instagram(browser=browser)

        time.sleep(random.randint(5, 10))

        browser.close()

        time.sleep(random.randint(1200, 2700))


def instagram_session(users={}, users_to_follow_followers={}):
    unfollow_session(users={"zhuzi.toothbrush": "ZHUZILAB!!##"}, number_of_users_to_unfollow=10)
    list_users_to_follow_followers = helpers.prepare_users(users=users_to_follow_followers,
                                                           users_to_follow_followers=users_to_follow_followers)

    for user_to_follow_followers in list_users_to_follow_followers:
        username = list(user_to_follow_followers.keys())[0]
        password = users[username]
        user_to_follow_followers = user_to_follow_followers[username]

        follow_session(username=username, password=password, user_to_follow_followers=user_to_follow_followers,
                       number_of_users_to_follow=10)

'''def instagram_session(users={}, users_to_follow_followers={}):
    list_users_to_follow_followers = helpers.prepare_users(users=users_to_follow_followers,
                                                           users_to_follow_followers=users_to_follow_followers)

    for user_to_follow_followers in list_users_to_follow_followers:
        username = list(user_to_follow_followers.keys())[0]
        password = users[username]
        number_of_users_to_follow = random.randint(10,15)
        user_to_follow_followers = user_to_follow_followers[username]
        session = InstaPy(username=username, password=password)
        session.login()
        session.follow_user_followers([user_to_follow_followers],
                                      amount=number_of_users_to_follow,
                                      sleep_delay=600,
                                      randomize=True)
        sleep(random.randint(2700, 4500))'''


new_dict = {"diogo.almeida96": ["thef2", "transfermarkt_official", "433"],
            "zhuzi.toothbrush": ["scarlettlondon", "lornaluxe", "lydiamillen"]}
            #["anitadacosta", "inescaldo", "sararsalgado"]}  # "joanavaz_"],
#{"memoraballofficial": "Memoraball2020", "zhuzi.toothbrush": "ZHUZILAB!!##"}

#print(helpers.prepare_users(users={"zhuzi.toothbrush": "ZHUZILAB!!##"},users_to_follow_followers=new_dict))

instagram_session(users={"diogo.almeida96": "(!!Md140403!!)"}, users_to_follow_followers=new_dict)
