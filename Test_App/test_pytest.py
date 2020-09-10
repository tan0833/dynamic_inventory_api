# file_name: test_abc.py
# import pdb; pdb.set_trace()     #设置断点
import pytest # 引入pytest包

# @pytest.fixture(autouse=True,scope='function',params=[1,2,3]) # 设置为默认运行
# def before(request):
#     print("------->before")
#     return request.parmas

def return_test_data():
    return [(1,2),(0,3)]

class Test_ABC:
    # 测试类级开始
    def setup_class(self):
        print("------->setup_class")

    # 测试类级结束
    def teardown_class(self):
        print("------->teardown_class")

    def test_a(self):
        print("------->test_a")
        assert 1

    @pytest.mark.parametrize("a,b", return_test_data())  # 使用函数返回值的形式传入参数值
    # @pytest.mark.parametrize("a", [3, 6])   #参数化
    # @pytest.mark.xfail(2 > 1, reason="标注为预期失败")
    # @pytest.mark.skipif(2>1, reason="测试跳过函数")
    def test_b(self,a,b):
        print(a)


if __name__ == '__main__':
    # pytest.main(["-s", "test_pytest.py"]) # 调用pytest的main函数执行测试
    # pytest.main(['-x'])   # 第01次失败，就停止测试
    # pytest.main(["--maxfail","2"])   # 出现2个失败就终止测试
    # pytest.main(["test_pytest.py"])     #指定测试模块
    # pytest.main(["case/"])  # 指定测试目录  暂时没有找到正确方法
    # pytest.main(["-k","MyClass and not method"]) #通过关键字表达式过滤执行
    # pytest.main(["test_pytest.py::test_b"]) #由模块文件名、分隔符、类名、方法名、参数构成
    # pytest.main(["test_pytest.py::TestClass::test_method"])  # 运行模块中的指定方法
    # pytest.main(["-m","slow"])  # 执行被装饰器 @pytest.mark.slow 装饰的所有测试用例
    # pytest.main(["test_pytest.py", "-n","2"])  # pip install -U pytest-xdist  多线程运行
    # pytest.main(["test_pytest.py", "--reruns", "2"])  # 重试运行cases  pip install -U pytest-rerunfailures
    # pytest.main(["test_pytest.py", "-s","-n","4"])       #同时运行4个进程，又想打印出print的内容
    # pytest.main(["--html","./Test_Flow/report.html"])   #pip install pytest-html
    # pytest.main(["--showlocals"])       # 在回溯中显示局部变量
    # pytest.main(["--pdb"])  # 每次遇到失败都跳转到 PDB
    # pytest.main(["-x","--pdb"])  # 第一次遇到失败就跳转到 PDB，结束测试执行
    # pytest.main(["--pdb","--maxfail","3"])  # 只有前三次失败跳转到 PDB
    # pytest.main(["--durations", "3"])       #获取最慢的3个用例的执行耗时
    # pytest.main(["-p", "no:doctest"])           #关闭 doctest 插件
    pytest.main(["-qq"], plugins=[Test_ABC()])      #从Python代码中调用pytest