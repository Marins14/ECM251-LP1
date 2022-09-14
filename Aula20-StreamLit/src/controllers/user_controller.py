from models.user import User

class UserController():
    def __init__(self) -> None:
        #Carrega os dados dos usuarios
        self.users = [
            User(name="Kratos", password="GAROTO", email="reidelas@gmail.com"),
            User(name="Garoto", password="paizao", email="reidelas123@gmail.com"),
            User(name="Gervasio", password="souestranho", email="reidasnovinha@gmail.com")
            ]
        def checkUser(self,user):
            return user in self.users
        
        def checkLogin(self,name,password):
            user_test = User(name = name,password = password,email = None)
            for user in self.users:
                if user.name == user_test.name and user.password == user_test.password:
                 return True
            return False
           
            