from tkinter import *
import variables
from tkinter import filedialog

def selectFolder():
    variables.image_file_path = filedialog.askdirectory()

def saveOptions():
    variables.imgH = b_exportHeight.get()
    variables.imgQ = b_exportQuality.get()
    mw.destroy()

def run():
    global mw, b_exportHeight, b_exportQuality
    mw = Toplevel()
    mw.geometry('260x450')
    mw.title('Export Options')

    #Labels
    Label(mw, text = "Export Options", font = "none 12 bold").grid(row = 0, column = 0, columnspan = 2, sticky = N, pady = 10)
    Label(mw, text = "Export Height (px)").grid(row = 1, column = 0, sticky = E, pady = 3)
    Label(mw, text = "Export Quality (0 to 100)").grid(row = 2, column = 0, sticky = E, pady = 3)
    Label(mw, text = "Export Location").grid(row = 3, column = 0, sticky = E, pady = 3)

    #Input Fields
    btn = []

    b_exportHeight = Entry (mw)
    b_exportHeight.grid(row = 1, column = 1, sticky = W, pady = 3)

    b_exportQuality = Entry (mw)
    b_exportQuality.grid(row = 2, column = 1, sticky = W, pady = 3)

    Button (mw, text = "Select Folder", command = lambda : selectFolder()).grid(row = 3, column = 1, sticky = W, pady = 3)

    Button (mw, text = "Save and Close", command = lambda: saveOptions()).grid(row = 4, column = 0, columnspan = 2, sticky = N, pady = 10)
    mw.mainloop()