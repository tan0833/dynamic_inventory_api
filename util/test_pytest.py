# file_name: test_abc.py
import pytest # 引入pytest包


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

    def test_b(self):
        print("------->test_b")


if __name__ == '__main__':
    pytest.main(["-s", "test_pytest.py"]) # 调用pytest的main函数执行测试
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