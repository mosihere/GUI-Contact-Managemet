def register_dal(contact):
    try:
        file_object = open("contact.txt", mode="at")
        file_object.write(f"{contact}\n")
    except BaseException as err:
        return ("ERROR", err)
    else:
        return ("SUCCESS", "")
    finally:
        file_object.close()



def check_duplicate(new_username, new_national_code):

    err_list = list()

    try:
        file_object = open("contact.txt", mode="rt")
        for item in file_object:
            contact = item.strip().split(",")
            # first_name = contact[0]
            # last_name = contact[1]
            user_name = contact[2]
            # password = contact[3]
            national_code = contact[4]

            if new_username == user_name:
                err_list.append("Username Error!!!")

            if new_national_code == national_code:
                err_list.append("NationalCode Error!!!")

    except BaseException as err:
        return ("ERROR", err)
    else:
        if err_list:
            return ("ERROR", err_list)
        else:
            return ("SUCCESS", "")
    finally:
        file_object.close()


def check_exists(check_username, check_password):

    err_list = list()

    try:
        file_object = open("contact.txt", mode="rt")
        for item in file_object:
            contact = item.strip().split(",")
            first_name = contact[0]
            last_name = contact[1]
            user_name = contact[2]
            password = contact[3]
            email = contact[4]

            if check_username == user_name and check_password==password:
                return ("SUCCESS", "")

    except BaseException as err:
        return ("ERROR", err)
    else:
        return ("ERROR", "Username doesnt exist")
    finally:
        file_object.close()