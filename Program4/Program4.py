# Newton迭代和弦截法求根的通用程序
import numpy as np

E = 1e-10


def f(x):
    return 2*x**4+24*x**3+61*x**2-16*x+1


def f1(x):
    return 8*x**3+72*x**2+122*x-16


def Newton_Iteration(x_0):
    x_k = x_0
    k = 0
    while(1):
        print("|  k=%d  |  %.10e  |  %.10e  |" % (k, x_k, f(x_k)))
        if np.fabs(f(x_k)) < E:
            break
        k = k + 1
        x_k = x_k - f(x_k)/f1(x_k)


def Secant_Method(x_0, x_1):
    x_k = x_1
    x_km1 = x_0
    k = 0
    print("|  k=%d  |  %.10e  |  %.10e  |" % (k, x_0, f(x_0)))
    while(1):
        k = k+1
        print("|  k=%d  |  %.10e  |  %.10e  |" % (k, x_k, f(x_k)))
        if np.fabs(f(x_k)) < E:
            break
        d = (x_k-x_km1)/(f(x_k)-f(x_km1))
        x_kp1 = x_k - f(x_k)*d
        x_km1 = x_k
        x_k = x_kp1


if __name__ == "__main__":
    print("Newton迭代：x0=0")
    Newton_Iteration(0)
    print("Newton迭代：x0=1")
    Newton_Iteration(1)
    print("弦截法求根：x0=0, x1=0.1")
    Secant_Method(0, 0.1)
    print("弦截法求根：x0=0.5, x1=1.0")
    Secant_Method(0.5, 1.0)
