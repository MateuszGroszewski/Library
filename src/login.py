class Login:

    @staticmethod
    def startScreen():
        print("1. Login")
        print("2. Register")
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                print(Login.loginProcedure())
            case 2:
                Login.registerProcedure()

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
        raise NotImplemented
