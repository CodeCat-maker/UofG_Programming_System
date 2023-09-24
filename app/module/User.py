class User:
    username: str = ""
    password: str = ""
    email:str =""
    phone_number:int = ""
    status:bool = False
    role: str = ""

    def login(self)->bool:
        return True
    def logout(self)->bool:
        return True
    def register(self,username,password,email,phone_number,status,role)->bool:
        return True



