__all__ = ['test_A']


def test_A(a, b):
    print(a + b)


def test_B(a, b):
    print(a - b)


# 功能测试---内置变量 __name__
if __name__ == '__main__':  # 这里的__main__是对应于my_module.py
    test_A(1, 2)
