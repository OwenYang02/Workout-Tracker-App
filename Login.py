# Login system
from User import User
import json
from constants import FILE_NAME
import hashlib
class Login: 
    def __init__(self):
        pass

    def create_account(self, username, email, password): 
        # ------------ create user object ----------------
        new_user = User(username, email)
        new_user.set_password(password)

        # -------- hash password with username ---------

        # load file
        try:
            with open(FILE_NAME, "r") as file:
                users = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            users = {}

        if username in users: 
            print("Username already exists, try a different username!")
            return None
        else: 
            # add new user to the users dictionary
            users[username] = new_user.password

            # write dictionary to the file
            with open(FILE_NAME, "w") as file:
                json.dump(users, file, indent=4)

            return new_user
    
    # check if usernames match and password hashes match
    def login(self, username, password):

        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
        # ----------------- load file ------------------- 
        try: 
            with open(FILE_NAME, "r") as file:
                users = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            users = {}

        # ----------------- login logic ------------------------

        # dictionary is empty, so no accounts have been created
        if not users:
            print("Account not found! Create a new account!")
        else:
            # username found and password hashes match
            if (username in users) and hashed_password == users[username]: 
                print("Login successful")
            else: 
                print("Username/password incorrect! Try again!")

        
                 
