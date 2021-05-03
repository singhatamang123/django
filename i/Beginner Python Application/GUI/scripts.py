from tkinter import *

def km_to_miles():
    miles= float(e1_var.get())*1.6
    t1.insert(END,  miles)

root = Tk()
b1 = Button(root, text="Executable", command=km_to_miles)
b1.grid(row=0, column=0)


e1_var = StringVar()
e1 = Entry(root, textvariable=e1_var)
e1.grid(row=0, column=1)

t1 = Text(root, height=1, width=20)
t1.grid(row=0, column=2)
root.mainloop()