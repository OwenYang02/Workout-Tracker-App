from Login import Login

def main():

    login_system = Login()

    login = input("Would you like to login? Press y if yes, press any other key if not: ")
    if login.lower() == "y":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        login_system.login(username, password)
    else: 
        username = input("Enter a username: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")


        login_system.create_account(username, email, password)

if __name__ == "__main__":
    main()