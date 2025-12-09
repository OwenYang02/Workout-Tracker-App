# Login system
from User import User
import json
class Login: 
    def __init__(self):
        pass

    def create_account(username, email, password): 
        # ------------ create user object ----------------
        new_user = User(username, email)
        new_user.set_password(password)

        # -------- hash password with username ---------

        filename = "passwords.json"

        # load file
        try:
            with open(filename, "r") as file:
                users = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            users = {}

        # add new user to the users dictionary
        users[username] = new_user.password

        # write dictionary to the file
        with open(filename, "w") as file:
            json.dump(users, file, indent=4)

        return new_user
    
    # check if usernames match and password hashes match
    def login(user):
        pass



