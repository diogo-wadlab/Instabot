from datetime import date, datetime
import zhuzi_files
import os


def array_to_string(array_to_convert=None):
    if array_to_convert is None:
        raise ValueError('Function needs array to convert')
    converted_string = ''
    for i in range(len(array_to_convert)):
        if i != len(array_to_convert) - 1:
            converted_string += str(array_to_convert[i]) + ","
        else:
            converted_string += str(array_to_convert[i])
    return converted_string


def string_to_array(string_to_convert=None, characters_to_remove=None, string_separator=","):
    if string_to_convert is None:
        raise ValueError('Function needs string to convert')
    converted_array = string_to_convert.split(string_separator)
    if characters_to_remove:
        for i in range(len(characters_to_remove)):
            converted_array.remove(characters_to_remove[i])
    return converted_array


def read_users(filename=None, file_as_date=False):
    if filename is None:
        raise ValueError('Function needs filename to write')

    f = open(filename, "r")
    read_users = [line.rstrip('\n') for line in f]
    f.close()

    return read_users


def write_users(filename=None, users_to_write=None):
    if filename is None:
        raise ValueError('Function needs filename to write')

    if users_to_write is None:
        raise ValueError('Function needs user list to write')

    with open(filename, "w") as file_handle:
        for list_item in users_to_write:
            file_handle.write('%s\n' % list_item)
        file_handle.close()


def append_users(filename=None, users_to_append=None):
    if filename is None:
        raise ValueError('Function needs filename to write')

    if users_to_append is None:
        raise ValueError('Function needs user list to append')

    with open(filename, "a") as file_handle:
        for list_item in users_to_append:
            file_handle.write('%s\n' % list_item)
        file_handle.close()


def read_from_file(filename=None):
    if filename is None:
        raise ValueError('Function needs filename to write')

    with open(filename, "r") as file_handle:
        data_from_file = file_handle.read()
        file_handle.close()

    return data_from_file


def write_in_file(filename=None, data_to_write=None):
    if filename is None:
        raise ValueError('Function needs filename to write')

    if data_to_write is None:
        raise ValueError('Function needs data to write')

    with open(filename, "w") as file_handle:
        try:
            file_handle.write('%s' % data_to_write)
        except:
            file_handle.write(data_to_write)
        file_handle.close()


def append_in_file(filename=None, data_to_append=None):
    if filename is None:
        raise ValueError('Function needs filename to write')

    if data_to_append is None:
        raise ValueError('Function needs data to write')

    with open(filename, "a") as file_handle:
        file_handle.write('%s' % data_to_append)
        file_handle.close()


def read_follow_session_log(function_used=None, datetime_to_read=None):
    if function_used is None:
        raise ValueError('Function needs filename to write')

    if datetime_to_read is None:
        raise ValueError('Function needs data to write')

    filename = zhuzi_files.followed_users_log_folder + function_used + "_" + datetime_to_read + ".txt"
    data_from_file = read_from_file(filename)
    data_from_file = data_from_file.split("#")

    function_used = data_from_file[1].split(",")[0]
    users_used_to_follow_followers = string_to_array(string_to_convert=data_from_file[2],
                                                     characters_to_remove=['\n', '$', '#'])
    users_followed = string_to_array(string_to_convert=data_from_file[3], characters_to_remove=['@', '#', '\n'])

    return function_used, users_used_to_follow_followers, users_followed


def read_already_used_users():
    # tem que ser melhorado
    already_used_users = read_users(filename=zhuzi_files.already_used_users)
    return already_used_users


def write_already_used_users(already_user_users=None):
    if already_user_users is None:
        raise ValueError('Function needs already used users to write')

    users_to_append = ["#@#" + date.today().strftime("%d_%m_%Y")] + already_user_users
    append_users(filename=zhuzi_files.already_used_users, users_to_append=users_to_append)


def write_wad_bot_log(data_to_write=None, session_notes=""):
    if data_to_write is None:
        raise ValueError('Function needs data to write')

    current_date = date.today().strftime("%d_%m_%Y")
    filename = zhuzi_files.wad_bot_log_folder + "wad_bot_log_" + current_date + ".txt"
    if not os.path.isfile(filename):
        data_to_write = "#@#@#@,\n" + session_notes + "\n" + data_to_write
        write_in_file(filename, data_to_write)
    else:
        data_to_write = "\n#@#@#@,\n" + data_to_write
        append_in_file(filename, data_to_write)

    write_in_file(zhuzi_files.zhuzi_log_file, data_to_write)


def data_to_write_followed_users(function_used=None, users_used_to_follow_followers=None, users_followed=None):
    data_to_write = '#' + function_used + ',\n#$#,' + array_to_string(
        users_used_to_follow_followers) + ',\n#@#,' + array_to_string(users_followed) + ",\n"
    return data_to_write


def write_followed_users_log(function_used=None, users_used_to_follow_followers=None, users_followed=None,
                             session_notes=None):
    if function_used is None:
        raise ValueError('Function needs function used to write in log')
    if users_used_to_follow_followers is None:
        raise ValueError('Function needs users_used_to_follow_followers')
    if users_followed is None:
        raise ValueError('Function needs users_followed')

    current_date = date.today().strftime("%d_%m_%Y")
    filename = zhuzi_files.followed_users_log_folder + function_used + "_" + current_date + ".txt"
    data_to_write = data_to_write_followed_users(function_used=function_used,
                                                 users_used_to_follow_followers=users_used_to_follow_followers,
                                                 users_followed=users_followed)
    write_in_file(filename, data_to_write)
    write_wad_bot_log(data_to_write=data_to_write, session_notes=session_notes)


def data_to_write_unfollowed_users(function_used=None, users_unfollowed=None):
    data_to_write = '#' + function_used + ',\n#@#,' + array_to_string(users_unfollowed) + ",\n"
    return data_to_write


def write_unfollowed_users_log(function_used=None, users_unfollowed=None, session_notes=None):
    if function_used is None:
        raise ValueError('Function needs function used to write in log')
    if users_unfollowed is None:
        raise ValueError('Function needs users_unfollowed')

    data_to_write = data_to_write_unfollowed_users(function_used=function_used, users_unfollowed=users_unfollowed)
    write_wad_bot_log(data_to_write=data_to_write, session_notes=session_notes)


def data_to_write_maintained_users(function_used=None, follow_rate=None, maintained_users=None):
    if not maintained_users:
        data_to_write = '#' + function_used + ',\n#$#,' + str(follow_rate) + ',\n#@#,' + "no maintained users" + ",\n"
    else:
        data_to_write = '#' + function_used + ',\n#$#,' + str(follow_rate) + ',\n#@#,' + array_to_string(maintained_users) + ",\n"
    return data_to_write


def write_maintained_users_log(function_used=None, follow_session_day=None, maintained_users=None, follow_rate=None):
    if function_used is None:
        raise ValueError('Function needs function used to write in log')
    if maintained_users is None:
        raise ValueError('Function needs users_used_to_follow_followers')
    if follow_session_day is None:
        raise ValueError('Function needs follow_session_day')
        # format = dd_mm_yyyy
    if datetime.strptime(follow_session_day, '%d_%m_%Y') is ValueError:
        raise ValueError("Incorrect data format, should be dd_mm_yyyy")
    if follow_rate is None:
        raise ValueError('Function needs follow_rate')

    filename = zhuzi_files.maintained_users_log_folder + function_used + "_" + str(follow_session_day) + ".txt"
    data_to_write = data_to_write_maintained_users(function_used=function_used, follow_rate=follow_rate,
                                                   maintained_users=maintained_users)
    write_in_file(filename, data_to_write)
