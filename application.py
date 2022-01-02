import math
import os
from tkinter import *
import seaborn as sns
import numpy as np
import pandas as pd
import scipy
import seaborn as sns
from matplotlib import pyplot as plt
from pandas.core.frame import DataFrame
from PIL import Image, ImageTk
from scipy.stats import norm
from sklearn import linear_model

# Functions..........................................................................................................


def disable_event():
    pass


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

# Code..................................................................................................................


df = pd.read_csv('./StudentsPerformance.csv')
passmark = 40

df['Percentage'] = (df.math +
                    df.reading+df.writing)/3
df["grade"] = df.apply(lambda x: Grade(x["Percentage"]), axis=1)
plt.tight_layout()


# Game loop.....................................................................................................................
root = Tk()
root.protocol("WM_DELETE_WINDOW", disable_event)
# Declarations and imports...........................................................................................
root.geometry("800x500")
image = Image.open("800.png")
photo = ImageTk.PhotoImage(image, master=root)
background1 = Label(root, image=photo)
background1.image = image
menu = Menu(root)
root.config(menu=menu)
exitMenu = Menu(menu)
menu.add_cascade(label='Exit', menu=exitMenu)
exitMenu.add_command(label='Exit', command=quit)


# Functions..........................................................................................................

def statistics():
    # Stat funcitons.....................................

    def exitStat():
        root.deiconify()
        statWindow.destroy()

    def genderPie():
        # Gender Ration Pie plot ------------------------
        sns.set(style='whitegrid')
        plt.figure(figsize=(14, 7))
        labels = ['Female', 'Male']
        plt.title('Gender')
        plt.axis('equal')
        plt.pie(df['gender'].value_counts(), labels=labels, explode=[0.1, 0.1],
                autopct='%1.2f%%', colors=['#E37383', '#FFC0CB'], startangle=90)
        plt.savefig('fig1.png')
        plt.clf()
        showPlot()
        description.config(
            text="Out of the total number of students, 51.89'%' are females while 48.20'%' are males.")

    def genderScore():
        # Gender v Score plot ----------------------------
        plt.figure(figsize=(10, 5))
        sns.set_context("talk", font_scale=1)
        sns.set_palette("pastel")
        ax = sns.countplot(y="grade", hue="gender", data=df, order=[
            "O", "A", "B", "C", "D", "E", "F"])
        ax.legend(loc='upper right', frameon=True)
        plt.title('Gender vs Grades', fontsize=18, fontweight='bold')
        ax.set(xlabel='COUNT', ylabel='GRADE')
        plt.savefig('fig1.png')
        showPlot()
        plt.clf()
        description.config(
            text="More female students received A and B Grade relative to male students. More number of boys received D and E grade.")

    def prepPlot():
        # tet preparation ---------------------------------
        sns.set_context("talk", font_scale=0.5)
        sns.set_palette("Pastel2")
        sns.kdeplot(data=df, x="Percentage",
                    hue="prep", multiple="stack")
        plt.title('Percentage vs Test Preparation',
                  fontsize=15, fontweight='bold')
        plt.savefig('fig1.png')
        showPlot()
        plt.clf()
        description.config(
            text="Students who have completed their test preparations have definitely scored better. ")

    def lunchPlot():
        # standard vs freee lunch
        sns.set_context("notebook", font_scale=0.8)
        sns.kdeplot(data=df, x="Percentage", hue="lunch",
                    multiple="layer", fill=True)
        plt.xlabel('Percentage')
        plt.title('Percentage vs Lunch Kde Plot',
                  fontsize=15, fontweight='bold')
        plt.savefig('fig1.png')
        showPlot()
        plt.clf()
        description.config(
            text="Students who had the standard lunch have performed very well. Students who had the free/reduced lunch have not performed so well.")

    def scoreLunchPlot():
        # writing score lunch vs percentage
        sns.set_palette("tab10")
        g = sns.JointGrid(data=df, x="Percentage",
                          y="writing", hue="lunch")
        g.plot(sns.scatterplot, sns.histplot)
        plt.title('Percentage and Writing score vs Lunch',
                  fontsize=15, fontweight='bold', y=1.3, loc="right")
        plt.savefig('fig1.png')
        showPlot()
        plt.clf()
        description.config(
            text="Students who had the standard lunch have performed very well. Students who had the free/reduced lunch have not performed so well.")

    def racePercentage():
        # race and percentage box plot analysis
        sns.set_palette("vlag")
        sns.catplot(x="race", y="Percentage", kind="boxen",
                    data=df.sort_values("race"))
        plt.title('Race/ethnicity vs Percentage',
                  fontsize=15, fontweight='bold')
        plt.savefig('fig1.png')
        showPlot()
        plt.clf()
        description.config(
            text="The average of group E is highest among all the groups while the average of group A is lowest.")

    def correlationScores():
        # correlation analysis scores and percantages----------------------
        plt.figure(figsize=(8, 8))
        plt.title('Correlation Analysis', color='Red', fontsize=20, pad=40)

        corr = df.corr()
        mask = np.triu(np.ones_like(corr, dtype=bool))
        sns.heatmap(df.corr(), mask=mask, annot=True, linewidths=.5)
        plt.xticks(rotation=60)
        plt.yticks(rotation=60)
        plt.savefig('fig1.png')
        showPlot()
        plt.clf()
        description.config(
            text="Almost all the scores are close to each other. There is average success in all three course.")

    # Stat Window Code....................................
    root.withdraw()
    statWindow = Toplevel()

    def showPlot():
        figure = Image.open("fig1.png")
        figure = figure.resize((780, 390), Image.ANTIALIAS)
        fPhoto = ImageTk.PhotoImage(figure, master=statWindow)
        figSet = Label(statWindow, image=fPhoto)
        figSet.image = fPhoto
        figSet.place(x=10, y=100)

    statWindow.protocol("WM_DELETE_WINDOW", disable_event)
    statWindow.geometry("800x500")
    statPhoto = ImageTk.PhotoImage(image, master=statWindow)
    bgS = Label(statWindow, image=statPhoto)
    bgS.image = statPhoto

    # Buttons
    menu = Menu(statWindow)
    statWindow.config(menu=menu)
    chartMenu = Menu(menu)
    menu.add_cascade(label='Choose Chart', menu=chartMenu)
    chartMenu.add_command(label='Gender Pie Chart', command=genderPie)
    chartMenu.add_command(
        label='Grades w.r.t Gender Chart', command=genderScore)
    chartMenu.add_command(
        label='Grades w.r.t Preparation Chart', command=prepPlot)
    chartMenu.add_command(label='Grades w.r.t Lunch Chart', command=lunchPlot)
    chartMenu.add_command(
        label='Percentage and Score w.r.t Lunch Chart', command=scoreLunchPlot)
    chartMenu.add_command(
        label='Percentages w.r.t Race BoxPlot', command=racePercentage)
    chartMenu.add_command(
        label='Correlations Between Scores chart', command=correlationScores)
    chartMenu.add_separator()
    chartMenu.add_command(label='Exit', command=exitStat)

    # make a menu and add all the functions and add commands and hide top cross and add exit and add label with findings.

    # placement.......................................
    bgS.place(x=0, y=0)
    description = Label(statWindow, text="Decription of image here",
                        font=("Times New Roman", 10), anchor="center")
    description.place(x=10, y=30)
    # gPie.place(x=300, y=100)

    statWindow.mainloop()


def probability():
    def exitProb():
        root.deiconify()
        probWindow.destroy()

    def normalMath():
        sns.histplot(df.math, kde=TRUE)
        plt.savefig('fig1.png')
        showPlot()
        plt.clf()
        getEntry()

    def normalReading():
        sns.histplot(df.reading, kde=TRUE)
        plt.savefig('fig1.png')
        showPlot()
        plt.clf()
        getEntry()

    def normalWriting():
        sns.histplot(df.writing, kde=TRUE)
        plt.savefig('fig1.png')
        showPlot()
        plt.clf()
        getEntry()

    def mathProb(score):
        mean = df.math.mean()
        std = df.math.std()
        x = score
        zScore = (x-mean)/std
        prob = norm.cdf(zScore)
        strAns = "The probability of getting upto " + \
            str(score) + " marks in Maths is " + str(prob*100) + "%"
        strAns1 = "The probability of getting at-least " + \
            str(score) + " marks in Maths is " + str((1-prob)*100) + "%"
        description.config(text=strAns)
        description1.config(text=strAns1)

    def readProb(score):
        mean = df.reading.mean()
        std = df.reading.std()
        x = score
        zScore = (x-mean)/std
        prob = norm.cdf(zScore)
        strAns = "The probability of getting upto " + \
            str(score) + " marks in Reading is " + str(prob*100) + "%"
        strAns1 = "The probability of getting at-least " + \
            str(score) + " marks in Reading is " + str((1-prob)*100) + "%"
        description.config(text=strAns)
        description1.config(text=strAns1)

    def writeProb(score):
        mean = df.writing.mean()
        std = df.writing.std()
        x = score
        zScore = (x-mean)/std
        prob = norm.cdf(zScore)
        strAns = "The probability of getting upto " + \
            str(score) + " marks in Writing is " + str(prob*100) + "%"
        strAns1 = "The probability of getting at-least " + \
            str(score) + " marks in Writing is " + str((1-prob)*100) + "%"
        description.config(text=strAns)
        description1.config(text=strAns1)

    def getEntry():
        enterNum = Entry(probWindow, text="Enter Marks", textvariable=value)
        enterNum.place(x=420, y=20)
        subBtn = Button(probWindow, text="Submit",
                        command=submitMarks)
        subBtn.place(x=495, y=39)

    def submitMarks():
        print(value.get())
        print(checkVal.get())
        marks = float(value.get())
        if marks > 0 and marks < 100:
            if checkVal.get() == 1:
                mathProb(marks)
            elif checkVal.get() == 2:
                readProb(marks)
            elif checkVal.get() == 3:
                writeProb(marks)
        else:
            description.config(text="Give correct input please")

    # Window creation.......................................................................
    root.withdraw()
    probWindow = Toplevel()
    value = StringVar()

    def showPlot():
        figure = Image.open("fig1.png")
        figure = figure.resize((780, 390), Image.ANTIALIAS)
        fPhoto = ImageTk.PhotoImage(figure, master=probWindow)
        figSet = Label(probWindow, image=fPhoto)
        figSet.image = fPhoto
        figSet.place(x=10, y=100)

    probWindow.protocol("WM_DELETE_WINDOW", disable_event)
    probWindow.geometry("800x500")
    statPhoto = ImageTk.PhotoImage(image, master=probWindow)
    bgS = Label(probWindow, image=statPhoto)
    bgS.image = statPhoto
    bgS.place(x=0, y=0)
    # Exit Menu
    menu = Menu(probWindow)
    probWindow.config(menu=menu)
    chartMenu = Menu(menu)
    menu.add_cascade(label='Exit', menu=chartMenu)
    chartMenu.add_command(label='Exit', command=exitProb)
    description = Label(probWindow, text="Probability will show here", font=(
        "Times New Roman", 10, 'bold'), anchor="center")
    description1 = Label(probWindow, text="Probability will show here", font=(
        "Times New Roman", 10, 'bold'), anchor="center")

    # Buttons
    checkVal = IntVar()
    mathBtn = Radiobutton(probWindow, text="Maths Score", variable=checkVal,
                          value=1, command=normalMath).place(x=10, y=20)
    readBtn = Radiobutton(probWindow, text="Reading Score", variable=checkVal,
                          value=2, command=normalReading).place(x=150, y=20)
    writeBtn = Radiobutton(probWindow, text="Writing Score", variable=checkVal,
                           value=3, command=normalWriting).place(x=300, y=20)

    description.place(x=10, y=50)
    description1.place(x=10, y=75)


# Logic on objects......................................................................................................
welcome = Label(
    root, text="Welcome to our Statistics and probability Analysis", font=("Times New Roman", 20), anchor="center")

btn1 = Button(root, text="Statistics", width=20,  height=3,
              back='#f86363', command=statistics)
btn2 = Button(root, text="Probability", width=20,  height=3,
              back='#f86363', command=probability)
btn3 = Button(root, text="Predicitons", width=20,  height=3, back='#f86363')


# Placements of objects...............................................................................................
background1.place(x=0, y=0)
welcome.place(x=100, y=50)
btn1.place(x=75, y=250)
btn2.place(x=315, y=250)
btn3.place(x=557.5, y=250)


# mainloop
root.mainloop()
