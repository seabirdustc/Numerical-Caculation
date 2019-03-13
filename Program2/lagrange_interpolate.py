import matplotlib.pyplot as plt
import numpy as np
import math


def f(x):
    return 1 / (4 + x + x ** 2)


def xset1(n):
    xlist1 = []
    for i in range(n + 1):
        xlist1.append(-5 + 10 / n * i)
    return xlist1


def xset2(n):
    xlist2 = []
    for i in range(n + 1):
        xlist2.append(-5 * math.cos((2 * i + 1) / (2 * n + 2) * math.pi))
    return xlist2


def interpolate(x, xlist):
    llist = []
    n = len(xlist)
    result = 0
    for i in range(n):
        l_i = 1
        xi = xlist[i]
        for j in range(n):
            xj = xlist[j]
            if i == j:
                continue
            else:
                l_i = l_i * (x - xj) / (xi - xj)
        llist.append(l_i)
    for i in range(n):
        result = result + llist[i] * f(xlist[i])
    return result


def deviation():
    print("第一组节点，误差为")
    for j in range(2, 5):
        print("n=%d , " % 2 ** j, end='')
        xlist = xset1(2 ** j)
        Max = 0
        for i in range(501):
            yi = i / 50 - 5
            di = math.fabs(f(yi) - interpolate(yi, xlist))
            Max = max(Max, di)
        print("%.12e\n" % Max)

    print("第二组节点，误差为")
    for j in range(2, 5):
        print("n=%d , " % 2 ** j, end='')
        xlist = xset2(2 ** j)
        Max = 0
        for i in range(501):
            yi = i / 50 - 5
            di = math.fabs(f(yi) - interpolate(yi, xlist))
            Max = max(Max, di)
        print("%.12e\n" % Max)


def SelPltPos(xlist):
    x = np.linspace(-5, 5, 1000)
    if len(xlist) == 5:
        plt.subplot(311)
    elif len(xlist) == 9:
        plt.subplot(312)
    else:
        plt.subplot(313)
    return x


def plot_lagrange():
    x = np.linspace(-5, 5, 1000)
    plt.subplot(311)
    plt.plot(x, f(x), color='gold')
    plt.subplot(312)
    plt.plot(x, f(x), color='gold')
    plt.subplot(313)
    plt.plot(x, f(x), color='gold')


def p1_plot(xlist):
    x = SelPltPos(xlist)
    plt.plot(x, interpolate(x, xlist), color='green', linestyle='--')


def p2_plot(xlist):
    x = SelPltPos(xlist)
    plt.plot(x, interpolate(x, xlist), color='blue', linestyle='-.')


def main():
    p1_plot(xset1(4))
    p1_plot(xset1(8))
    p1_plot(xset1(16))
    p2_plot(xset2(4))
    p2_plot(xset2(8))
    p2_plot(xset2(16))
    plot_lagrange()
    deviation()
    plt.show()


if __name__ == '__main__':
    main()
