from tkinter import *

window = Tk()
window.title("Find the Smallest Number")
window.geometry("400x300+20+10")

def findSmallest():
    L = []
    L.append(eval(conOfent2.get()))
    L.append(eval(conOfent3.get()))
    L.append(eval(conOfent4.get()))
    smallestNumber.set(max(L))

lbl1 = Label(window ,text="The Program that Finds the Smallest Number")
lbl1.grid(row=0, column=1, columnspan=2, sticky=EW)
lbl2 = Label(window, text="Enter the first number:")
lbl2.grid(row=1, column=0, sticky=W)
conOfent2 = StringVar()
ent2 = Entry(window, bd=3, textvariable=conOfent2)
ent2.grid(row=1, column=1)
lbl3 = Label(window, text="Enter the second number:")
lbl3.grid(row=2, column=0)
conOfent3 = StringVar()
ent3 = Entry(window, bd=3, textvariable=conOfent3)
ent3.grid(row=2, column=1)
lbl4 = Label(window, text="Enter the third number:")
lbl4.grid(row=3, column=0, sticky=W)
conOfent4 = StringVar()
ent4 = Entry(window, bd=3, textvariable=conOfent4)
ent4.grid(row=3, column=1)

btn1 = Button(window, text="Find the Smallest no.", command=findSmallest)
btn1.grid(row=4, column=1)
lbl5 = Label(window, text="The Smallest number:")
lbl5.grid(row=5, column=0, sticky=W)
smallestNumber = StringVar()
ent5 = Entry(window, bd=3, state="readonly", textvariable=smallestNumber)
ent5.grid(row=5, column=1)


mainloop()