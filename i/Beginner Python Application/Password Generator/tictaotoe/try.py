
from tkinter import *
from tkinter import messagebox
import tkinter
class Tic_Tac_Toe:

    def __init__(self, root) -> None:
        self.root = root
        self.root.title('Tic-Tac-Toe')
        self.root.geometry('1350x7500+0+0')
        self.root.config(background= 'Cadet Blue')
        Tops = Frame(self.root, bg='Cadet Blue', pady=2, width=1350, height=100,relief=RIDGE)
        Tops.grid(row=0, column=0)

        title = Label(Tops, font=('arial', 50, 'bold'),  text="advanced tic-tac-toe", bd=12, bg='Cadet Blue', fg='Cornsilk', justify=CENTER)
        title.grid(row=0, column=0)
        
        MainFrame = Frame(self.root, bg= 'Powder Blue', bd=10, width=1350,height=600, relief=RIDGE)
        MainFrame.grid(row=1, column=0)

        LeftFrame = Frame(MainFrame, bd=10, width=750, height=500, pady=2, padx=10, bg="Cadet Blue", relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        RightFrame = Frame(MainFrame, bd=10, width=460, height=500, pady=2,padx=10, bg="Cadet Blue", relief=RIDGE)
        RightFrame.pack(side=RIGHT)
        RightFrame2 = Frame(RightFrame, bd=10, width=560, height=200, pady=2,padx=10, bg="Cadet Blue", relief=RIDGE)
        RightFrame2.grid(row=0, column=0)
        RightFrame3 = Frame(RightFrame, bd=10, width=560, height=200, pady=2,padx=10, bg="Cadet Blue", relief=RIDGE)
        RightFrame3.grid(row=1, column=0)

        self.PlayerX = IntVar()
        self.PlayerO = IntVar()

        self.PlayerX.set(0)
        self.PlayerO.set(0)
        self.buttons = StringVar()
        self.click = True




        def checker(buttons):
            global click
            if buttons["text"]==" " and self.click == True:
                buttons["text"] = "X"
                self.click = False
                score()
            elif buttons["text"]==" " and self.click == False:
                buttons["text"] = "O"
                self.click = True
                score()

        # for reset button
        def reset():
            Button1["text"] = " "
            Button2["text"] = " "
            Button3["text"] = " "
            Button4["text"] = " "
            Button5["text"] = " "
            Button6["text"] = " "
            Button7["text"] = " "
            Button8["text"] = " "
            Button9["text"] = " "

            Button1.configure(background="gainsboro")
            Button2.configure(background="gainsboro")
            Button3.configure(background="gainsboro")
            Button4.configure(background="gainsboro")
            Button5.configure(background="gainsboro")
            Button6.configure(background="gainsboro")
            Button7.configure(background="gainsboro")
            Button8.configure(background="gainsboro")
            Button9.configure(background="gainsboro")

        def new():
            reset()
            self.PlayerX.set(0)
            self.PlayerO.set(0)

        
        def score():
             if (Button1["text"]=="X" and Button2["text"]=="X" and Button3["text"]=="X"):
                 Button1.configure(background="powder blue")
                 Button2.configure(background="powder blue")
                 Button3.configure(background="powder blue")
                 n = float(self.PlayerX.get())
                 result =(n+1)
                 self.PlayerX.set(result)
                 messagebox.showinfo("Playe X , you won the game")

             if (Button4["text"]=="X" and Button5["text"]=="X" and Button6["text"]=="X"):
                 Button4.configure(background="red")
                 Button5.configure(background="red")
                 Button6.configure(background="red")
                 n = float(self.PlayerX.get())
                 result =(n+1)
                 self.PlayerX.set(result)
                 messagebox.showinfo("Playe X , you won the game")

             if (Button7["text"]=="X" and Button8["text"]=="X" and Button9["text"]=="X"):
                 Button7.configure(background="cadet blue")
                 Button8.configure(background="cadet blue")
                 Button9.configure(background="cadet blue")
                 n = float(self.PlayerX.get())
                 result =(n+1)
                 self.PlayerX.set(result)
                 messagebox.showinfo("Playe X , you won the game")

             if (Button3["text"]=="X" and Button5["text"]=="X" and Button7["text"]=="X"):
                 Button3.configure(background="cadet blue")
                 Button5.configure(background="cadet blue")
                 Button7.configure(background="cadet blue")
                 n = float(self.PlayerX.get())
                 result =(n+1)
                 self.PlayerX.set(result)
                 messagebox.showinfo("Playe X , you won the game")

             if (Button3["text"]=="X" and Button6["text"]=="X" and Button9["text"]=="X"):
                 Button3.configure(background="cadet blue")
                 Button6.configure(background="cadet blue")
                 Button9.configure(background="cadet blue")
                 n = float(self.PlayerX.get())
                 result =(n+1)
                 self.PlayerX.set(result)
                 messagebox.showinfo("Playe X , you won the game")

             if (Button2["text"]=="X" and Button5["text"]=="X" and Button8["text"]=="X"):
                 Button2.configure(background="cadet blue")
                 Button5.configure(background="cadet blue")
                 Button8.configure(background="cadet blue")
                 n = float(self.PlayerX.get())
                 result =(n+1)
                 self.PlayerX.set(result)
                 messagebox.showinfo("Playe X , you won the game")

             if (Button1["text"]=="X" and Button4["text"]=="X" and Button7["text"]=="X"):
                 Button1.configure(background="cadet blue")
                 Button4.configure(background="cadet blue")
                 Button7.configure(background="cadet blue")
                 n = float(self.PlayerX.get())
                 result =(n+1)
                 self.PlayerX.set(result)
                 messagebox.showinfo("Playe X , you won the game")

             if (Button1["text"]=="X" and Button5["text"]=="X" and Button9["text"]=="X"):
                 Button1.configure(background="cadet blue")
                 Button5.configure(background="cadet blue")
                 Button9.configure(background="cadet blue")
                 n = float(self.PlayerX.get())
                 result =(n+1)
                 self.PlayerX.set(result)
                 messagebox.showinfo("Playe X , you won the game")


                 # For the O Player
             if (Button1["text"]=="O" and Button2["text"]=="O" and Button3["text"]=="O"):
                 Button1.configure(background="powder blue")
                 Button2.configure(background="powder blue")
                 Button3.configure(background="powder blue")
                 n = float(self.PlayerO.get())
                 result =(n+1)
                 self.PlayerO.set(result)
                 messagebox.showinfo("Playe O , you won the game")

             if (Button4["text"]=="O" and Button5["text"]=="O" and Button6["text"]=="O"):
                 Button4.configure(background="red")
                 Button5.configure(background="red")
                 Button6.configure(background="red")
                 n = float(self.PlayerO.get())
                 result =(n+1)
                 self.PlayerO.set(result)
                 messagebox.showinfo("Playe O , you won the game")

             if (Button7["text"]=="O" and Button8["text"]=="O" and Button9["text"]=="O"):
                 Button7.configure(background="cadet blue")
                 Button8.configure(background="cadet blue")
                 Button9.configure(background="cadet blue")
                 n = float(self.PlayerO.get())
                 result =(n+1)
                 self.PlayerO.set(result)
                 messagebox.showinfo("Playe O , you won the game")

             if (Button3["text"]=="O" and Button5["text"]=="O" and Button7["text"]=="O"):
                 Button3.configure(background="cadet blue")
                 Button5.configure(background="cadet blue")
                 Button7.configure(background="cadet blue")
                 n = float(self.PlayerO.get())
                 result =(n+1)
                 self.PlayerO.set(result)
                 messagebox.showinfo("Playe O , you won the game")

             if (Button3["text"]=="O" and Button6["text"]=="O" and Button9["text"]=="O"):
                 Button3.configure(background="cadet blue")
                 Button6.configure(background="cadet blue")
                 Button9.configure(background="cadet blue")
                 n = float(self.PlayerO.get())
                 result =(n+1)
                 self.PlayerO.set(result)
                 messagebox.showinfo("Playe O , you won the game")

             if (Button2["text"]=="O" and Button5["text"]=="O" and Button8["text"]=="O"):
                 Button2.configure(background="cadet blue")
                 Button5.configure(background="cadet blue")
                 Button8.configure(background="cadet blue")
                 n = float(self.PlayerO.get())
                 result =(n+1)
                 self.PlayerO.set(result)
                 messagebox.showinfo("Playe O , you won the game")

             if (Button1["text"]=="O" and Button4["text"]=="O" and Button7["text"]=="O"):
                 Button1.configure(background="cadet blue")
                 Button4.configure(background="cadet blue")
                 Button7.configure(background="cadet blue")
                 n = float(self.PlayerO.get())
                 result =(n+1)
                 self.PlayerO.set(result)
                 messagebox.showinfo("Playe O , you won the game")

             if (Button1["text"]=="O" and Button5["text"]=="O" and Button9["text"]=="O"):
                 Button1.configure(background="cadet blue")
                 Button5.configure(background="cadet blue")
                 Button9.configure(background="cadet blue")
                 n = float(self.PlayerO.get())
                 result =(n+1)
                 self.PlayerO.set(result)
                 messagebox.showinfo("Playe O , you won the game")
 


        # View player info 
        lbPlayerX = Label(RightFrame2, font=('arial', 40, 'bold'), bd=12, bg='Cadet Blue', padx=2, pady=2, text="PlayerX")
        lbPlayerX.grid(row=0, column=0, sticky=W)
        lbPlayerXentry = Entry(RightFrame2, font=('arial', 40, 'bold'), bd=2, bg='white', width=14, justify=LEFT, textvariable=self.PlayerX)
        lbPlayerXentry.grid(row=0, column=1)

        lbPlayerO = Label(RightFrame2, font=('arial', 40, 'bold'), bd=12, bg='Cadet Blue', padx=2, pady=2, text="PlayerO")
        lbPlayerO.grid(row=1, column=0, sticky=W)
        lbPlayerOentry = Entry(RightFrame2, font=('arial', 40, 'bold'), bd=2, bg='white', width=14, justify=LEFT, textvariable=self.PlayerO)
        lbPlayerOentry.grid(row=1, column=1)

        resetbtn= Button(RightFrame3, font=('arial', 40, 'bold'), bd=12, bg='Cadet Blue', height=1, width=20,  text="RESET GAME", command=reset)
        resetbtn.grid(row=2, column=0, padx=6, pady=11)

        newbtn= Button(RightFrame3, font=('arial', 40, 'bold'), bd=12, bg='Cadet Blue',height=1, width=20, text="NEW GAME", command=new)
        newbtn.grid(row=3, column=0, padx=6, pady=10)
        


        # Button for x and 0
        Button1 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3,width=8, bg='gainsboro', command=lambda:checker(Button1))
        Button1.grid(row=1, column=0, sticky=S+N+E+W)
        Button2 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3,width=8, bg='gainsboro', command=lambda:checker(Button2))
        Button2.grid(row=1, column=1, sticky=S+N+E+W)
        Button3 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3,width=8, bg='gainsboro', command=lambda:checker(Button3))
        Button3.grid(row=1, column=2, sticky=S+N+E+W)
        Button4 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3,width=8, bg='gainsboro', command=lambda:checker(Button4))
        Button4.grid(row=2, column=0, sticky=S+N+E+W)
        Button5 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3,width=8, bg='gainsboro', command=lambda:checker(Button5))
        Button5.grid(row=2, column=1, sticky=S+N+E+W)
        Button6 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3,width=8, bg='gainsboro', command=lambda:checker(Button6))
        Button6.grid(row=2, column=2, sticky=S+N+E+W)
        Button7 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3,width=8, bg='gainsboro', command=lambda:checker(Button7))
        Button7.grid(row=3, column=0, sticky=S+N+E+W)
        Button8 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3,width=8, bg='gainsboro', command=lambda:checker(Button8))
        Button8.grid(row=3, column=1, sticky=S+N+E+W)
        Button9 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3,width=8, bg='gainsboro', command=lambda:checker(Button9))
        Button9.grid(row=3, column=2, sticky=S+N+E+W)



       

root = Tk()
p = Tic_Tac_Toe(root)
root.mainloop()

   

