import account_actions_instagram
import random
import time
import helpers
import files_manipulation
import zhuzi_files
import selenium

from datetime import date
#from keep_alive import keep_alive
#from replit import db
import json
# username="diogo.almeida96", password="(!!Md140403!!)"
username = "zhuzi.toothbrush"
password = "ZHUZILAB!!##"


def follow_session(username=None,
                   password=None,
                   user_to_follow_followers=None,
                   number_of_users_to_follow=None):
    number_to_follow = random.randint(round(number_of_users_to_follow * 0.8),
                                      round(number_of_users_to_follow * 1.20))

    browser = selenium.webdriver.Firefox()

    time.sleep(random.randint(5, 10))

    browser = account_actions_instagram.account_login_instagram(
        browser=browser, username=username, password=password)

    time.sleep(random.randint(5, 10))

    account_actions_instagram.search_on_instagram(
        browser=browser,
        username_to_search=user_to_follow_followers,
        number_of_users_to_follow=number_to_follow)

    time.sleep(random.randint(5, 10))

    browser = account_actions_instagram.account_sign_off_instagram(
        browser=browser)

    time.sleep(random.randint(5, 10))

    browser.close()

    time.sleep(random.randint(1200, 2100))


def unfollow_session(users={}, number_of_users_to_unfollow=None):
    users_keys = users.keys()
    current_date = date.today().strftime("%d_%m_%Y")

    for key in users_keys:
        username = key
        password = users[key]

        number_to_unfollow = random.randint(
            round(number_of_users_to_unfollow * 0.8),
            round(number_of_users_to_unfollow * 1.20))

        followed_key = username + "_followed"
        follow_back_key = username + "_follow_back"
        follow_rate_key = username + "_follow_rate"
        followers_key = username + "_followers"

        try:
          #followed = db[followed_key]
          print("\n\nfollowed - 1 - ", followed)
        except:
          #followed = []
          print("\n\nfollowed - 2 - ", followed)

        try:
          #follow_back = db[follow_back_key]
          print("\n\nfollow_back - 1 - ", follow_back)
        except:
          follow_back = []
          print("\n\nfollow_back - 2 - ", follow_back)

        forbidden_unfollows = []
        browser = selenium.webdriver.Firefox()

        time.sleep(random.randint(5, 10))

        browser = account_actions_instagram.account_login_instagram(
            browser=browser, username=username, password=password)

        time.sleep(random.randint(5, 10))

        browser, followed, follow_back, profile_followers = account_actions_instagram.unfollow_on_instagram(
            browser=browser,
            number_to_unfollow=number_to_unfollow,
            followed=followed,
            follow_back=follow_back,
            forbidden_unfollows=forbidden_unfollows)

        time.sleep(random.randint(5, 10))

        browser = account_actions_instagram.account_sign_off_instagram(
            browser=browser)

        time.sleep(random.randint(5, 10))

        browser.close()

        print("\n\n\n################\n#### Follow Session####\n################\n")
        print("Followed - 3 -", followed)
        print("\n\nFollow Back - 3 -", follow_back)
        print("\n\nProfile Followers - 3 -", profile_followers)
        print("\n\n\n")

        #db[followed_key] = followed
        print("followed - ", followed)
        #db[follow_back_key] = follow_back
        print("follow_back - ", follow_back)
        #db[follow_rate_key] = int(len(follow_back) / len(followed) * 100)
        print("follow_rate_key - ", follow_rate_key)
        #db[followers_key] = profile_followers
        print("followers_key - ", followers_key)

        time.sleep(random.randint(1200, 2700))


def instagram_session(users={}, users_to_follow_followers={}):
    
    users_dict_a, users_dict_b = helpers.split_users_to_follow_followers(users_to_follow_followers)
    list_users_to_follow_followers = helpers.prepare_users(
        users=users,
        users_to_follow_followers=users_dict_a)

    '''unfollow_session(users=users, number_of_users_to_unfollow=10)'''
    for user_to_follow_followers in list_users_to_follow_followers:
        username = list(user_to_follow_followers.keys())[0]
        password = users[username]
        user_to_follow_followers = user_to_follow_followers[username]

        follow_session(username=username,
                       password=password,
                       user_to_follow_followers=user_to_follow_followers,
                       number_of_users_to_follow=10)

    time.sleep(random.randint(14400, 27000))

    unfollow_session(users=users, number_of_users_to_unfollow=10)
    list_users_to_follow_followers = helpers.prepare_users(users=users, users_to_follow_followers=users_dict_b)

    for user_to_follow_followers in list_users_to_follow_followers:
        username = list(user_to_follow_followers.keys())[0]
        password = users[username]
        user_to_follow_followers = user_to_follow_followers[username]

        follow_session(username=username,
                       password=password,
                       user_to_follow_followers=user_to_follow_followers,
                       number_of_users_to_follow=10)

#keep_alive()
time.sleep(random.randint(5, 10))

new_dict = {
    "diogo.almeida96": ["thef2", "transfermarkt_official", "433", "soccerbible", "sportf", "copa90"],
    "zhuzi.toothbrush": ["scarlettlondon", "lornaluxe", "lydiamillen", "belenrodriguezreal", "valentinaferragni","la_mainoo"]
}
#["anitadacosta", "inescaldo", "sararsalgado"]}  # "joanavaz_"],
users = {"memoraballofficial": "Memoraball2020", "zhuzi.toothbrush": "ZHUZILAB!!##"}


instagram_session(users={"zhuzi.toothbrush": "ZHUZILAB!!##"},users_to_follow_followers=new_dict)