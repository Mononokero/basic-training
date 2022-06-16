import argparse

l = login_values = {
    "player": "password1",
    "ololo": "password2"
}

def check_password(username: str, password) -> bool:
    return l.get(username) == password


def decor_login(func):
    def inner(username, password):
        if check_password(username, password):
            return func(username, password)
        else:
            return False

    return inner


@decor_login
def login(username: str, password: str) -> bool:
    return True

def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", help="valid username")
    parser.add_argument("-p", "--password", help="valid password")
    return parser.parse_args()
args = parser()

attempts = 3
attempt = 0

while attempt < attempts:
    attempt += 1

    username = ""
    password = ""

    if attempt == 1:
        if args.username is not None:
            username = args.username
        else:
            username = input("Input username: \n>> ")
        if args.password is not None:
            password = args.password
        else:
            password = input("Input password: \n>> ")
    else:
        username = input("Input username: \n>> ")
        password = input("Input password: \n>> ")

    if login(username, password):
        print("Logged in")
        break
    else:
        print("Attempts left", attempts - attempt)
else:
    print("Attempts expired")



