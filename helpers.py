def name_from_url(url=None):
    return url.replace("https://www.instagram.com/", "").replace("/", "")


def prepare_users(users={}, users_to_follow_followers={}):
    users_keys = list(users.keys())
    length_keys = {}
    sum_keys = 0
    key_control = 0
    new_users_to_follow_followers = []
    for key in users_keys:
        length = len(users_to_follow_followers[key])
        length_keys[key] = length
        sum_keys += length
    for i in range(sum_keys):
        key = users_keys[key_control]
        new_users_to_follow_followers.append({key: users_to_follow_followers[key][length_keys[key] - 1]})
        length_keys[key] = length_keys[key] - 1
        key_control += 1

        if length_keys[key] == 0:
            users_keys.remove(key)
            key_control = key_control - 1

        if key_control == len(users_keys):
            key_control = 0
    print(new_users_to_follow_followers)
    return new_users_to_follow_followers

def split_users_to_follow_followers(users_dict):
    dict_keys = users_dict.keys()
    dict_to_return_a = {}
    dict_to_return_b = {}
    for key in dict_keys:
        half = len(users_dict[key]) // 2
        dict_to_return_a[key] = users_dict[key][half:]
        dict_to_return_b[key] = users_dict[key][:half]
    return dict_to_return_a, dict_to_return_b