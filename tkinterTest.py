from tkinter import *

top = Tk()
playlist = []

def results():
    result = E1.get()
    playlist. append(result)
    E1.delete(0, END)
    
def printList():
    print(playlist)
    
def exportList():
    with open('text.txt', 'w') as f:
        for item in playlist:
            f.write("%s/n" % item()


def clearWindow():
    for widget in top.winfo_children():
        widget.destroy()


def mainMenu():
    clearWindow()
    LMain = Label(top, text = "Block 5 GUI projects")
    LMain.grid(column = 0, row = 1)
    B1Main = Button(text = "Week 1", bg = "White")
    B1Main.grid(column = 0, row = 2)
    B2Main = Button(text = "Week 2", bg = "White")
    B2Main.grid(column = 0, row = 3)
    B3Main = Button(text = "Week 3", bg = "White")
    B3Main.grid(column = 0, row = 4)
    


    
#This is a label widget
L1 = Label(top, text="Playlist Generator")
L1.grid(collumn = 0, row =1)

#This is an Entry widget 
E1= Entry(top, bd = 5)
E1.grid(collumn = 0, row= 2)

#This is a Button widget
B1= Button(text" + ",bg="white", command=result)
B1.grid(collumn = 1, row= 2)

B2 = Button(text = "Print ", bg = "light blue", command= printlist)
B1.grid(collumn = 2, row = 2)

B3 = Button(text"Export List", bg = "#B4FFCD", command = exportList)
B3.grid(column = 0, row = 3)

Bexit = Button(text = "Clear Window", bg = "red", command = clearWindow)
Bexit.grid(column = 1, row = 3)









                    
top.mainloop()
