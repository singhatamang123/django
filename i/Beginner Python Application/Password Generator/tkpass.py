from tkinter import *

import string, random
from tkinter import messagebox
class password:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("Generator")
        self.root.geometry("600x400")

    
        self.passlength = IntVar()
        self.passstr = IntVar()
        self.passstr.set('')
        self.passlength.set(0)

        
        pass_label = Label(self.root, text="Password")
        pass_label.grid(row=0, column=0)

        pass_entry = Entry(self.root, textvariable=self.passstr)
        pass_entry.grid(row=0, column=1)

        length_label = Label(self.root, text="Enter password Length")
        length_label.grid(row=1, column=0)
        length_entry = Entry(self.root, textvariable=self.passlength)
        length_entry.grid(row=1, column=1)

        gent_button = Button(self.root, text="Generate password", command=self.gen)
        gent_button.grid(row=2, column=1)

       
    def gen(self):
        passes = ""
        s1 = string.ascii_lowercase
        s2 = string.ascii_uppercase
        s4 = string.punctuation
        s3 = string.digits + s1 + s2 + s4
        try:
            for i in range(self.passlength.get()): 
                passes = passes + random.choice(s3)
            self.passstr.set(passes)
        except:
            messagebox.showerror("Plese insert number")

root = Tk()
p = password(root)
root.mainloop()