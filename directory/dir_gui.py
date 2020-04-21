
from tkinter import *
import tkinter as tk
from tkinter import filedialog



def browse_button(self):
            filename = filedialog.askdirectory()
            
            self.txt_field.insert(1, filename)
            print(filename)


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(300,150)
        self.master.maxsize(300,150)

        self.lbl_browse = tk.Label(self.master,text="Browse...")
        self.lbl_browse.grid(row=0,column=0,padx=(20,0),pady=(20,0),sticky=N+W)

        self.txt_field = tk.Entry(self.master)
        self.txt_field.grid(row=0,column=1,columnspan=2,rowspan=1,padx=(10,0),pady=(20,0),sticky=N+E+W)

        self.btn_browse = tk.Button(self.master,width=12,height=2,text="Open Directory",command=lambda: browse_button(self))
        self.btn_browse.grid(row=1,column=0,padx=(20,0),pady=(40,0),sticky=W)


        















if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
