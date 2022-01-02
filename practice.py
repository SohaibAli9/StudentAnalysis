import math
import os
import numpy as np
import pandas as pd
from tkinter import *
from pandas.core.frame import DataFrame
import seaborn as sns
import scipy
from scipy.stats import norm
from matplotlib import pyplot as plt
from sklearn import linear_model

pd.set_option("max_columns", None)

# Functions ------------------------------------------------------------------------------------------------


# def Grade(Percentage):
#     if (Percentage >= 95):
#         return 'O'
#     if (Percentage >= 81):
#         return 'A'
#     if (Percentage >= 71):
#         return 'B'
#     if (Percentage >= 61):
#         return 'C'
#     if (Percentage >= 51):
#         return 'D'
#     if (Percentage >= 41):
#         return 'E'
#     else:
#         return 'F'


# def genderPie():
#     # Gender Ration Pie plot ------------------------
#     sns.set(style='whitegrid')
#     plt.figure(figsize=(14, 7))
#     labels = ['Female', 'Male']
#     plt.pie(df['gender'].value_counts(), labels=labels, explode=[0.1, 0.1],
#             autopct='%1.2f%%', colors=['#E37383', '#FFC0CB'], startangle=90)
#     plt.title('Gender')
#     plt.axis('equal')
#     plt.show()


# def genderScore():
#     # Gender v Score plot ----------------------------
#     plt.figure(figsize=(10, 5))
#     sns.set_context("talk", font_scale=1)
#     sns.set_palette("pastel")
#     ax = sns.countplot(y="grade", hue="gender", data=df, order=[
#         "O", "A", "B", "C", "D", "E", "F"])
#     ax.legend(loc='upper right', frameon=True)
#     plt.title('Gender vs Grades', fontsize=18, fontweight='bold')
#     ax.set(xlabel='COUNT', ylabel='GRADE')
#     plt.show()


# def correlationScores():
#     # correlation analysis scores and percantages----------------------
#     plt.figure(figsize=(8, 8))
#     plt.title('Correlation Analysis', color='Red', fontsize=20, pad=40)

#     corr = df.corr()
#     mask = np.triu(np.ones_like(corr, dtype=bool))
#     sns.heatmap(df.corr(), mask=mask, annot=True, linewidths=.5)
#     plt.xticks(rotation=60)
#     plt.yticks(rotation=60)
#     plt.show()


# def prepPlot():
#     # tet preparation ---------------------------------
#     sns.set_context("talk", font_scale=0.5)
#     sns.set_palette("Pastel2")
#     sns.kdeplot(data=df, x="Percentage",
#                 hue="test preparation course", multiple="stack")
#     plt.title('Percentage vs Test Preparation', fontsize=15, fontweight='bold')

#     plt.show()


# def lunchPlot():
#     # standard vs freee lunch
#     sns.set_context("notebook", font_scale=0.8)
#     sns.kdeplot(data=df, x="Percentage", hue="lunch",
#                 multiple="layer", fill=True)
#     plt.xlabel('Percentage')
#     plt.title('Percentage vs Lunch Kde Plot', fontsize=15, fontweight='bold')

#     plt.show()


# def scoreLunchPlot():
#     # writing score lunch vs percentage
#     sns.set_palette("tab10")
#     g = sns.JointGrid(data=df, x="Percentage", y="writing score", hue="lunch")
#     g.plot(sns.scatterplot, sns.histplot)
#     plt.title('Percentage and Writing score vs Lunch',
#               fontsize=15, fontweight='bold', y=1.3, loc="right")
#     plt.show()


# def racePercentage():
#     # race and percentage box plot analysis
#     sns.set_palette("vlag")
#     sns.catplot(x="race/ethnicity", y="Percentage", kind="boxen",
#                 data=df.sort_values("race/ethnicity"))
#     plt.title('Race/ethnicity vs Percentage', fontsize=15, fontweight='bold')

#     plt.show()


def isNormal(arr):
    p = scipy.stats.normaltest(arr)
    if p.pvalue < 0.001:
        return TRUE
    return FALSE


# def mathProb(score):
#     mean = score.mean()
#     std = score.std()
#     x = int(input("Enter Marks: "))
#     zScore = (x-mean)/std
#     prob = norm.cdf(zScore)
#     print("There is ", prob*100, "% probability of getting less than ", x, " marks")
#     print("There is ", (1 - prob)*100,
#           "% probability of getting more than ", x, " marks")


# def readProb(score):
#     mean = score.mean()
#     std = score.std()
#     x = int(input("Enter Marks: "))
#     zScore = (x-mean)/std
#     prob = norm.cdf(zScore)
#     print("There is ", prob*100, "% probability of getting less than ", x, " marks")
#     print("There is ", (1 - prob)*100,
#           "% probability of getting more than ", x, " marks")


# def writeProb(score):
#     mean = score.mean()
#     std = score.std()
#     x = int(input("Enter Marks: "))
#     zScore = (x-mean)/std
#     prob = norm.cdf(zScore)
#     print("There is ", prob*100, "% probability of getting less than ", x, " marks")
#     print("There is ", (1 - prob)*100,
#           "% probability of getting more than ", x, " marks")


def probMenu(maths, reading, writing):
    print("PRESS")
    print("1. for Maths Score Probability")
    print("2. for Writing Score Probability")
    print("3. for Reading Score Probability")
    choice = int(input("Enter: "))

    if choice == 1:
        mathProb(maths)
    elif choice == 2:
        writeProb(reading)
    elif choice == 3:
        readProb(writing)
    else:
        print("Invalid input")


# Code -----------------------------------------------------------------------------------------------------
df = pd.read_csv('./StudentsPerformance.csv')
passmark = 40

df['Percentage'] = (df.math +
                    df.reading+df.writing)/3
df["grade"] = df.apply(lambda x: Grade(x["Percentage"]), axis=1)
plt.tight_layout()


reg = linear_model.LinearRegression()
reg.fit(df[['math', 'writing']].values, df.reading)
print(reg.coef_)
print(reg.intercept_)
print(reg.predict([[67, 89]])[0])


# plt.xlabel('Maths Score', fontsize=10)
# plt.ylabel('Reading Score', fontsize=10)
# plt.scatter(df.math, df.reading, marker=".")
# plt.plot(df.math, reg.predict(df[["math"]]), color="red")
# plt.show()


# print(reg.predict([[90]]))


# print(df.corr())

# genderScore()
# correlationScores()
# genderPie()

# arr = np.array(df.math)

# if isNormal(arr):
#     print("yes")
# else:
#     print("no")

# sns.histplot(df.math, kde=TRUE)
# plt.show()
mean = df.math.mean()
std = df.math.std()
mathNorm = np.array(df.math)
# mathNorm = mathNorm[((mathNorm > (mean - 3*std)) &
#                      (mathNorm < (mean + 3*std)))]


# sns.histplot(mathNorm, kde=TRUE)
# plt.show()

# mathZ = np.array(((mathNorm-mathNorm.mean())/mathNorm.std()))
# mathZ = mathZ[(mathZ < 4) | (mathZ > -4)]
# # sns.histplot(mathZ, kde=TRUE)
# plt.show()
# print(mathZ.mean())
# print(mathZ.std())

# x = float(input("Enter Number: "))
# x = (x-mean)/std
# prob = (1 - norm.cdf(x))*100
# print("probability is: ", prob, " Percent")


# plt.show()


# distrbution which tell probability of getting particular score.
# clean data
# caluclate based on zcore the probability of getting  marks and print output
# maths fucntion, claens maths, gets input, greater than, less than, then computes
# do reverse too, so from zscore tell marks
# MORE THAN, LESS THAN, BETWEEN
# DONE#


# predicting scores with y = mxab because correaltion.

# DATA PREPROCESS
