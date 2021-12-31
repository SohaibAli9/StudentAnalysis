from tkinter import *


def printName(event):
    print("My name is Sohaib")


root = Tk()

btn1 = Button(root, text="print Name")
btn1.bind("<Button-1>", printName)
btn1.pack() 

root.mainloop()

# lbl1 = Label(root, text="Name")
# lbl2 = Label(root, text="Password")
# inputName = Entry(root)
# inputPass = Entry(root)

# lbl1.grid(row=0, sticky=W)
# lbl2.grid(row=1, sticky=W)
# inputName.grid(row=0, column=1)
# inputPass.grid(row=1, column=1)

# c = Checkbutton(root, text="keep me logged in")
# c.grid(columnspan=2)

# topFrame = Frame(root)
# topFrame.pack(side=TOP)
# bottomFrame = Frame(root)
# bottomFrame.pack(side=BOTTOM)

# btn1 = Button(topFrame, text="Sex", fg="red")
# btn2 = Button(topFrame, text="Before", fg="orange")
# btn3 = Button(topFrame, text="the", fg="blue")
# btn4 = Button(bottomFrame, text="HEX", fg="green")

# btn1.pack(side=LEFT)
# btn2.pack(side=LEFT)
# btn3.pack(side=LEFT)
# btn4.pack(fill=Y)
