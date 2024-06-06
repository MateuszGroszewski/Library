from src.inputToInt import convertInputToInt
from src.authentication import Authentication
from src.databases.userDB import UserDB


class Menu:

    @staticmethod
    def start():
        print("1. Login")
        print("2. Register")
        print("0. Exit")
        choice = convertInputToInt(input("Enter your choice: "))

        match choice:
            case 1:
                print("Login")
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                loggedIn: bool = Authentication.login(username, password)
                if loggedIn:
                    Menu.showMenu()
            case 2:
                Authentication.register("Anna", "Smith", "anna.smith@email.com", "Anna98", "123")

    @staticmethod
    def showMenu():
        print("Menu")
        print("1. Browse books")
        print("2. Rental history")
        print("3. My account")
        print("0. Exit")
        choice = convertInputToInt(input("Enter your choice: "))

        match choice:
            case 1:
                name = input("Enter your name: ")
                lastName = input("Enter your last name: ")
                mail = input("Enter your mail: ")
                userName = input("Enter your user name: ")
                password = input("Enter your password: ")
                UserDB.addUser(name, lastName, mail, userName, password)
            case 2:
                name = input("Enter your name: ")
                UserDB.findUserLoginData(name)
