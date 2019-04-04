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
    print("复化梯形积分 误差和误差阶为")
    elist1 = []
    for k in range(0, 13):
        # print("k={} ,".format(k), end=' ')
        print("|%d" % k, end='')
        N = 2 ** k
        T = compound_trapezoid(1, 6, N)
        # print("e%d=" % k, end='')
        # print("%.12e" % (I - T), end=' ')
        print("|%.12e|" % (I - T), end=' ')
        elist1.append(I - T)
        if k == 0:
            print('')
        if k != 0:
            # print("d%d=" % k, end='')
            # print("%.12e" % (-(np.log(np.fabs(elist1[k] / elist1[k - 1])) / np.log(2))))
            print("%.12e|" % (-(np.log(np.fabs(elist1[k ] / elist1[k - 1])) / np.log(2))))
    print("复化Simpson积分 误差和误差阶为")
    elist2 = []
    for k in range(1, 13):
        # print("k={} ,".format(k), end=' ')
        print("|%d" % k, end='')
        N = 2 ** k
        T = compound_simpson(1, 6, N)
        # print("e%d=" % k, end='')
        # print("%.12e" % (I - T), end=' ')
        print("|%.12e|" % (I - T), end=' ')
        elist2.append(I - T)
        if k == 1:
            print('')
        if k != 1:
            # print("d%d=" % k, end='')
            # print("%.12e" % (-(np.log(np.fabs(elist2[k-1] / elist2[k - 2])) / np.log(2))))
            print("%.12e|" % (-(np.log(np.fabs(elist2[k - 1] / elist2[k - 2])) / np.log(2))))


if __name__ == "__main__":
    main()
