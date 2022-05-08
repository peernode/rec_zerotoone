'''
数据集：https://grouplens.org/datasets/movielens/ml-latest-small.zip
LFM：latent factor model 隐语义模型
步骤：
1. 声明两个分解向量和偏置
2. 用ALS方式进行求解
'''

import numpy as np

def prediction(pu,qi,bu,bi):
    return np.dot(pu, qi.T)+bu+bi

def getError(r,pu,qi,bu,bi):
    return r - prediction(pu,qi,bu,bi)

def tryTrain():
    real = np.mat([[1, 2, 3, 0, 3], [3, 0, 3, 1, 3], [3, 2, 0, 3, 1]])
    print(real)

    factors=4
    p = np.random.randn(3, factors)
    q = np.random.randn(5, factors)
    ul, il = real.shape
    bu = np.random.randn(ul)
    bi = np.random.randn(il)

    lr=0.05
    lamda=0.1
    for e in range(30):
        for u in range(ul):
            for i in range(il):
                r = real[u,i]
                if r!=0:
                    error = getError(r, p[u], q[i], bu[u], bi[i])
                    p[u] -= lr * (-2 * error * q[i] + 2 * lamda * p[u])
                    q[i] -= lr * (-2 * error * p[u] + 2 * lamda * q[i])
                    bu[u] -= lr * (-2 * error + 2 * lamda * bu[u])
                    bi[i] -= lr * (-2 * error + 2 * lamda * bi[i])

    print(finalPrediction(p,q,bu,bi))

def finalPrediction(pu,qi,bu,bi):
    p = np.dot(pu, qi.T)
    for u in p:
        u += bi
    for i in p.T:
        i += bu
    return p

if __name__ == '__main__':
    tryTrain()