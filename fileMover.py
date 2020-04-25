
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os
import sqlite3
import shutil


def CreateDb(self):
    conn=sqlite3.connect('txtMover.db')
    cur=conn.cursor()
    with conn:
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtFound( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_txt TEXT, \
            col_time INT);")
    addToDb(self)
    conn.commit()

def addToDb(self):
    folder = self.txt_sourceCode.get()
    for file in os.listdir(folder):
        filename = os.fsdecode(file)
        if filename.endswith('.txt'):
            print(os.path.getmtime(os.path.join(folder, filename)), os.path.join(folder, filename))
            text = os.path.join(folder, filename)
            time = int(os.path.getmtime(os.path.join(folder, filename)))
            conn=sqlite3.connect('txtMover.db')
            cur=conn.cursor()
            with conn:
                cur.execute("INSERT INTO tbl_txtFound(col_time, col_txt) VALUES (?, ?)", \
                            (time, text,))  
            continue
        else:
            continue


def findTxt(self):
    CreateDb(self)
    folder = self.txt_sourceCode.get()
    for file in os.listdir(folder):
        filename = os.fsdecode(file)
        if filename.endswith('.txt'):
            print(os.path.getmtime(os.path.join(folder, filename)), os.path.join(folder, filename))
            text = os.path.join(folder, filename)
            time = int(os.path.getmtime(os.path.join(folder, filename)))
            shutil.move(text, self.txt_destinyCode.get())
            continue
        else:
            continue
    


def browse_button1(self):
            filename = filedialog.askdirectory()  
            self.txt_sourceCode.insert(1, filename)
            print(filename)

def browse_button2(self):
            filename = filedialog.askdirectory()
            self.txt_destinyCode.insert(1, filename)
            print(filename)
            

class ParentWindow(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)

        self.master = master
        self.master.minsize(400,200)
        self.master.maxsize(400,200)

        self.lbl_source = tk.Label(self.master,text="Source Directory:")
        self.lbl_source.grid(row=0,column=0,padx=(20,0),pady=(25,0),sticky=N+W)
        self.lbl_destiny = tk.Label(self.master,text="Final Directory:")
        self.lbl_destiny.grid(row=1,column=0,padx=(20,0),pady=(18,0),sticky=N+W)

        self.txt_sourceCode = tk.Entry(self.master, text='' )
        self.txt_sourceCode.grid(row=0,column=1,columnspan=2,padx=(8,0),pady=(25,0),sticky=N+E+W)
        self.txt_destinyCode = tk.Entry(self.master, text='' )
        self.txt_destinyCode.grid(row=1,column=1,columnspan=2,padx=(8,0),pady=(18,0),sticky=N+E+W)

        self.btn_browseSource = tk.Button(self.master,width=12,height=1,text="Browse...", command=lambda:browse_button1(self))
        self.btn_browseSource.grid(row=0,column=4,padx=(40,0),pady=(23,0),sticky=E)
        self.btn_browseDestiny = tk.Button(self.master,width=12,height=1,text="Browse...", command=lambda:browse_button2(self))
        self.btn_browseDestiny.grid(row=1,column=4,padx=(40,0),pady=(15,0),sticky=E)
        self.btn_execute = tk.Button(self.master,width=12,height=2,text="Move Files",command=lambda:findTxt(self))
        self.btn_execute.grid(row=2,column=0,padx=(20,0),pady=(40,0),sticky=S+W)












if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
