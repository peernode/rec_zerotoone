'''
数据集：https://grouplens.org/datasets/movielens/ml-latest-small.zip
步骤：
1. svd分解
2. 降维
3. 预测
'''
import numpy as np

def svd(data, k):
    u, i, v = np.linalg.svd(data)
    u = u[:,0:k]
    i = np.diag(i[0:k])
    v = v[:k,:]
    return u,i,v

def predictSignle(u_index, i_index, u, i, v):
    return u[u_index].dot(i).dot(v.T[i_index].T)

def play():
    k = 4
    data = np.mat([[1,2,3,1,1],[1,3,3,1,2],[3,1,1,2,1],[1,2,3,3,1]])
    u, i, v = svd(data, k)
    print(u.dot(i).dot(v))
    print(predictSignle(0, 0, u, i, v))

if __name__ == '__main__':
    play()