
#模块级别
def setup_module():
    print("资源准备：setup_module")

def teardown_module():
    print("资源准备：teardown_module")

def test_case1():
    print("case1")

def setup_function():
    print("资源准备：setup_function")

def teardown_function():
    print("资源销毁：teardown_function")

class TestDemo:

        #执行类 前后分别执行 setup_class  teardown_class
    def setup_class(self):
        print("TestDemo setup_calss")

    def teardown_class(self):
        print("TestDemo teardown_class")

       #每个方法的前和后分别执行 setup  teardown
    def setup(self):
        print("TestDemo setup")

    def teardown(self):
        print("TestDemo teardown")


    def test_demo1(self):
        print("test demo1")

    def test_demo2(self):
        print("test demo2")