import argparse
from datetime import datetime
from datetime import timedelta

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


block_duration_minutes = 5


def login_execution() -> bool:
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
            return True
        else:
            print("Attempts left", attempts - attempt)
    else:
        print("Attempts expired. You've been blocked for " + str(block_duration_minutes) + " minutes")
        return False


def if_not_blocked(last_wrong_attempt_time) -> bool:
    return last_wrong_attempt_time == None or datetime.now() >= (
                last_wrong_attempt_time + timedelta(minutes=block_duration_minutes))


def main():
    last_wrong_attempt_time = None

    while True:
        if if_not_blocked(last_wrong_attempt_time):
            if login_execution():
                break
            else:
                last_wrong_attempt_time = datetime.now()

    print("Verification successful")


if __name__ == "__main__":
    main()



