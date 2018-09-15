# -*- coding: utf-8 -*-
 
from tkinter import *
from gui import Ui_MainWindow

MainWindow = Tk()
MainWindow.geometry("377x657")
MainWindow.resizable(width=False,height=False)
MainWindow.title("PY Calculator v1.2")
try:
	MainWindow.iconbitmap(default='logo.ico')
except:
	pass
app = Ui_MainWindow(MainWindow)
app.mainloop()