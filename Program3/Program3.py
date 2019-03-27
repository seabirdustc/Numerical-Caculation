# 复化积分
import numpy as np


def f(x):
    return np.sin(x)


def compound_simpson(a, b, n):
    tmp1 = 0
    tmp2 = 0
    for i in range(1, n, 2):
        tmp1 += 4 * f(a + i * (b - a) / n)
    for i in range(2, n - 1, 2):
        tmp2 += 2 * f(a + i * (b - a) / n)
    result = (b - a) / (3 * n) * (f(a) + tmp1 + tmp2 + f(b))
    return result


def compound_trapezoid(a, b, n):
    tmp = 0
    for i in range(1, n):
        tmp = tmp + f(a + i * (b - a) / n)
    result = (b - a) / n * (1 / 2 * f(a) + tmp + 1 / 2 * f(b))
    return result


def main():
    I = -np.cos(6) + np.cos(1)  # 精准值
    # print("I:", I)
    print("复化梯形积分 误差和误差阶为")
    for k in range(0, 13):
        print("k={} ,".format(k), end=' ')
        N = 2 ** k
        T = compound_trapezoid(1, 6, N)
        print("e%d=" % k, end='')
        print("%.12e" % (I - T), end=' ')
        if k == 0:
            e = np.fabs(I - T)
            print('')
        if k != 0:
            print("d%d=" % k, end='')
            print("%.4f" % (-(np.log(np.fabs((I - T)) / e) / np.log(N))))
    print("复化Simpson积分 误差和误差阶为")
    for k in range(0, 13):
        print("k={} ,".format(k), end=' ')
        N = 2 ** k
        T = compound_simpson(1, 6, N)
        print("e%d=" % k, end='')
        print("%.12e" % (I - T), end=' ')
        if k == 0:
            e = np.fabs(I - T)
            print('')
        if k != 0:
            print("d%d=" % k, end='')
            print("%.4f" % (-(np.log(np.fabs((I - T)) / e) / np.log(N))))


if __name__ == "__main__":
    main()
