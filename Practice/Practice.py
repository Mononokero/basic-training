
l = login_values = {
    "first_player": "password1",
    "user_ololo": "password2"
}

def check_password(username: str, password) -> bool:
    if username in l and l[username] == password:
        return True
    else:
        return False

def login(func):
    def inner(username, password):
        if check_password(username, password):
            return func(username, password)
        else:
            return False

    return inner


@login
def decor_login(username: str, password: str) -> bool:
    return True

attempts = 3
attempt = 0

while attempt < attempts:
    attempt += 1
    username = input("Input username: \n>> ")
    password = input("Input password: \n>> ")

    if decor_login(username, password):
        print("Logged in")
        break
    else:
        print("Attempts left", attempts - attempt)
else:
    print("Attempts expired")

