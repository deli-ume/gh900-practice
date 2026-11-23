"""練習用の電卓。subtract にわざとバグを入れています（演習2で直します）。"""


def add(a, b):
    return a + b


def subtract(a, b):
    # バグ：引き算なのに足し算になっている
    return a + b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


if __name__ == "__main__":
    print("10 - 3 =", subtract(10, 3))
