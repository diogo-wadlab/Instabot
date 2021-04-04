import random
import search_in_page_source
import helpers
import time


def unfollow_on_instagram(browser=None,
                          number_to_unfollow=1,
                          followed=[],
                          follow_back=[],
                          forbidden_unfollows=[]):
    time.sleep(random.randint(10, 15))

    profile_button = browser.find_element_by_css_selector(
        "span.qNELH > img:nth-child(1)")
    profile_button.click()

    time.sleep(random.randint(5, 10))

    got_to_profile_button = browser.find_element_by_css_selector(".La5L3")
    got_to_profile_button.click()

    time.sleep(random.randint(5, 10))
    '''print(browser.current_url)
    profile_page_source = browser.page_source
    profile_following = search_in_page_source.search_number_of_following(page_source=profile_page_source)
    profile_followers = search_in_page_source.search_number_of_followers(page_source=profile_page_source)
    time.sleep(random.randint(5, 10))'''
    profile_followers = 0
    followers_button = browser.find_element_by_css_selector(
        "li.Y8-fY:nth-child(3) > a:nth-child(1)")
    followers_button.click()

    print("unfollow_session - 1")

    time.sleep(random.randint(5, 10))
    last_ht, ht, j = 0, 1, 0

    scroll_box = browser.find_element_by_css_selector("div[class='isgrP']")

    time.sleep(random.randint(5, 10))

    print("unfollow_session - 2")

    limit = random.randint(10, 30)
    while ht != last_ht and j < limit:
        last_ht = ht
        time.sleep(random.randint(5, 10))
        ht = browser.execute_script(
            """
            arguments[0].scrollTo(0, arguments[0].scrollHeight); 
            return arguments[0].scrollHeight;
            """, scroll_box)
        j += 1

    print("unfollow_session - 3")

    if j < limit:
        limit_to_unfollow = 48
    else:
        limit_to_unfollow = 100
    usernames_seen = []
    i = 0

    while i <= number_to_unfollow:

        number_to_unfollow_now = random.randint(1, limit_to_unfollow)
        print("number_to_unfollow ", number_to_unfollow_now)

        if number_to_unfollow_now in usernames_seen:
            print("unfollow_session - 4")
            while number_to_unfollow_now in usernames_seen:
                number_to_unfollow_now = random.randint(1, 50)
                print("x_loop", number_to_unfollow_now)
            print("out_loop", number_to_unfollow_now)

        print("unfollow_session - 5 - ", number_to_unfollow_now)
        try:
            user_to_unfollow_button = browser.find_element_by_css_selector(
                "li.wo9IH:nth-child(" + str(number_to_unfollow_now) +
                ") > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > a:nth-child(1)"
            )
        except:
            try:
                user_to_unfollow_button = browser.find_element_by_css_selector(
                    "li.wo9IH:nth-child(" + str(2) +
                    ") > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > a:nth-child(1)"
                )
            except:
                user_to_unfollow_button = browser.find_element_by_css_selector(
                    "li.wo9IH:nth-child(" + str(10) +
                    ") > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > a:nth-child(1)"
                )

        print("unfollow_session - 6")

        user_to_unfollow_button.click()

        time.sleep(random.randint(5, 10))

        username_of_unfollow = helpers.name_from_url(url=browser.current_url)
        browser, page_source_follower = search_in_page_source.get_page_source(
            browser=browser, username=username_of_unfollow)
        #write_in_file(filename="C:\\Users\\dfbalmeida\\Documents\\NO_DELETE\\zhuzi_bot\\direct.txt", data_to_write=page_source_follower)
        #write_in_file(filename="C:\\Users\\dfbalmeida\\Documents\\NO_DELETE\\zhuzi_bot\\script.txt", data_to_write=browser.page_source)
        check_follow_back = search_in_page_source.search_if_follow_back(
            page_source=page_source_follower)
        print("Follow Back - ", check_follow_back)
        follower_followers = search_in_page_source.search_number_of_followers(
            page_source=browser.page_source)
        print("unfollow_session - 7")
        if (username_of_unfollow
                not in forbidden_unfollows) and (follower_followers < 10000):
            followed.append(username_of_unfollow)
            if check_follow_back:
                follow_back.append(username_of_unfollow)

            time.sleep(random.randint(5, 10))
            usernames_seen.append(number_to_unfollow_now)
            try:
                unfollow = browser.find_element_by_css_selector("._6VtSN")
                unfollow.click()

                time.sleep(random.randint(2, 10))
                print("aqui - 1")
                try:
                    print("aqui - 2")
                    unfollow_button = browser.find_element_by_css_selector(
                        "button.aOOlW:nth-child(1)")
                    unfollow_button.click()
                    time.sleep(random.randint(5, 10))

                except:
                    print("aqui - 3")
                    browser.back()
                    time.sleep(random.randint(5, 10))
            except:
                print("aqui - 4")
                time.sleep(random.randint(2, 10))

            browser.back()

            time.sleep(random.randint(5, 10))

            i += 1

            print("unfollow_session - 8")

        else:
            print("unfollow_session - 9")
            time.sleep(random.randint(5, 10))

            browser.back()

            time.sleep(random.randint(5, 10))

            followed.append(username_of_unfollow)

    close_followers_button = browser.find_element_by_css_selector(
        "div.WaOAr:nth-child(3) > button:nth-child(1)")
    close_followers_button.click()

    time.sleep(random.randint(5, 10))

    return browser, followed, follow_back, profile_followers


def search_on_instagram(browser=None,
                        username_to_search="",
                        number_of_users_to_follow=None):
    print("\n\n\n############################\n " + username_to_search +
          "\n############################\n\n\n")
    instagram_link = 'https://www.instagram.com/'
    browser.get(instagram_link + username_to_search)
    
    print("follow  - 1")
    time.sleep(random.randint(10, 20))
    try:
        login_form = browser.find_element_by_css_selector("a[class='-nal3 ']")
    # WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH,"//a[@href='/zhuzi.toothbrush/followers/']/span[@class='g47SY lOXF2'"))).click()
        login_form.click()
    except:
        browser.get(instagram_link + username_to_search + "/followers")
    time.sleep(random.randint(5, 10))

    print("follow  - 2")

    scroll_box = browser.find_element_by_css_selector("div[class='isgrP']")
    last_ht, ht, j = random.randint(1, 100), 1, 0
    # last_ht, ht, j = 10, 0, 0
    ht_control = 0
    used_numbers = []

    while (last_ht * 700) > ht and ht != ht_control:
        ht_control = ht
        time.sleep(random.randint(5, 10))
        print("follow  - 3")
        ht = browser.execute_script(
            """
            arguments[0].scrollTo(0, arguments[0].scrollHeight); 
            return arguments[0].scrollHeight;
            """, scroll_box)
        # time.sleep(random.randint(5, 10))
        # ht += 1
        j += 1
        print(last_ht * 700)
        print(ht)
        print(ht_control)
        print("\n")
        '''j += 1
        follow_button = browser.find_element_by_css_selector("button[class='sqdOP  L3NKy   y3zKF     ']")
        follow_button.click()
        if j == number_of_users_to_follow:
            account_sign_off_instagram(browser)
            return'''
    if last_ht * 700 > ht:
        last_ht = ht
    for i in range(number_of_users_to_follow):
        print("follow  - 4")
        x = random.randint(1, last_ht * 10)
        print("used_numbers", used_numbers)
        if x in used_numbers:
            while x in used_numbers:
                x = random.randint(1, last_ht * 10)
                print("x_loop", x)
            print("out_loop", x)
            used_numbers.append(x)
            follow_button = browser.find_element_by_css_selector(
                "li.wo9IH:nth-child(" + str(x) +
                ") > div:nth-child(1) > div:nth-child(2)")
            follow_button.click()
        else:
            print("follow  - 5")
            used_numbers.append(x)
            try:
                print("follow  - 6")
                follow_button = browser.find_element_by_css_selector(
                    "li.wo9IH:nth-child(" + str(x) +
                    ") > div:nth-child(1) > div:nth-child(2)")
                try:
                    print("follow  - 7")
                    follow_button.click()
                    print("else 1", x)
                except:
                    try:
                        print("follow  - 8")
                        time.sleep(random.randint(5, 20))
                        follow_button.click()
                        print("else 2", x)
                    except:
                        print("follow  - 9")
                        print("break 1")
                        break
            except:
                try:
                    print("follow  - 10")
                    time.sleep(random.randint(5, 20))
                    follow_button = browser.find_element_by_css_selector(
                        "li.wo9IH:nth-child(" + str(x) +
                        ") > div:nth-child(1) > div:nth-child(2)")

                    try:
                        print("follow  - 11")
                        follow_button.click()
                        print("else 3 ", x)
                    except:
                        print("follow  - 12")
                        try:
                            print("follow  - 13")
                            time.sleep(random.randint(5, 20))
                            follow_button.click()
                            print("else 4 ", x)
                        except:
                            print("follow  - 14")
                            print("break 2")
                            break
                except:
                    print("follow  - 15")
                    print("break 3")
                    break

        time.sleep(random.randint(5, 20))
    print("follow  - 16")
    time.sleep(random.randint(10, 20))
    try:
      close_followers_button = browser.find_element_by_css_selector(
          "div.WaOAr:nth-child(3) > button:nth-child(1)")
      close_followers_button.click()
      print("follow  - 17")
    except:
      print("follow  - 18")
      browser.get(instagram_link + username_to_search)
    print("follow  - 19")


def account_sign_off_instagram(browser=None):
    time.sleep(random.randint(5, 10))

    print("sign off - 1")
    profile_button = browser.find_element_by_css_selector(".qNELH")
    profile_button.click()

    time.sleep(random.randint(5, 10))
    sign_out_button = browser.find_element_by_css_selector(
        "div.-qQT3 > div:nth-child(1)")
    # f2ebbce7c159a06 > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)
    sign_out_button.click()

    print("sign off - 2")

    go_link = [
        "https://www.bloomberg.com/", "https://www.apple.com/",
        "https://www.google.com", "https://www.amazon.com",
        "https://www.youtube.com", "https://www.sapo.pt",
        "https://www.nike.com", "https://www.bmw.com",
        "https://www.covid19.min-saude.pt", "https://www.linkedin.pt"
    ]
    browser.get(go_link[random.randint(0, 9)])

    time.sleep(random.randint(5, 10))

    return browser


def account_login_instagram(browser=None, username="", password=""):
    # size = browser.get_window_size()
    # browser.set_window_size(size['width'] / 2, 695)

    instagram_link = 'https://www.instagram.com/'
    browser.get(instagram_link)
    print("log in - 1")
    try:
        cookies_accept = browser.find_element_by_xpath(
            "//button[text()='Accept']")
        cookies_accept.click()
    except:
        time.sleep(random.randint(1, 5))

    time.sleep(random.randint(5, 10))

    username_input = browser.find_element_by_css_selector(
        "input[name='username']")
    password_input = browser.find_element_by_css_selector(
        "input[name='password']")

    username_input.send_keys(username)
    password_input.send_keys(password)
    
    print("log in - 2")

    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()

    time.sleep(random.randint(10, 20))

    try:
        login_link = browser.find_element_by_xpath(
            "//button[text()='Save Info']")
        login_link.click()
        time.sleep(random.randint(5, 10))
    except:
        time.sleep(random.randint(1, 5))

    print("log in - 3")

    try:
        login_link = browser.find_element_by_xpath(
            "//button[text()='Not Now']")
        login_link.click()
        time.sleep(random.randint(5, 10))
    except:
        browser.get(instagram_link + username)

    print("log in - 4")

    return browser
