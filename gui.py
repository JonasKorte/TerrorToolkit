import core.terror as terror
import tkinter as tk
from tkinter import ttk

def initializeWindow():
    gui = tk.Tk()
    gui.title("TerrorToolkit")

    return gui

def setupWidgets():
    pass

def main():
    gui = initializeWindow()

    setupWidgets()

    gui.mainloop()

if __name__ == '__main__':
    main()