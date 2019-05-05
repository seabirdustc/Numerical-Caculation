import numpy as np

E = 10e-5


def Jacobi(A, B, X):
    n = 0
    while(True):
        for i in range(len(A)):
            temp = B[i]
            for j in range(len(A[i])):
                if j != i:
                    temp -= A[i][j]*X[j][0]
            X[i][1] = temp/A[i][i]
        n += 1
        if max((np.fabs(X[i][1]-X[i][0]) for i in range(len(A)))) <= E:
            print("Jacobi迭代")
            print("迭代步数:", n)
            print([X[i][1] for i in range(len(A))])
            break
        for i in range(len(A)):
            X[i][0] = X[i][1]

def Gauss_Seidel(A, B, X):
    n = 0
    while(True):
        for i in range(len(A)):
            temp = B[i]
            for j in range(len(A[i])):
                if j != i:
                    temp -= A[i][j]*X[j][1]
            X[i][1] = temp/A[i][i]
        n += 1
        if max((np.fabs(X[i][1]-X[i][0]) for i in range(len(A)))) <= E:
            print("Gauss-Seidel迭代")
            print("迭代步数:", n)
            print([X[i][1] for i in range(len(A))])
            break
        for i in range(len(A)):
            X[i][0] = X[i][1]


def main():
    A = np.array([[31, -13, 0, 0, 0, -10, 0, 0, 0],
                  [-13, 35, -9, 0, -11, 0, 0, 0, 0],
                  [0, -9, 31, -10, 0, 0, 0, 0, 0],
                  [0, 0, -10, 79, -30, 0, 0, 0, -9],
                  [0, 0, 0, -30, 57, -7, 0, -5, 0],
                  [0, 0, 0, 0, -7, 47, -30, 0, 0],
                  [0, 0, 0, 0, 0, -30, 41, 0, 0],
                  [0, 0, 0, 0, -5, 0, 0, 27, -2],
                  [0, 0, 0, -9, 0, 0, 0, -2, 29]])
    B = np.array([-15, 27, -23, 0, -20, 12, -7, 7, 10])
    X = [[0, 0] for p in range(len(B))]
    Jacobi(A, B, X)
    print("*******************************************")
    Gauss_Seidel(A,B,X)

if __name__ == '__main__':
    main()
