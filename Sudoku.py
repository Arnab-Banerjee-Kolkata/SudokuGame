from random import randint
from tkinter import *
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import time
import random
numbers = [1,2,3,4,5,6,7,8,9]

n=9
m=3
def search(c=0):
    "Recursively search for a solution starting at position c."
    i, j = divmod(c, n)
    i0, j0 = i - i % m, j - j % m # Origin of mxm block
    numbers = list(range(1, n + 1))
    random.shuffle(numbers)
    for x in numbers:
        if (x not in board[i]                     # row
            and all(row[j] != x for row in board) # column
            and all(x not in row[j0:j0+m]         # block
                 for row in board[i0:i])): 
            board[i][j] = x
            if c + 1 >= n**2 or search(c + 1):
                return board
    else:
            # No number is valid in this cell: backtrack and try again.
         board[i][j] = None
         return None

    return search()

EASY=45
MEDIUM=32
HARD=25
class Box:                          #Contains all characteristics and properties of a single box of the grid
    def __init__(self):
        self.isValue=False          #Stores is cell has value or is empty
        self.value=''               #Stores value of cell
        self.isInitialValue=False   #Stores if value in the cell is given in question(True) or input by user(False)
        self.bckgrnd="white"
def Create_puzzle(difficulty):
    global grid
    grid=[[Box() for i in range(9)] for j in range(9)]
    global board
    board=[[None for a in range(9)] for a in range(9)]
    search()    
    diff=0
    if(difficulty=="easy"):
        diff=EASY
    elif(difficulty=="medium"):
        diff=MEDIUM
    else:
        diff=HARD
    rows=[0 for i in range(9)]
    cols=[0 for i in range(9)]
    for i in range(diff):
        while True:
            x=randint(0,8)
            y=randint(0,8)
            chk=0
            if(i==diff-1):                
                for j in range(9):
                    if(rows[j]==0 or cols[j]==0):
                        chk=1
                        break                
            if(grid[x][y].isValue==False):
                grid[x][y].value=board[x][y]
                grid[x][y].isValue=True
                grid[x][y].isInitialValue=True
                rows[x]=cols[y]=1
                break
            if(chk==1):
                break
    if(chk==1):                    
        Create_puzzle(difficulty)


        
    
class chkBoard(tk.Frame):
    def __init__(self, parent):
    
        # use black background so it "peeks through" to 
        # form grid lines
        tk.Frame.__init__(self, parent, background="black")
        self._widgets = []
        
        for row in range(9):
            current_row = []
            for column in range(9):
                if(grid[row][column].isInitialValue==True and grid[row][column].bckgrnd=="red"):
                    label = tk.Label(self, text=grid[row][column].value,borderwidth=5, height=3, width=6, font=20,background=grid[row][column].bckgrnd, relief="raised")
                elif(grid[row][column].isInitialValue==True):
                    label = tk.Label(self, text=grid[row][column].value,borderwidth=5, height=3, width=6, font=20,background="skyblue", relief="raised")
                else:
                    label = tk.Label(self, text=grid[row][column].value,borderwidth=5, height=3, width=6, font=20,background=grid[row][column].bckgrnd)
                    
                   # data=label.get("%d")
                    
                if(column%3==2 and row%3==2):
                    label.grid(row=row, column=column, sticky="nsew", padx=(1,5), pady=(1,5))
                    current_row.append(label)
                elif(column%3==2):
                    label.grid(row=row, column=column, sticky="nsew", padx=(1,5), pady=1)
                    current_row.append(label)
                elif(row%3==2):
                    label.grid(row=row, column=column, sticky="nsew", padx=1, pady=(1,5))
                    current_row.append(label)
                else:
                    label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                    current_row.append(label)
        

class hintBoard(tk.Frame):
    def __init__(self, parent):
    
        # use black background so it "peeks through" to 
        # form grid lines
        tk.Frame.__init__(self, parent, background="black")
        self._widgets = []
        
        for row in range(9):
            current_row = []
            for column in range(9):                
                if(grid[row][column].isInitialValue==True):
                    label = tk.Label(self, text=grid[row][column].value,borderwidth=5, height=3, width=6, font=20,background="skyblue", relief="raised")
                else:
                    label = tk.Label(self, text=grid[row][column].value,borderwidth=5, height=3, width=6, font=20,background=grid[row][column].bckgrnd)                 
                   
                    
                if(column%3==2 and row%3==2):
                    label.grid(row=row, column=column, sticky="nsew", padx=(1,5), pady=(1,5))
                    current_row.append(label)
                elif(column%3==2):
                    label.grid(row=row, column=column, sticky="nsew", padx=(1,5), pady=1)
                    current_row.append(label)
                elif(row%3==2):
                    label.grid(row=row, column=column, sticky="nsew", padx=1, pady=(1,5))
                    current_row.append(label)
                else:
                    label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                    current_row.append(label)




class ResetDialog(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, background="white")        
        written=Frame(dia)
        written.pack(side="top")
        label=tk.Label(written, text="Do you want to clear all entered values?", borderwidth=1, height=5, width=40, font=20, background="white", foreground="red")
        label.grid(row=0,column=0)
        clck=Frame(dia)
        clck.pack(side="bottom")
        yb=tk.Button(clck, text="YES", width=20)
        yb.grid(row=5, column=1)
        yb.config(command=Reset)
        nb=tk.Button(clck, text="NO", width=20)
        nb.grid(row=5, column=15)
        nb.config(command=dia.destroy)
        dia.minsize(50,100)

def showResetDialog():
    global dia
    dia=tk.Tk()
    dia.title("RESET DIALOG BOX")
    ResetDialog(dia).pack(side="top", fill="x")
    dia.mainloop()



class NewGameDialog(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, background="white")        
        written=Frame(dia2)
        written.pack(side="top")
        label=tk.Label(written, text="Do you want to start a new game?", borderwidth=1, height=5, width=40, font=20, background="white", foreground="red")
        label.grid(row=0,column=0)
        clck=Frame(dia2)
        clck.pack(side="bottom")
        yb=tk.Button(clck, text="YES", width=20)
        yb.grid(row=5, column=1)
        yb.config(command=NewGame)
        nb=tk.Button(clck, text="NO", width=20)
        nb.grid(row=5, column=15)
        nb.config(command=dia2.destroy)
        dia2.minsize(50,100)

def showNewGameDialog():
    global dia2
    dia2=tk.Tk()
    dia2.title("NEW GAME DIALOG BOX")
    NewGameDialog(dia2).pack(side="top", fill="x")
    dia2.mainloop()
    

class DevelopersWindow(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, background="white")
        #img=PhotoImage(file="background.jpg")
        label1=tk.Label(self, text="TEAM:                                                   Bengal Institute Of Technology, Kolkata", borderwidth=1, height=5, width=80, font="Verdana 13 bold", background="white", foreground="black", anchor='w')
        label1.grid(row=0,column=0)
        label6=tk.Label(self, text="DATE:                                                   December, 2017", borderwidth=1, height=3, width=80, font="verdana 13 bold", background="white", foreground="black",anchor='w')
        label6.grid(row=1,column=0)
        label2=tk.Label(self, text="LEAD PROGRAMMER:                            ARNAB BANERJEE", borderwidth=1, height=5, width=80, font="verdana 13 bold", background="white", foreground="black", anchor='w')
        label2.grid(row=2,column=0)
        label3=tk.Label(self, text="ASSISTANT DEVELOPERS:                    RUPSA DE", borderwidth=1, height=2, width=80, font="verdana 13 bold", background="white", foreground="black", anchor='w')
        label3.grid(row=3,column=0)
        label4=tk.Label(self, text="                                                             SAIKAT KARFA", borderwidth=1, height=2, width=80, font="verdana 13 bold", background="white", foreground="black", anchor='w')
        label4.grid(row=4,column=0)
        label5=tk.Label(self, text="                                                             DEBAPRATIM CHAKRABORTY", borderwidth=1, height=2, width=80, font="verdana 13 bold", background="white", foreground="black", anchor='w')
        label5.grid(row=5,column=0)
        developers.minsize(100,100)



def showDevelopers():
    global developers
    developers=tk.Tk()
    developers.title("DEVELOPERS")
    DevelopersWindow(developers).pack(side="top", fill="x")
    developers.mainloop()



class makeGrid(tk.Frame):
    def __init__(self, parent):
    
        # use black background so it "peeks through" to 
        # form grid lines
        tk.Frame.__init__(self, parent, background="black")
        self._widgets = []
        
        for row in range(9):
            current_row = []
            for column in range(9):
                if(grid[row][column].isInitialValue==True):
                    label = tk.Label(self, text=grid[row][column].value,borderwidth=5, height=3, width=6, font=20,background="skyblue", relief="raised")
                else:
                    vcmd = (self.register(self.isLegal),'%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W',row,column)
                    label = tk.Entry(self, text=grid[row][column].value,borderwidth=0, width=10, font=70,background=grid[row][column].bckgrnd,
                                     cursor="hand1",justify='center',validate="key", validatecommand=vcmd)
                    
                   # data=label.get("%d")
                    
                if(column%3==2 and row%3==2):
                    label.grid(row=row, column=column, sticky="nsew", padx=(1,5), pady=(1,5))
                    current_row.append(label)
                elif(column%3==2):
                    label.grid(row=row, column=column, sticky="nsew", padx=(1,5), pady=1)
                    current_row.append(label)
                elif(row%3==2):
                    label.grid(row=row, column=column, sticky="nsew", padx=1, pady=(1,5))
                    current_row.append(label)
                else:
                    label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                    current_row.append(label)
        
                
            self._widgets.append(current_row)
        chkbutton=tk.Button(self,text="CHECK",width=20, height=2)
        chkbutton.grid(row=0,column=9)
        chkbutton.config(command=makeGrid.check)
        clr=tk.Button(self,text="RESET",width=20, height=2)
        clr.grid(row=1,column=9)
        clr.config(command=showResetDialog)
        hn=tk.Button(self, text="HINT",width=20, height=2)
        hn.grid(row=2,column=9)
        hn.config(command=makeGrid.ShowHint)
        sub=tk.Button(self,text="SUBMIT",width=20, height=2)
        sub.grid(row=3, column=9)
        sub.config(command=Submit)
        newg=tk.Button(self,text="NEW GAME",width=20, height=2)
        newg.grid(row=4, column=9)
        newg.config(command=showNewGameDialog)
        dev=tk.Button(self, text="DEVELOPERS", width=20, height=2)
        dev.grid(row=5, column=9)
        dev.config(command=showDevelopers)
        

        for column in range(9):
            self.grid_columnconfigure(column, weight=1)
    def isLegal(self, d, i, P, s, S, v, V, W,row,column):
        if(int(i)>0):
            self.bell()
            return False
        if(len(P)==0):
            grid[int(row)][int(column)].value=''
            grid[int(row)][int(column)].isValue=False
            return True
        for char in S:
            if(char.isdigit()==False):
                self.bell()
                return False
        inval=int(S)
        if(inval<1 or inval>9):
            self.bell()
            return False
        else:
            grid[int(row)][int(column)].value=inval
            grid[int(row)][int(column)].isValue=True
            return True

    def check():
        chk1=0
        for i in range(9):
            for j in range(9):
                
                if(grid[i][j].isInitialValue):
                    continue
                val=grid[i][j].value
                for k in range(9):
                    if(grid[i][k].value==val and val!='' and k!=j):
                        grid[i][j].bckgrnd="red"
                        grid[i][k].bckgrnd="red"
                        chk1=1
                    if(grid[k][j].value==val and val!='' and k!=i):
                        grid[k][j].bckgrnd="red"
                        grid[i][j].bckgrnd="red"
                        chk1=1
                startx=i-(i%3)
                starty=j-(j%3)
                for k in range(startx,startx+3):
                    for m in range(starty, starty+3):
                        if(grid[k][m].value==val and val!='' and (k!=i and m!=j)):
                            grid[k][m].bckgrnd="red"
                            grid[i][j].bckgrnd="red"
                            chk1=1                            
                            break
                    
        if(chk1==1):
            root2=tk.Tk()
            root2.title("SUDOKU-CHECK(3 SEC)")
            chkBoard(root2).pack(side="top", fill="x")            
            root2.after(3000,root2.destroy)
            #time.sleep(5)
            for i in range(9):
                for j in range(9):
                    grid[i][j].bckgrnd="white"



    def ShowHint():
        chk1=0
        for i in range(9):
            for j in range(9):
                if(grid[i][j].value!=board[i][j] and grid[i][j].isValue==True):
                    grid[i][j].bckgrnd="orange"
                if(grid[i][j].isValue==False):
                    grid[i][j].value=board[i][j]
                    grid[i][j].bckgrnd="lightgreen"
        root2=tk.Tk()
        root2.title("SUDOKU-HINT(5 SEC)")
        hintBoard(root2).pack(side="top", fill="x")            
        root2.after(5000,root2.destroy)
        #time.sleep(5)
        for i in range(9):
            for j in range(9):
                 grid[i][j].bckgrnd="white"
                 if(grid[i][j].isValue==False):
                     grid[i][j].value=''

    




def Reset():
    dia.destroy()
    for i in range(9):
        for j in range(9):
            if(grid[i][j].isInitialValue==False):
                grid[i][j].value=''
                grid[i][j].isValue=False
    #print("Operation Complete.")
    root.destroy()
    set()


def set():
    global root
    root=tk.Tk()
    root.title("SUDOKU")
    makeGrid(root).pack(side="top", fill="x")
    root.mainloop()







def winner(chk1):
    canvas_width = 500
    canvas_height =500

    master = tk.Tk()
    master.title("RESULT")
    MARGIN=20
    SIDE=50
    w = Canvas(master,
    width=canvas_width, 
    height=canvas_height)
    w.pack()
    st=''
    tg=''
    if(chk1==0):
        st="RIGHT ANSWER!"
        tg="AC"
        x0=y0=MARGIN+SIDE*2
        x1=y1=MARGIN+SIDE*7
        w.create_oval(x0,y0,x1,y1,
           tags="victory", fill="light green", outline="black")
        x = y = MARGIN + 4 * SIDE + SIDE / 2
        w.create_text(x, y,
            text=st, tags=tg,
            fill="black", font=("Arial", 32))
    else:
        st="WRONG ANSWER!"
        tg="WA"
        x0=y0=MARGIN+SIDE*2
        x1=y1=MARGIN+SIDE*7
        w.create_oval(x0,y0,x1,y1,
           tags="victory", fill="dark orange", outline="red")

        x = y = MARGIN + 4 * SIDE + SIDE / 2
        w.create_text(x, y,
            text=st, tags=tg,
            fill="red", font=("Arial", 32))
        
    #root2=tk.Tk()
    mainloop()
    



def NewGame():
    dia2.destroy()
    root.destroy()
    for i in range(9):
        for j in range(9):
            grid[i][j].value=''
            grid[i][j].isValue=False
            grid[i][j].isInitialValue=False
            grid[i][j].bckgrnd="white"
    global root3
    root3=tk.Tk()
    root3.title("SELECT DIFFICULTY")
    es=tk.Button(root3,text="EASY",width=15)
    es.grid(row=0, column=3)
    es.config(command=setEasy)
    mid=tk.Button(root3,text="MEDIUM",width=15)
    mid.grid(row=0, column=6)
    mid.config(command=setMid)
    hr=tk.Button(root3,text="HARD",width=15)
    hr.grid(row=0, column=9)
    hr.config(command=setHard)
    root3.mainloop()
    
    


def Submit():
        chk1=0
        chk2=0
        for i in range(9):
            for j in range(9):
                
                if(grid[i][j].isInitialValue):
                    continue
                if(grid[i][j].isValue==False):
                   chk2=1
                val=grid[i][j].value
                for k in range(9):
                    if(grid[i][k].value==val and val!='' and k!=j):                        
                        chk1=1
                    if(grid[k][j].value==val and val!='' and k!=i):                        
                        chk1=1
                startx=i-(i%3)
                starty=j-(j%3)
                for k in range(startx,startx+3):
                    for m in range(starty, starty+3):
                        if(grid[k][m].value==val and val!='' and (k!=i and m!=j)):                            
                            chk1=1                            
                            break
            if(chk2==1):
                break
        if(chk2==0 and chk1==0):            
            winner(chk1)
        else:
            winner(1)
        
        
def setEasy():
    root3.destroy()
    Create_puzzle("easy")
    global root
    root=tk.Tk()
    root.title("SUDOKU")
    makeGrid(root).pack(side="top", fill="x")
    root.mainloop()
def setMid():
    root3.destroy()
    Create_puzzle("medium")
    global root
    root=tk.Tk()
    root.title("SUDOKU")
    makeGrid(root).pack(side="top", fill="x")
    root.mainloop()
def setHard():
    root3.destroy()
    Create_puzzle("hard")
    global root
    root=tk.Tk()
    root.title("SUDOKU")
    makeGrid(root).pack(side="top", fill="x")
    root.mainloop()



        
#just a checker method                
def main():
    global root3
    root3=tk.Tk()
    root3.title("SELECT DIFFICULTY")
    es=tk.Button(root3,text="EASY",width=15)
    es.grid(row=0, column=3)
    es.config(command=setEasy)
    mid=tk.Button(root3,text="MEDIUM",width=15)
    mid.grid(row=0, column=6)
    mid.config(command=setMid)
    hr=tk.Button(root3,text="HARD",width=15)
    hr.grid(row=0, column=9)
    hr.config(command=setHard)
    root3.mainloop()
    
if(__name__=="__main__"):
    main()
