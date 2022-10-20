
import streamlit as st

pip install zigzag


pip install yfinance
import yfinance as yf


data = yf.download("TSLA", start="2019-01-01", end="2019-04-30")


data=data['Adj Close']



X = data.to_numpy()

%matplotlib inline

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from zigzag import *


X = arr
pivots = peak_valley_pivots(X, 0.003, -0.003)



def plot_pivots(X, pivots):
    plt.xlim(0, len(X))
    plt.ylim(X.min()*0.99, X.max()*1.01)
    plt.plot(np.arange(len(X)), X, 'k:', alpha=1)
    plt.plot(np.arange(len(X))[pivots != 0], X[pivots != 0], 'k-')
    plt.scatter(np.arange(len(X))[pivots == 1], X[pivots == 1], color='g')
    plt.scatter(np.arange(len(X))[pivots == -1], X[pivots == -1], color='r')



plot_pivots(X, pivots)

