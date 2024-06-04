from inputToInt import convertInputToInt


class Menu:

    @staticmethod
    def showMenu():
        print("Menu")
        print("1. Browse books")
        print("2. Rental history")
        print("0. Exit")
        choice = convertInputToInt(input("Enter your choice: "))
        