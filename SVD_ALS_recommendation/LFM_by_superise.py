'''
数据集：https://grouplens.org/datasets/movielens/ml-latest-small.zip
LFM：latent factor model 隐语义模型

surprise库：
http://surpriselib.com/
https://surprise.readthedocs.io
'''

from surprise import Dataset,Reader,SVD,dump
from surprise import accuracy
from surprise.model_selection import train_test_split
import pandas as pd

def readData():
    path = 'ml-latest-small/ratings.csv'
    odatas = pd.read_csv(path, usecols=[0,1,2])
    return odatas

def splitTrainSetTestSet(odatas,frac):
    reader = Reader(rating_scale=(0,5))
    data = Dataset.load_from_df(odatas[['userId','movieId','rating']], reader)
    trainset, testset = train_test_split(data, test_size=frac)
    return trainset, testset

def train():
    trainset, testset = splitTrainSetTestSet(readData(), 0.2)
    algo = SVD(n_factors=100,n_epochs=10,lr_all=0.005,reg_all=0.02,biased=True,verbose=True)
    algo.fit(trainset)
    accuracy.rmse(algo.test(testset))
    dump.dump('model/surprise_lfm.model',algo=algo)

def play():
    _, algo = dump.load('model/surprise_lfm.model')
    print(algo.predict(1, 1))

if __name__ == '__main__':
    train()
    # play()