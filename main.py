from src.authentication import Authentication
from src.databases.userDB import UserDB
from src.menu import Menu

if __name__ == '__main__':
    UserDB.createUserDB()
    Menu.showMenu()
    #Authentication.startScreen()
