

from tkinter import *
import tkinter as tk

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # master frame config
        self.master = master
        self.master.minsize(400,150)
        self.master.maxsize(400,150)
        self.master.title("Check Files")

        self.btn_browse1 = tk.Button(self.master, width=12, height=1, text="Browse...")
        self.btn_browse1.grid(row=1, column=0, rowspan=1, padx=(10,0), pady=(25,0), sticky=W)
        self.btn_browse2 = tk.Button(self.master, width=12, height=1, text="Browse...")
        self.btn_browse2.grid(row=2, column=0, rowspan=1, padx=(10,0), pady=(10,0), sticky=W)
        self.btn_check = tk.Button(self.master, width=12, height=2, text="Check for files...")
        self.btn_check.grid(row=3, column=0, rowspan=1, padx=(10,0), pady=(10,0), sticky=W)
        self.btn_closeApp = tk.Button(self.master, width=12, height=2, text="Close Program")
        self.btn_closeApp.grid(row=3, column=4, rowspan=1, padx=(180,0), pady=(10,0), sticky=E)

        self.txt_browse1 = tk.Entry(self.master, text='')
        self.txt_browse1.grid(row=1, column=2, rowspan=1, columnspan=3, padx=(20,0), pady=(25,0), sticky=N+E+W)
        self.txt_browse1 = tk.Entry(self.master, text='')
        self.txt_browse1.grid(row=2, column=2, rowspan=1, columnspan=3, padx=(20,0), pady=(10,0), sticky=N+E+W)





if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
