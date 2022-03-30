from tkinter import *
import variables

def saveOptions():
    variables.csv_file_path = csvFilePath.get()
    variables.ID = int(startingID.get())
    variables.websiteLink = websiteLink.get()
    variables.image_file_path = imageFilePath.get()
    for i in range (0,9):
        variables.startPrice[i] = int(basePrice[i].get())
        variables.oversizeMarkup[i] = int(oversizeMarkup[i].get())
    print(variables.oversizeMarkup)
    mw.destroy()

def run():
    #Declaring Global Variables
    global startingID, websiteLink, csvFilePath, imageFilePath, basePrice, oversizeMarkup, mw

    mw = Toplevel()
    mw.geometry('450x800')
    mw.title('Advance Options')
    
    #All Texts
    Label(mw, text = "Advance Options", font = "none 12 bold").place(height = 25, width = 450)
    Label(mw, text = "Starting ID").grid(row = 0, column = 0, sticky = E, pady = (30,3))
    Label(mw, text = "Website Link").grid(row = 1, column = 0, sticky = E, pady = 3)
    Label(mw, text = "Tags").grid(row = 2, column = 0, sticky = E, pady = 3)
    Label(mw, text = "CSV File Path and name").grid(row = 3, column = 0, sticky = E, pady = 3)
    Label(mw, text = "Images File Path").grid(row = 4, column = 0, sticky = E, pady = 3)

    Label(mw, text = "Base Price", font = "none 12 bold").grid(row = 5, column = 0, sticky = E, pady = (7,3))
    Label(mw, text = "Round Neck Half Sleeves Tshirt",).grid(row = 6, column = 0, sticky = E, pady = 3)
    Label(mw, text = "Round Neck Full Sleeves Tshirt",).grid(row = 7, column = 0, sticky = E, pady = 3)
    Label(mw, text = "V Neck Half Sleeves Tshirt",).grid(row = 8, column = 0, sticky = E, pady = 3)
    Label(mw, text = "Raglan Tshirt",).grid(row = 9, column = 0, sticky = E, pady = 3)
    Label(mw, text = "Sweatshirt",).grid(row = 10, column = 0, sticky = E, pady = 3)
    Label(mw, text = "Hooded Sweatshirt",).grid(row = 11, column = 0, sticky = E, pady = 3)
    Label(mw, text = "Crop Top",).grid(row = 12, column = 0, sticky = E, pady = 3)
    Label(mw, text = "Crop Hoodies",).grid(row = 13, column = 0, sticky = E, pady = 3)
    Label(mw, text = "Long Top Full Sleeves T-Shirt",).grid(row = 14, column = 0, sticky = E, pady = 3)

    Label(mw, text = "Oversize Markup", font = "none 12 bold").grid(row = 15, column = 0, sticky = E, pady = (7,3))
    Label(mw, text = "Round Neck Half Sleeves Tshirt",).grid(row = 16, column = 0, sticky = E, pady = 3)
    Label(mw, text = "Round Neck Full Sleeves Tshirt",).grid(row = 17, column = 0, sticky = E, pady = 3)
    Label(mw, text = "V Neck Half Sleeves Tshirt",).grid(row = 18, column = 0, sticky = E, pady = 3)
    Label(mw, text = "Raglan Tshirt",).grid(row = 19, column = 0, sticky = E, pady = 3)
    Label(mw, text = "Sweatshirt",).grid(row = 20, column = 0, sticky = E, pady = 3)
    Label(mw, text = "Hooded Sweatshirt",).grid(row = 21, column = 0, sticky = E, pady = 3)
    Label(mw, text = "Crop Top",).grid(row = 22, column = 0, sticky = E, pady = 3)
    Label(mw, text = "Crop Hoodies",).grid(row = 23, column = 0, sticky = E, pady = 3)
    Label(mw, text = "Long Top Full Sleeves T-Shirt",).grid(row = 24, column = 0, sticky = E, pady = 3)
    
    #Input Field
    startingID = Entry(mw)
    startingID.grid(row = 0, column = 1, sticky = W, pady = (30,3))

    websiteLink = Entry(mw)
    websiteLink.grid (row = 1, column = 1, sticky = W, pady = 3)

    tags = Entry(mw)
    tags.grid (row = 2, column = 1, sticky = W, pady = 3)

    csvFilePath = Entry(mw)
    csvFilePath.grid (row = 3, column = 1, sticky = W, pady = 3)

    imageFilePath = Entry(mw)
    imageFilePath.grid (row = 4, column = 1, sticky = W, pady = 3)

    basePrice = [0] * 9 
    oversizeMarkup = [0]*9

    for i in range (0,9):
        basePrice[i] = Entry(mw)
        basePrice[i].grid (row = (i+6), column = 1, sticky = W, pady = 3)
    
    for i in range (0,9):
        oversizeMarkup[i] = Entry(mw)
        oversizeMarkup[i].grid (row = (i+16), column = 1, sticky = W, pady = 3)
    
    Button(mw, text = "Save and Close", command = lambda : saveOptions()) .grid (row = 25, column = 1, sticky = N, pady = 10)

    mw.mainloop()