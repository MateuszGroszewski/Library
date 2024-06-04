from src.inputToInt import convertInputToInt
from src.databases.userDB import UserDB


class Menu:

    @staticmethod
    def showMenu():
        print("Menu")
        print("1. Browse books")
        print("2. Rental history")
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
        