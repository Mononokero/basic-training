import json
import argparse
from datetime import datetime
from datetime import timedelta

# l = login_values = {
#     "ololo1": "pass1",
#     "ololo2": "pass2"
# }

filename = "l.json"
# s = json.dumps(l)
# with open(filename, "w", encoding="utf-8") as file:
#     file.write(s)

with open("l.json", "r") as login_file:
    try:
        accounts = json.load(login_file)
    except:
        accounts = {}
print(accounts)

def create_user():
    global accounts
    create_login = input("Create login name: ")
    if create_login in accounts:
        print("Login name already exist!")
    else:
        create_password = input("Create password: ")
        accounts[create_login] = create_password
        print("New User created! Please log-in.")
        save_data()
#create_user()

def save_data():
    new_data = accounts
    with open("l.json", encoding="utf-8") as file:
        data = json.load(file)
        data.update(new_data)
        with open(filename, "w", encoding="utf-8") as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=2)


class UserDoesNotExist(Exception):
    pass

def check_password(username: str, password) -> bool:
    with open("l.json") as dataf:
        data = json.load(dataf)
        result = data.get(username) == password
        if result:
            return True
        else:
            raise UserDoesNotExist("User not found")


def decor_login(func):
    def inner(username, password):
        try:
            if check_password(username, password):
                return func(username, password)
        except UserDoesNotExist as e:
            print("Error", e)
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


block_duration_minutes = 1


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
        #print("Attempts expired")
        #print("Attempts expired. You've been blocked for " + str(block_duration_minutes) + " minutes")
        return False





def if_not_blocked(last_wrong_attempt_time) -> bool:
    return last_wrong_attempt_time == None or datetime.now() >= (last_wrong_attempt_time + timedelta(minutes=block_duration_minutes))


def main():
    last_wrong_attempt_time = None

    while True:
        if if_not_blocked(last_wrong_attempt_time):
            if login_execution():
                break
            else:
                #last_wrong_attempt_time = datetime.now()
                create_user()

    print("Verification successful")


if __name__ == "__main__":
    main()