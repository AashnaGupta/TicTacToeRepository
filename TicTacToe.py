# create window
from Tkinter import *
from Tkinter import Button

window = Tk()
window.title("Tic Tac Toe")

# define variables
Player_1 = True
Player_2 = False
flag = 0

# Button functions
def button1():
    global Player_1
    global Player_2
    global flag
    if Player_1 == True and TopLeft["text"] == " ":
        TopLeft["text"] = "X"
        Player_1 = False
        Player_2 = True
        flag += 1
        check()

    elif Player_2 == True and TopLeft["text"] == " ":
        TopLeft["text"] = "0"
        Player_1 = True
        Player_2 = False
        flag += 1
        check()



def button2():
    global Player_1
    global Player_2
    global flag
    if Player_1 == True and TopMiddle["text"] == " ":
        TopMiddle["text"] = "X"
        Player_1 = False
        Player_2 = True
        flag += 1
        check()
    elif Player_2 == True and TopMiddle["text"] == " ":
        TopMiddle["text"] = "0"
        Player_1 = True
        Player_2 = False
        flag += 1
        check()


def button3():
    global Player_1
    global Player_2
    global flag
    if Player_1 == True and TopRight["text"] == " ":
        TopRight["text"] = "X"
        Player_1 = False
        Player_2 = True
        flag += 1
        check()
    elif Player_2 == True and TopRight["text"] == " ":
        TopRight["text"] = "0"
        Player_1 = True
        Player_2 = False
        flag += 1
        check()


def button4():
    global Player_1
    global Player_2
    global flag
    if(Player_1 == True)and(MiddleLeft["text"] == " "):
        MiddleLeft["text"] = "X"
        Player_1 = False
        Player_2 = True
        flag += 1
        check()
    elif Player_2 == True and MiddleLeft["text"] == " ":
        MiddleLeft["text"] = "0"
        Player_1 = True
        Player_2 = False
        flag += 1
        check()

def button5():
    global Player_1
    global Player_2
    global flag
    if Player_1 == True and MiddleMiddle["text"] == " ":
        MiddleMiddle["text"] = "X"
        Player_1 = False
        Player_2 = True
        flag += 1
        check()
    elif Player_2 == True and MiddleMiddle["text"] == " ":
        MiddleMiddle["text"] = "0"
        Player_1 = True
        Player_2 = False
        flag += 1
        check()

def button6():
    global Player_1
    global Player_2
    global flag
    if Player_1 == True and MiddleRight["text"] == " ":
        MiddleRight["text"] = "X"
        Player_1 = False
        Player_2 = True
        flag += 1
        check()
    elif Player_2 == True and MiddleRight["text"] == " ":
        MiddleRight["text"] = "0"
        Player_1 = True
        Player_2 = False
        flag += 1
        check()


def button7():
    global Player_1
    global Player_2
    global flag
    if Player_1 == True and BottomLeft["text"] == " ":
        BottomLeft["text"] = "X"
        Player_1 = False
        Player_2 = True
        flag += 1
        check()
    elif Player_2 == True and BottomLeft["text"] == " ":
        BottomLeft["text"] = "0"
        Player_1 = True
        Player_2 = False
        flag += 1
        check()

def button8():
    global Player_1
    global Player_2
    global flag
    if Player_1 == True and BottomMiddle["text"] == " ":
        BottomMiddle["text"] = "X"
        Player_1 = False
        Player_2 = True
        flag += 1
        check()
    elif Player_2 == True and BottomMiddle["text"] == " ":
        BottomMiddle["text"] = "0"
        Player_1 = True
        Player_2 = False
        flag += 1
        check()


def button9():
    global Player_1
    global Player_2
    global flag
    if Player_1 == True and BottomRight["text"] == " ":
        BottomRight["text"] = "X"
        Player_1 = False
        Player_2 = True
        flag += 1
        check()

    elif Player_2 == True and BottomRight["text"] == " ":
        BottomRight["text"] = "0"
        Player_1 = True
        Player_2 = False
        flag += 1
        check()



# create grid
TopLeft = Button(window, text=" ",command=button1)
TopMiddle = Button(window, text=" ", command=button2)
TopRight = Button(window, text=" ", command=button3)

# TopMiddle.pack(fill = X)
# TopMiddle.pack(fill = Y)
MiddleRight = Button(window, text=" ", command=button6)
# MiddleRight.pack(fill = X)
# MiddleRight.pack(fill = Y)
MiddleLeft = Button(window, text=" ", command=button4)
# MiddleLeft.pack(fill = X)
# MiddleLeft.pack(fill = Y)
MiddleMiddle = Button(window, text=" ", command=button5)
# MiddleMiddle.pack(fill = X)
# MiddleMiddle.pack(fill = Y)
BottomRight = Button(window, text=" ", command=button9)
# BottomRight.pack(fill = X)
# BottomRight.pack(fill = X)
BottomLeft = Button(window, text=" ", command=button7)
# BottomLeft.pack(fill = X)
# BottomLeft.pack(fill = Y)
BottomMiddle = Button(window, text=" ", command=button8)
# BottomMiddle.pack(fill = X)
# BottomMiddle.pack(fill = Y)

TopRight.grid(row=0, column=2)
TopLeft.grid(row=0, column=0)
TopMiddle.grid(row=0, column=1)
MiddleRight.grid(row=1, column=2)
MiddleLeft.grid(row=1, column=0)
MiddleMiddle.grid(row=1, column=1)
BottomRight.grid(row=2, column=2)
BottomLeft.grid(row=2, column=0)
BottomMiddle.grid(row=2, column=1)


def check():

    if TopLeft["text"] == "X" and TopRight["text"] == "X" and TopMiddle["text"] == "X":
        label = Label(window, text = "Player 1 won!", fg ="red")
        label.grid(row = 0, column=3)
    elif TopLeft["text"] == "0" and TopRight["text"] == "0" and TopMiddle["text"] == "0":
        label = Label(window, text = "Player 2 won!", fg ="red")
        label.grid(row = 0, column=3)
    elif MiddleLeft["text"] == "X" and MiddleRight["text"] == "X" and MiddleMiddle["text"] == "X":
        label = Label(window, text = "Player 1 won!", fg ="red")
        label.grid(row = 0, column=3)
    elif MiddleLeft["text"] == "0" and MiddleRight["text"] == "0" and MiddleMiddle["text"] == "0":
        label = Label(window, text = "Player 2 won!", fg ="red")
        label.grid(row = 0, column=3)
    elif BottomLeft["text"] == "X" and BottomRight["text"] == "X" and BottomMiddle["text"] == "X":
        label = Label(window, text = "Player 1 won!", fg ="red")
        label.grid(row = 0, column=3)

    elif BottomLeft["text"] == "0" and BottomRight["text"] == "0" and BottomMiddle["text"] == "0":
        label = Label(window, text="Player 2 won!", fg ="red")
        label.grid(row = 0, column=3)
    elif TopLeft["text"] == "X" and MiddleLeft["text"] == "X" and BottomLeft["text"] == "X":
        label = Label(window, text = "Player 1 won!", fg ="red")
        label.grid(row = 0, column=3)
    elif TopLeft["text"] == "0" and MiddleLeft["text"] == "0" and BottomLeft["text"] == "0":
        label = Label(window, text = "Player 2 won!", fg ="red")
        label.grid(row = 0, column=3)
    elif TopMiddle["text"] == "X" and MiddleMiddle["text"] == "X" and BottomMiddle["text"] == "X":
        label = Label(window, text = "Player 1 won!", fg ="red")
        label.grid(row = 0, column=3)
    elif TopMiddle["text"] == "0" and MiddleMiddle["text"] == "0" and BottomMiddle["text"] == "0":
        label = Label(window, text = "Player 2 won!", fg ="red")
        label.grid(row = 0, column=3)
    elif TopRight["text"] == "X" and MiddleRight["text"] == "X" and BottomRight["text"] == "X":
        label = Label(window, text = "Player 1 won!", fg ="red")
        label.grid(row = 0, column=3)
    elif TopRight["text"] == "0" and MiddleRight["text"] == "0" and BottomRight["text"] == "0":
        label = Label(window, text = "Player 2 won!", fg ="red")
        label.grid(row = 0, column=3)
    elif TopLeft["text"] == "X" and MiddleMiddle["text"] == "X" and BottomRight["text"] == "X":
        label = Label(window, text = "Player 1 won!", fg ="red")
        label.grid(row = 0, column=3)
    elif TopLeft["text"] == "0" and MiddleMiddle["text"] == "0" and BottomRight["text"] == "0":
        label = Label(window, text = "Player 2 won!", fg ="red")
        label.grid(row = 0, column=3)
    elif TopRight["text"] == "X" and MiddleMiddle["text"] == "X" and BottomLeft["text"] == "X":
        label = Label(window, text = "Player 1 won!", fg ="red")
        label.grid(row = 0, column=3)
    elif TopRight["text"] == "0" and MiddleMiddle["text"] == "0" and BottomLeft["text"] == "0":
        label = Label(window, text = "Player 2 won!", fg ="red")
        label.grid(row = 0, column=3)
    elif(flag == 9):
        label = Label(window, text = "Tic-Tac-Toe. It is a Tie", fg ="red")
        label.grid(row = 0, column=3)


window.mainloop()
