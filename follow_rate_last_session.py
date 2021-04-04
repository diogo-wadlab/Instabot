import search_in_profiles
import zhuzi_files


def maintained_users_last_session(followed_users_last_session=None, current_account_followers=None):
    if followed_users_last_session is None:
        raise ValueError('Function needs last session followed users to check')

    if current_account_followers is None:
        raise ValueError('Function needs list of current users to check')

    maintained_users = []
    for i in range(len(followed_users_last_session)):
        if followed_users_last_session[i] in current_account_followers:
            maintained_users.append(followed_users_last_session[i])
    return maintained_users


def follow_rate_last_session(username=None, session=None,
                             followed_users_last_session=search_in_profiles.read_users(zhuzi_files.followed_users_last_session)):
    if username is None:
        raise ValueError('Function needs username of account to check')

    if session is None:
        raise ValueError('Function needs open session to check')

    current_account_followers = session.grab_followers(username=username, amount="full", live_match=True, store_locally=True)

    maintained_users = maintained_users_last_session(followed_users_last_session, current_account_followers)
    total_number_of_followed_users = len(followed_users_last_session)
    total_number_of_maintained_users = len(maintained_users)

    print("followed_users_last_session", followed_users_last_session)
    follow_rate = total_number_of_maintained_users / total_number_of_followed_users * 100

    return maintained_users, follow_rate
