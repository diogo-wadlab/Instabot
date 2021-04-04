import zhuzi_files
from account_actions_instagram import *
import random
import time
import helpers
import files_manipulation
import zhuzi_files
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

def search_for_country(page_source, country_code):
    if type(country_code) is str:
        country_code = [country_code]
    for i in range(len(country_code)):
        query_country = '"country_code":"' + country_code[i] + '"'
        if query_country in page_source:
            return True
    return False


def search_if_private(page_source):
    # true if private
    query_private = '"is_private":true'
    return query_private in page_source


def search_if_follow_back(page_source):
    query_follow_back = '"follows_viewer":true'
    return query_follow_back in page_source


def search_number_if_business_account(page_source):
    query_follow_back = '"is_business_account":true'
    return query_follow_back in page_source


def search_number_of_following(page_source=None):
    print("\n\n Following \n\n")
    direct_page = "</span> following</a>" not in page_source
    #direct_page = '<html><head><meta name="viewport" content="width=device-width">' not in page_source
    if direct_page:
        if "k Following" in page_source:
            following = page_source.split("Followers, ")[1].split("k Following,")[0]
            thousands = following.split(".")[0]
            hundreds = following.split(".")[1]
            following = int(thousands) * 1000 + int(hundreds) * 100
            print("1 - Following ", following)
            return int(following)
        elif "m Following" in page_source:
            following = page_source.split("Followers, ")[1].split("m Following,")[0]
            millions = following.split(".")[0]
            thousands = following.split(".")[1]
            following = int(millions) * 1000000 + int(thousands) * 100000
            print("2 - Following ", following)
            return int(following)
        else:
            following = page_source.split("Followers, ")[1].split(" Following,")[0]
            if len(following) == 5:
                following = following.split(",")
                following = int(following[0]) * 1000 + int(following[1])
                print("3 - Following ", following)
                return int(following)
            else:
                print("4 - Following ", following)
                return int(following)
    else:
        if "k</span> following</a>" in page_source:
            following = page_source.split('<span class="g47SY ">')[2].split("</span> following</a>")[0]
            thousands = following.split(".")[0]
            hundreds = following.split(".")[1]
            following = int(thousands) * 1000 + int(hundreds) * 100
            print("5 - Following ", following)
            return int(following)
        elif "m</span> following</a>" in page_source:
            following = page_source.split('<span class="g47SY ">')[2].split("</span> following</a>")[0]
            millions = following.split(".")[0]
            thousands = following.split(".")[1]
            following = int(millions) * 1000000 + int(thousands) * 100000
            print("6 - Following ", following)
            return int(following)
        else:
            following = page_source.split('<span class="g47SY ">')[2].split("</span> following</a>")[0]
            if len(following) == 5:
                following = following.split(",")
                following = int(following[0]) * 1000 + int(following[1])
                print("7 - Following ", following)
                return int(following)
            else:
                print("8 - Following ", following)
                return int(following)


def search_number_of_posts(page_source=None):
    print("\n\n Posts \n\n")
    direct_page = "</span> followers</a>" not in page_source
    if direct_page:
        if "k Posts" in page_source:
            posts = page_source.split("Following, ")[1].split("k Posts -")[0]
            thousands = posts.split(".")[0]
            hundreds = posts.split(".")[1]
            posts = int(thousands) * 1000 + int(hundreds) * 100
            print("1 - Posts ", posts)
            return int(posts)
        elif "m Posts" in page_source:
            posts = page_source.split("Following, ")[1].split("m Posts -")[0]
            millions = posts.split(".")[0]
            thousands = posts.split(".")[1]
            posts = int(millions) * 1000000 + int(thousands) * 100000
            print("2 - Posts ", posts)
            return int(posts)
        else:
            posts = page_source.split("Following, ")[1].split(" Posts -")[0]
            if len(posts) == 5:
                posts = posts.split(",")
                posts = int(posts[0]) * 1000 + int(posts[1])
                print("3 - Posts ", posts)
                return int(posts)
            else:
                print("4 - Posts ", posts)
                return int(posts)
    else:
        if "k</span> posts</span>" in page_source:
            posts = page_source.split('<span class="g47SY ">')[1].split("</span> posts</span>")[0]
            thousands = posts.split(".")[0]
            hundreds = posts.split(".")[1]
            posts = int(thousands) * 1000 + int(hundreds) * 100
            print("5 - Posts ", posts)
            return int(posts)
        elif "m</span> posts</span>" in page_source:
            posts = page_source.split('<span class="g47SY ">')[1].split("</span> posts</span>")[0]
            millions = posts.split(".")[0]
            thousands = posts.split(".")[1]
            posts = int(millions) * 1000000 + int(thousands) * 100000
            print("6 - Posts ", posts)
            return int(posts)
        else:
            posts = page_source.split('<span class="g47SY ">')[1].split("</span> posts</span>")[0]
            if len(posts) == 5:
                posts = posts.split(",")
                posts = int(posts[0]) * 1000 + int(posts[1])
                print("7 - Posts ", posts)
                return int(posts)
            else:
                print("8 - Posts ", posts)
                return int(posts)


def search_number_of_followers(page_source=None):
    print("\n\n Followers \n\n")
    direct_page = "</span> followers</a>" not in page_source
    if direct_page:
        print("direct_page")
        if "k Followers" in page_source:
            followers = page_source.split('<meta content="')[1].split("k Followers")[0]
            list_split = followers.split(".")
            thousands = list_split[0]
            print(list_split)
            if len(list_split) == 2:
                hundreds = list_split[1]
                followers = int(thousands) * 1000 + int(hundreds) * 100
                return int(followers)
            else:
                followers = int(thousands) * 1000
                print("1 - Followers ", followers)
                return int(followers)
        elif "m Followers" in page_source:
            followers = page_source.split('<meta content="')[1].split("m Followers")[0]

            millions = followers.split(".")[0]
            thousands = followers.split(".")[1]
            followers = int(millions) * 1000000 + int(thousands) * 100000
            print("2 - Followers ", followers)
            return int(followers)
        else:
            followers = page_source.split('<meta content="')[1].split(" Followers")[0]
            if len(followers) == 5:
                followers = followers.split(",")
                followers = int(followers[0]) * 1000 + int(followers[1])
                print("3 - Followers ", followers)
                return int(followers)
            else:
                print("4 - Followers ", followers)
                return int(followers)
    else:
        print("not direct page")
        if "k</span> followers</a>" in page_source:
            followers = page_source.split("k</span> followers</a>")[0].split('">')[-1]
            split_list = followers.split(".")
            thousands = split_list[0]
            print(split_list)
            if len(split_list) == 2:
                hundreds = split_list[1]
                followers = int(thousands) * 1000 + int(hundreds) * 100
            else:
                followers = int(thousands) * 1000
            print("5 - Followers ", followers)
            return int(followers)
        elif "m</span> followers</a>" in page_source:
            followers = page_source.split("m</span> followers</a>")[0].split('">')[-1]
            millions = followers.split(".")[0]
            thousands = followers.split(".")[1]
            followers = int(millions) * 1000000 + int(thousands) * 100000
            print("6 - Followers ", followers)
            return int(followers)
        else:
            followers = page_source.split("</span> followers</a>")[0].split('">')[-1]
            if len(followers) == 5:
                followers = followers.split(",")
                followers = int(followers[0]) * 1000 + int(followers[1])
                print("7 - Followers ", followers)
                return int(followers)
            else:
                print("8 - Followers ", followers)
                return int(followers)


def get_page_source(browser=None, username=None):
    link = "view-source:https://www.instagram.com/"

    browser.execute_script("window.open('');")

    sleep(random.randint(5, 10))

    browser.switch_to.window(browser.window_handles[1])

    sleep(random.randint(5, 10))

    browser.get(link + username + "/")

    sleep(random.randint(10, 20))

    page_source = browser.page_source

    sleep(random.randint(5, 10))

    browser.close()

    sleep(random.randint(5, 10))

    browser.switch_to.window(browser.window_handles[0])

    sleep(random.randint(5, 10))
    return browser, page_source
