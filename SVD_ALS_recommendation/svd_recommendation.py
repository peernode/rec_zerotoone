'''
数据集：https://grouplens.org/datasets/movielens/ml-latest-small.zip
步骤：
1. 构建数据矩阵
2. svd分解
3. 降维
4. 预测
'''

import pandas as pd
import numpy as np
from tqdm import tqdm
import sys

def readDatas():
    path = 'ml-latest-small/ratings.csv'
    odatas = pd.read_csv(path,usecols=[0,1,2])
    return odatas

def splitTrainSetTestSet(odatas):
    testset = odatas.sample(frac=0.2, axis=0)
    trainset = odatas.drop(index=testset.index.values.tolist(), axis=0)
    return trainset, testset

def getMatrix(trainset):
    userSet, itemSet = set(), set()
    # Return a Numpy representation of the DataFrame.
    for d in trainset.values:
        userSet.add(int(d[0]))
        itemSet.add(int(d[1]))

    userList = list(userSet)
    itemList = list(itemSet)

    # 构建共现矩阵，行为userid，列为itemid
    df = pd.DataFrame(0, index=userList, columns=itemList, dtype=float)
    for d in tqdm(trainset.values):
        df[d[1]][d[0]] = d[2]

    return df, userList, itemList

def svd(m,k):
    u, i, v = np.linalg.svd(m)
    return u[:,0:k], np.diag(i[0:k]), v[0:k,:]

def predict(u,i,v,user_index,item_index):
    return float(u[user_index].dot(i).dot(v.T[item_index].T))

def getPredicts(testSet, userList, itemList, u, i, v):
    y_true, y_hat = [], []
    for d in tqdm(testSet.values):
        user = int(d[0])
        item = int(d[1])
        if user in userList and item in itemList:
            # 找到user和item的index
            user_index = userList.index(user)
            item_index = itemList.index(item)
            y_true.append(d[2])
            y_hat.append(predict(u,i,v,user_index,item_index))

    return y_true, y_hat

def RMSE(a,b):
    return (np.average((np.array(a)-np.array(b))**2))**0.5

def play():
    k=200 #奇异值数量

    trainset, testset = splitTrainSetTestSet(readDatas())
    df, userList, itemList = getMatrix(trainset)
    u, i, v = svd(np.mat(df), k)

    train_y_true, train_y_hat = getPredicts(trainset, userList, itemList, u, i, v)
    test_y_true, test_y_hat = getPredicts(testset, userList, itemList, u, i, v)

    print(RMSE(train_y_true, train_y_hat))
    print(RMSE(test_y_true, test_y_hat))

if __name__ == '__main__':
    play()