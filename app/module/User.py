from ..utils.sqlUtil import LiteDb
from loguru import logger
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
        db.openDb('/Users/wangzepeng/Desktop/重要文件/格拉/code/Programming/&System/TeamProject/app/database.db')
        result = db.executeSql(f'select * from users where username = "{self.username}"')[1]
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



