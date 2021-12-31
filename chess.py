from functools import wraps
import os
import numpy as np
import pandas as pd
from tkinter import *
import seaborn as sns
import pandas as pd
import missingno as msno
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings("ignore")

data = pd.read_csv('./games.csv')
pd.set_option('display.max_columns', None)

wRating = np.array(data["white_rating"])
bRating = np.array(data["black_rating"])
rating = np.stack((wRating, bRating), 1)
newone = np.array(abs(wRating - bRating))
w_rating = data["white_rating"]
win = []
for i in data["winner"]:
    if(i == "draw"):
        win.append(0)
    else:
        win.append(1)
win = np.array(win)
#rr = pd.DataFrame(win, newone)
# print(rr.corr())

# wRating.sort()
# bRating.sort()
print(wRating)
plt.plot(wRating, bRating)
plt.show()
