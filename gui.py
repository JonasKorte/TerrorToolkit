import core.terror as terror
import tkinter as tk
from tkinter import ttk

def initializeWindow():
    gui = tk.Tk()
    gui.title("TerrorToolkit")

    return gui

def TestButton():
    terror.executeModule("terrortest")

def setupWidgets(gui):
    testButton = ttk.Button(master = gui, text = "Test Me!", command = TestButton)
    testButton.pack()

def main():
    terror.scanModules()

    gui = initializeWindow()

    setupWidgets(gui)

    gui.mainloop()

if __name__ == '__main__':
    main()