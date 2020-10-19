import pytest

@pytest.fixture(autouse=True,scope="module")
def login():
    #setup 操作
    print("登录操作")
    #yield 相当于 return
    yield ['tom','123456']
    #teardown操作
    print("登出操作")

@pytest.fixture(scope='session',autouse=True)
def conn_db():
    print("完成 ，数据库连接")
    yield "database"
    print("关闭 数据库连接")