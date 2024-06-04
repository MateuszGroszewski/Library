import sqlite3


class Authentication:

    @staticmethod
    def startScreen():
        print("1. Login")
        print("2. Register")
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                print(Authentication.loginProcedure())
            case 2:
                Authentication.registerProcedure("Anna", "Smith", "anna.smith@email.com", "Anna98", "123")

    @staticmethod
    def loginProcedure() -> True | False:
        print("Login procedure")
        username = input("Enter your username: ").rstrip()
        password = input("Enter your password: ").rstrip()
        if username == password:
            return True
        else:
            return False

    @staticmethod
    def registerProcedure(name: str, lastName: str, email: str, username: str, password: str):
        newUser_name: str = name
        newUser_lastName: str = lastName
        newUser_email: str = email
        newUser_username: str = username
        newUser_password: str = password
        print(newUser_name, newUser_lastName, newUser_email, newUser_username, newUser_password)
