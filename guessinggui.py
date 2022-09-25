# Importing the important modules
import random
import math
from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd

root = Tk()
root.title("Welcome to The Random Number Guessing Game!!")
root.geometry("800x400") # Setting up the WidthxHeight
root.resizable(0,0)

# Defining a function to set the range for the selection of the random number.

def range():
    global low,up
    low = sd.askfloat("Lower Range Selection", "Input an Float")
    up = sd.askfloat("Upper Range Selection", "Input an Float")
    prob = round(math.log(up - low + 1, 2))
    mb.showinfo("Amount of Tries", "It takes about {} tries in general to guess the correct number!".format(prob))
    return low, up

# Defining a function to generate the random number.

def genrandomnum():
    global x
    x = round(random.uniform(low, up))
    mb.showinfo("A Number was Generated!", "Please Guess the Number")

# Defining a function to take the users guess and promt the user if they wish to continue playong or giveup.

def get_me():
    count = 1
    num = sd.askfloat("Good Luck", "Please Enter Your Guess")
    while num != x:
        count += 1
        if num < x:
            mb.showinfo("","Your Guess was less than the Random number!")
        elif num > x:
            mb.showinfo("","Your Guess was greater than the Random number!")
        retry = mb.askyesno("","Would you like to Guess again?")
        if retry == 1:
            num = sd.askfloat("Good Luck", "Please Enter Your Guess")
        elif retry == 0:
            mb.showinfo("Better Luck Next time!!","The Random number was{}".format(x))
            break
    if num == x:
        mb.showinfo("Congratulation you guessed it","\n""It took you {} tries to guess the number".format(count))

# Creatring the Labels and Buttons:

L1 = Label(root, text="Step 1: Setting up the Range for the random number", font=("Times New Roman", 18))
L1.pack(pady=10)
rangebtn = Button(root, text="Setting the range", font=("Times New Roman", 12), command=range)
rangebtn.pack(pady=10)

L2 = Label(root, text="Step 2: Generating the random number", font=("Times New Roman", 18))
L2.pack(pady=10)
rdbtn = Button(root, text="Lets generate the random number!!", font=("Times New Roman", 12), command=genrandomnum)
rdbtn.pack(pady=10)

L2 = Label(root, text="Final Step: Entering our guess!!",font=("Times New Roman", 18))
L2.pack(pady=10)
ansbtn = Button(root, text="Let's begin", font=("Times New Roman", 12), command=get_me)
ansbtn.pack(pady=10)

mainloop()
