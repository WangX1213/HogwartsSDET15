import pytest
import yaml

from pythoncode.calculator import Calculator

#解析测试数据文件
def get_datas():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)

    add_datas = datas['add']['datas']
    add_ids = datas['add']['ids']
    print(add_datas)
    print(add_ids)
    return (add_datas,add_ids)

#解析测试步骤文件
def steps(addstepsfile,calc,a,b,expect):
    with open(addstepsfile) as f:
        steps = yaml.safe_load(f)

    for step in steps:
        if 'add' == step:
            print("step: add")
            result = calc.add(a,b)
        elif 'add1' == step:
            print("step: add1")
            result = calc.add1(a,b)
        assert  expect == result

class TestCalc:

    def setup_class(self):
        print("计算开始")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    # @pytest.mark.parametrize('a,b,expect',[
    #     [1,1,2],[100,100,200],[0.1,0.1,0.2],[-1,-1,-2],
    #     [1,0,1]
    # ],ids=['int_case','bignum_case','float_case','minus_case','zero_case'])
    @pytest.mark.parametrize('a,b,expect',get_datas()[0]
                             ,ids=get_datas()[1])
    def test_add(self,a,b,expect):
        #calc = Calculator() #实例化被测类
        result = self.calc.add(a,b) #调用方法
        assert result == expect #断言
    #
    # def test_add1(self):
    #     test_data = [[1,1,2],[100,100,200],[0.1,0.1,0.2],[-1,-1,-2],
    #     [1,0,1]]
    #     for i in range(1,len(test_data)):
    #         #calc = Calculator() #实例化被测类
    #         result = self.calc.add(test_data[i][0],test_data[i][1]) #调用方法
    #         assert result == test_data[i][2] #断言
        #
    # def test_add2(self):
    #     #calc = Calculator()  # 实例化被测类
    #     result = self.calc.add(0.1, 0.1)  # 调用方法
    #     assert result == 0.2  # 断言

    @pytest.mark.parametrize('a,b,expect',[
        [2,3,-1],[0.3,0.2,0.1],[3,2,1]],
        ids=['minus_case','float_case','int_case'])
    def test_sub(self,a,b,expect):
        result = self.calc.sub(a,b)
        assert result == expect
    #
    @pytest.mark.parametrize('a,b,expect',[
        [2,3,6],[0.2,0.3,0.06],[-2,-1,2],[-2,1,-2],[0,-2,0]],
        ids=['int_case','float_case','minus_minus_case','minus_positive_case','zero_case'])
    def test_mul(self,a,b,expect):
        result = self.calc.mul(a,b)
        assert result == expect
    #
    @pytest.mark.parametrize('a,b,expect',[
        [0.1,0],[10, 0]
    ])
    def test_div_zero(self,a,b,expect):
        with pytest.raises(ZeroDivisionError):
            self.calc.div(a,b)
    #
    # def test_add_steps(self):
    #     a = 1
    #     b = 2
    #
    #     steps("./steps/add_steps",)
        # assert 2 == self.calc.add(1,1)
        # assert 3 == self.calc.add1(1,2)
        # assert 0 == self.calc.add1(-1,1)