import pandas as pd
from GMM import *
import util as plot
from matplotlib import pyplot as plt

def For_Iris(features,No_Component=2):

    data = pd.read_csv("Data/Iris.csv", header = 0)
    data = data.reset_index()
    replace_map = {'Species': {'Iris-virginica': 1, 'Iris-versicolor': 2,'Iris-setosa':3}}
    data.replace(replace_map, inplace=True)
    label=data[['Species']]
    col=['SepalWidthCm', 'PetalLengthCm']
    x=data[col]
    x=np.array(x)
    gmm = GaussianMixModel(x,No_Component)
    gmm.fit()
    plot.plot_2D(gmm,x,col,label)

def main():
  For_Iris(2,3)
if __name__== "__main__":
  main()
