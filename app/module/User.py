from ..utils.sqlUtil import LiteDb
from loguru import logger
import os
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
dbName = os.path.join(PROJECT_ROOT,"../database.db")

class User:
    username: str = ""
    password: str = ""
    email:str =""
    phone_number:int = ""
    status:bool = False
    role: str = ""
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def login(self)->bool:
        db=LiteDb()
        print(dbName)
        db.openDb(dbName)
        result = db.executeSql(f'select * from Users where username = "{self.username}"')[1]
        if result:
            logger.debug(result)
            tmpPassWord = result[0][2]
            if tmpPassWord == self.password:
                return True
            else:
                return False
        return False
    def logout(self)->bool:
        return True
    def register(self,username,password,email,phone_number,status,role)->bool:
        return True



