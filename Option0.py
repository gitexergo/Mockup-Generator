from tkinter import *
import variables

def saveOptions():
    for i in range (0,26):
        variables.selectedColorOptions[0][i] = cb_color[i].get()
    for i in range (0,11):
        variables.selectedSizeOptions[0][i] = cb_size[i].get()
    mw.destroy()

def run():
    global mw
    mw = Toplevel()
    mw.geometry('450x450')

    #Title
    Label(mw, text ="Round Neck Half Sleeves Tshirt Options", font = "none 12 bold").place(height = 25, width = 450)
    #Select Colour
    Label(mw, text ="Select Colours", font = "none 10 bold").grid(row = 0, column = 0, pady = (55,0), sticky = W)
    
    #Local Variables
    global cb_size, cb_color
    cb_size = [IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar()]
    cb_color = [IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar()]
    #Checkbuttons Colours
    Checkbutton(mw, text = "Beige", variable = cb_color[0], onvalue = 1, offvalue = 0, font = "none 8 bold", fg = "green").grid(row = 1, column = 0, sticky = W)
    Checkbutton(mw, text = "Black", variable = cb_color[1], onvalue = 1, offvalue = 0, font = "none 8 bold", fg = "green").grid(row = 1, column = 1, sticky = W)
    Checkbutton(mw, text = "Bottle Green", variable = cb_color[2], onvalue = 1, offvalue = 0, font = "none 8 bold", fg = "green").grid(row = 1, column = 2, sticky = W)
    Checkbutton(mw, text = "Brick Red", variable = cb_color[3], onvalue = 1, offvalue = 0, font = "none 8 bold", fg = "green").grid(row = 1, column = 3, sticky = W)

    Checkbutton(mw, text = "Charcoal Melange", variable = cb_color[4], onvalue = 1, offvalue = 0, font = "none 8 bold", fg = "green").grid(row = 2, column = 0, sticky = W)
    Checkbutton(mw, text = "Coffee Brown", variable = cb_color[5], onvalue = 1, offvalue = 0, font = "none 8 bold", fg = "green").grid(row = 2, column = 1, sticky = W)
    Checkbutton(mw, text = "Flag Green", variable = cb_color[6], onvalue = 1, offvalue = 0, font = "none 8 bold", fg = "green").grid(row = 2, column = 2, sticky = W)
    Checkbutton(mw, text = "Golden Yellow", variable = cb_color[7], onvalue = 1, offvalue = 0, font = "none 8 bold", fg = "green").grid(row = 2, column = 3, sticky = W)

    Checkbutton(mw, text = "Grey Melange", variable = cb_color[8], onvalue = 1, offvalue = 0, font = "none 8 bold", fg = "green").grid(row = 3, column = 0, sticky = W)
    Checkbutton(mw, text = "Lavender", variable = cb_color[9], onvalue = 1, offvalue = 0, font = "none 8 bold", fg = "green").grid(row = 3, column = 1, sticky = W)
    Checkbutton(mw, text = "Light Baby Pink", variable = cb_color[10], onvalue = 1, offvalue = 0, font = "none 8 bold", fg = "green").grid(row = 3, column = 2, sticky = W)
    Checkbutton(mw, text = "Maroon", variable = cb_color[11], onvalue = 1, offvalue = 0, font = "none 8 bold", fg = "green").grid(row = 3, column = 3, sticky = W)
    
    Checkbutton(mw, text = "Mustard Yellow", variable = cb_color[12], onvalue = 1, offvalue = 0, font = "none 8 bold", fg = "green").grid(row = 4, column = 0, sticky = W)
    Checkbutton(mw, text = "Navy Blue", variable = cb_color[13], onvalue = 1, offvalue = 0, font = "none 8 bold", fg = "green").grid(row = 4, column = 1, sticky = W)
    Checkbutton(mw, text = "New Yellow", variable = cb_color[14], onvalue = 1, offvalue = 0, font = "none 8 bold", fg = "green").grid(row = 4, column = 2, sticky = W)
    Checkbutton(mw, text = "Olive Green", variable = cb_color[15], onvalue = 1, offvalue = 0, font = "none 8 bold", fg = "green").grid(row = 4, column = 3, sticky = W)

    Checkbutton(mw, text = "Orange", variable = cb_color[16], onvalue = 1, offvalue = 0, font = "none 8 bold", fg = "green").grid(row = 5, column = 0, sticky = W)
    Checkbutton(mw, text = "Petrol Blue", variable = cb_color[17], onvalue = 1, offvalue = 0, font = "none 8 bold", fg = "green").grid(row = 5, column = 1, sticky = W)
    Checkbutton(mw, text = "Pink", variable = cb_color[18], onvalue = 1, offvalue = 0).grid(row = 5, column = 2, sticky = W)
    Checkbutton(mw, text = "Purple", variable = cb_color[19], onvalue = 1, offvalue = 0, font = "none 8 bold", fg = "green").grid(row = 5, column = 3, sticky = W)

    Checkbutton(mw, text = "Red", variable = cb_color[20], onvalue = 1, offvalue = 0, font = "none 8 bold", fg = "green").grid(row = 6, column = 0, sticky = W)
    Checkbutton(mw, text = "Royal Blue", variable = cb_color[21], onvalue = 1, offvalue = 0, font = "none 8 bold", fg = "green").grid(row = 6, column = 1, sticky = W)
    Checkbutton(mw, text = "Sky Blue", variable = cb_color[22], onvalue = 1, offvalue = 0, font = "none 8 bold", fg = "green").grid(row = 6, column = 2, sticky = W)
    Checkbutton(mw, text = "Steel Grey", variable = cb_color[23], onvalue = 1, offvalue = 0, font = "none 8 bold", fg = "green").grid(row = 6, column = 3, sticky = W)
    
    Checkbutton(mw, text = "White", variable = cb_color[24], onvalue = 1, offvalue = 0, font = "none 8 bold", fg = "green").grid(row = 7, column = 0, sticky = W)
    Checkbutton(mw, text = "Yellow", variable = cb_color[25], onvalue = 1, offvalue = 0, font = "none 8 bold", fg = "green").grid(row = 7, column = 1, sticky = W)

    #Select Size
    Label(mw, text ="Select Size", font = "none 10 bold").grid(row = 8, column = 0, pady = (30,0), sticky = W)

    #Checkbutton Size
    Checkbutton(mw, text = "X-Small", variable = cb_size[0], onvalue = 1, offvalue = 0).grid(row = 9, column = 0, sticky = W)
    Checkbutton(mw, text = "Small", variable = cb_size[1], onvalue = 1, offvalue = 0, font = "none 8 bold", fg = "green").grid(row = 9, column = 1, sticky = W)
    Checkbutton(mw, text = "Medium", variable = cb_size[2], onvalue = 1, offvalue = 0, font = "none 8 bold", fg = "green").grid(row = 9, column = 2, sticky = W)
    Checkbutton(mw, text = "Large", variable = cb_size[3], onvalue = 1, offvalue = 0, font = "none 8 bold", fg = "green").grid(row = 9, column = 3, sticky = W)

    Checkbutton(mw, text = "X-Large", variable = cb_size[4], onvalue = 1, offvalue = 0, font = "none 8 bold", fg = "green").grid(row = 10, column = 0, sticky = W)
    Checkbutton(mw, text = "2X-Large", variable = cb_size[5], onvalue = 1, offvalue = 0, font = "none 8 bold", fg = "green").grid(row = 10, column = 1, sticky = W)
    Checkbutton(mw, text = "3X-Large", variable = cb_size[6], onvalue = 1, offvalue = 0, font = "none 8 bold", fg = "green").grid(row = 10, column = 2, sticky = W)
    Checkbutton(mw, text = "4X-Large", variable = cb_size[7], onvalue = 1, offvalue = 0, font = "none 8 bold", fg = "green").grid(row = 10, column = 3, sticky = W)

    Checkbutton(mw, text = "5X-Large", variable = cb_size[8], onvalue = 1, offvalue = 0, font = "none 8 bold", fg = "green").grid(row = 11, column = 0, sticky = W)
    Checkbutton(mw, text = "6X-Large", variable = cb_size[9], onvalue = 1, offvalue = 0, font = "none 8 bold", fg = "green").grid(row = 11, column = 1, sticky = W)
    Checkbutton(mw, text = "7X-Large", variable = cb_size[10], onvalue = 1, offvalue = 0, font = "none 8 bold", fg = "green").grid(row = 11, column = 2, sticky = W)

    Button (mw, text = "Save & Close",width = 10, command = saveOptions).grid(row = 12, column = 0, columnspan = 4, sticky = NS, pady = 30)


    mw.mainloop()