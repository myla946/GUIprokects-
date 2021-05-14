from tkinter import *
import random

top = Tk()
playlist = []
myRolls = []
dieType = 0
rollTimes = 0

def printList():
    print(playlist)
    
def exportList():
    with open('text.txt', 'w') as f:
        for item in playlist:
            f.write("%s/n" % item())

 
def clearWindow():
    for widget in top.winfo_children():
        widget.destroy()


def mainMenu():
    clearWindow()
    LMain = Label(top, text = "Block 5 GUI projects")
    LMain.grid(column = 0, row = 1)
    B1Main = Button(text = "Week 1", bg = "White", command = week1)
    B1Main.grid(column = 0, row = 2)
    B2Main = Button(text = "Week 2", bg = "White", command = week2)
    B2Main.grid(column = 0, row = 3)
    B3Main = Button(text = "Week 3", bg = "White")
    B3Main.grid(column = 0, row = 4)
    
    


def week1():
    clearWindow()
    def results():
        result = E1.get()
        playlist. append(result)
        E1.delete(0, END)

    #This is an label widget
    L1 = Label(top, text="Playlist Generator")
    L1.grid(collumn = 0, row =1)

    #This is an Entry widget 
    E1= Entry(top, bd = 5)
    E1.grid(collumn = 0, row = 2)

    #This is an Button widget
    B1= Button(text = " + ", bg = "white", command = result)
    B1.grid(collumn = 1, row= 2)

    B2 = Button(text = "Print ", bg = "light blue", command= printlist)
    B1.grid(collumn = 2, row = 2)

    B3 = Button(text = "Export List", bg = "#B4FFCD", command = exportList)
    B3.grid(column = 0, row = 3)

    Bexit = Button(text = "Clear Window", bg = "red", command = clearWindow)
    Bexit.grid(column = 1, row = 3)

def week2():
    #update variable data
    def rollDice():
        dieTyoe = E2Week2.get()
        rollTimes = E1Week2.get()
        #clear window AFTER updating varibals 
        clearWindow()
        #roll the dice
        for x in range(0, int(rollTime)):
            myRolls.append(random.randit(1, int(dieType)))

        #build the results window
        L4Week2 = Label(top,  text= "Here's your rolls!")
        L4Week2.grid(column = 0, row = 1)

        L5Week2 = Label(top, text= "{}".format(myRolls))
        L5Week2.grid(column = 0, row = 2)

        B2Week2 = Button(text="Main Menu", bg= "yellow", command= mainMenu)
        B2Week2.grid(column = 0, row = 3)



    clearWindow()
    B1Week2 = Button(tex = "Roll em!", bg="yellow")

    L1Week2 = Label(top, text="# of rolls")
    L1Week1.grid(column = 0, row = 2)

    L2Week2 = Label(top, text="# of sides ")
    L2.grid(column = 3, row = 2)

    L3Week2 = Label(top, text= "Dice Roller App")
    L1Week2.grid(column = 2, row = 1)

    E1Week2 = Entry()
    E2Week2 = Entry()


if __name__ == "__main__":
    mainMenu()
    top.mainloop()
