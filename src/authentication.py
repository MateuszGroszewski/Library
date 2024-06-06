from src.inputToInt import convertInputToInt
import sqlite3


class Authentication:

    @staticmethod
    def login(userName: str, password: str) -> bool:
        loginSucceed: bool = False
        userDBConnection = sqlite3.connect("userDB.db")
        userDBCursor = userDBConnection.cursor()
        userDBCursor.execute(f"SELECT USERNAME, PASSWORD FROM users WHERE USERNAME = '{userName}'")
        loginUserName, loginPassword = userDBCursor.fetchone()
        if userName == loginUserName and password == loginPassword:
            loginSucceed = True
        else:
            loginSucceed = False
        userDBConnection.commit()
        userDBConnection.close()
        return loginSucceed

    @staticmethod
    def register(name: str, lastName: str, email: str, username: str, password: str):
        newUser_name: str = name
        newUser_lastName: str = lastName
        newUser_email: str = email
        newUser_username: str = username
        newUser_password: str = password
        print(newUser_name, newUser_lastName, newUser_email, newUser_username, newUser_password)
