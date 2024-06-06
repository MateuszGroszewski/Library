import sqlite3


class UserDB:

    @staticmethod
    def createUserDB() -> None:
        userDBConnection = sqlite3.connect("userDB.db")
        userDBCursor = userDBConnection.cursor()
        userDBCursor.execute("""CREATE TABLE IF NOT EXISTS users (
        USERID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT,
        LASTNAME TEXT,
        MAIL TEXT,
        USERNAME TEXT,
        PASSWORD TEXT
        )
        """)

        userDBConnection.commit()
        userDBConnection.close()

    @staticmethod
    def addUser(name: str, lastname: str, mail: str, username: str, password: str) -> None:
        userDBConnection = sqlite3.connect("userDB.db")
        userDBCursor = userDBConnection.cursor()
        userDBCursor.execute(f"INSERT INTO users (NAME, LASTNAME, MAIL, USERNAME, PASSWORD) VALUES ('{name}', '{lastname}', '{mail}', '{username}', '{password}')")
        userDBConnection.commit()
        userDBConnection.close()

    @staticmethod
    def editUser(userID: int):
        raise NotImplemented

    @staticmethod
    def deleteUser(userID: int):
        raise NotImplemented

    @staticmethod
    def findUserLoginData(userName: str):
        userDBConnection = sqlite3.connect("userDB.db")
        userDBCursor = userDBConnection.cursor()
        userDBCursor.execute(f"SELECT USERNAME, PASSWORD FROM users WHERE USERNAME = '{userName}'")
        loginUserName, loginPassword = userDBCursor.fetchone()
        print(f'name: {loginUserName} pass: {loginPassword}')
        userDBConnection.commit()
        userDBConnection.close()


