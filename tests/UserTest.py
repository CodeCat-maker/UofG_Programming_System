import unittest
from app.module.User import User  # 替换为你的模块路径

class TestUserLogin(unittest.TestCase):

    def setUp(self):
        # 在每个测试方法执行之前运行
        self.user = User("testName", "test123")

    def tearDown(self):
        # 在每个测试方法执行之后运行
        pass

    def test_login_success(self):
        # 测试登录成功的情况
        result = self.user.login()
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
