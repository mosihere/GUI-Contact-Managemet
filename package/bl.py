from .dal import *


def register_bl(firstname, username, national_code, lastname, password, confirm_password):
    
    err_list = list()

    if not firstname.strip():
        err_list.append("firstname error")

    if not lastname.strip():
        err_list.append("lastname error")\

    if not username.strip():
        err_list.append("UserName error")

    if not national_code.strip():
        err_list.append("NationalCode error")

    if not password.strip():
        err_list.append("password error")

    if not confirm_password.strip():
        err_list.append("confirm password error")

    if password != confirm_password:
        err_list.append("password error")

    if err_list:
        return ("ERROR", "\n".join(err_list))



    res = check_duplicate(
        new_username=username,
        new_national_code=national_code
    )

    if res[0]=="ERROR":
        return ("ERROR", "\n".join(res[1]))


    contact = f"{firstname},{lastname},{username},{password},{national_code}"

    res = register_dal(contact)

    if res[0]=="ERROR":
        return ("ERROR", "Database Error!!!")

    if res[0]=="SUCCESS":
        return ("SUCCESS", "Success message")
    

def login_bl(username, password):
    
    err_list = list()

    if not username.strip():
        err_list.append("username error")

    if not password.strip():
        err_list.append("password error")

    if err_list:
        return ("ERROR", "\n".join(err_list))


    # To do

    res = check_exists(
        check_username=username,
        check_password=password
    )

    if res[0]=="ERROR":
        return ("ERROR", res[1])

    if res[0]=="SUCCESS":
        return ("SUCCESS", "Success message")