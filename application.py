import math
import os
import numpy as np
import pandas as pd
from tkinter import *
from matplotlib import pyplot as plt
from pandas.core.frame import DataFrame
import seaborn as sns
import scipy
from scipy.stats import norm
from sklearn import linear_model


root = Tk()
# Declarations and imports...........................................................................................
root.geometry("800x500")
back = PhotoImage(file="800.png")
back1 = PhotoImage(file="800.png")
fg = PhotoImage(file='bg.png')
backImage = Label(root, image=back)


# Functions..........................................................................................................

def Grade(Percentage):
    if (Percentage >= 95):
        return 'O'
    if (Percentage >= 81):
        return 'A'
    if (Percentage >= 71):
        return 'B'
    if (Percentage >= 61):
        return 'C'
    if (Percentage >= 51):
        return 'D'
    if (Percentage >= 41):
        return 'E'
    else:
        return 'F'


def statistics():
    # Stat funcitons.....................................
    def exitStat():
        root.deiconify()
        statWindow.destroy()

    # Stat Window Code....................................
    root.withdraw()
    statWindow = Toplevel()
    statWindow.geometry("800x500")
    bgS = Label(statWindow, image=back1)
    exStat = Button(statWindow, text="Exit", command=exitStat)

    # placement.......................................
    bgS.place(x=0, y=0)
    exStat.place(x=100, y=100)

    statWindow.mainloop()


# Logic on objects......................................................................................................
welcome = Label(
    root, text="Welcome to our Statistics and probability Analysis", font=("Blackadder ITC", 20))
btn1 = Button(root, text="Statistics", width=20,  height=3,
              back='#f86363', command=statistics)
btn2 = Button(root, text="Probability", width=20,  height=3, back='#f86363')
btn3 = Button(root, text="Predicitons", width=20,  height=3, back='#f86363')


# Placements of objects...............................................................................................
backImage.place(x=0, y=0)
welcome.place(x=172.5, y=50)
btn1.place(x=75, y=250)
btn2.place(x=315, y=250)
btn3.place(x=557.5, y=250)

# mainloop
root.mainloop()
