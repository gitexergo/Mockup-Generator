from tkinter import *
from tkinter import filedialog

#Option Windows
import Option0
import Option1
import Option2
import Option3
import Option4
import Option5
import Option6
import Option7
import Option8
import ExportOptions
import AdvanceOptions
import runPS

#Global Variable
import variables

#CSV Program
import WriteCSV

#Program to browse files
def browseFiles():
    variables.filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File")

#Program to Save Values
def saveOptions():
    variables.designName = designName.get()
    variables.designCode = designCode.get()
    variables.designDiscription = designDiscription.get(1.0,END)
    variables.printSizeL = printSizeL.get()
    variables.printSizeH = printSizeH.get()
    variables.printPos = options.index(clicked.get())
    variables.productCategory = productCategory.get()
    imageNameGen()
    btn_advOptions['state'] = NORMAL

#Advance Options
def advanceOptions():
    btn_csv['state'] = NORMAL
    AdvanceOptions.run()

#Generate CSV File
def generateCSV():
    btn_exportoptions['state'] = NORMAL
    WriteCSV.run()

#Export Options
def exportOptions():
    btn_run['state'] = NORMAL
    ExportOptions.run()

#Program to check and change state of option buttons
def stateCheck(num):
    variables.app_sel[num] = cb_state[num].get()
    if cb_state[num].get() == 0:
        btn[num]['state'] = DISABLED
        btn[num].configure(text = "Please select to see options")
    elif cb_state[num].get() == 1:
        btn[num]['state'] = NORMAL
        btn[num].configure(text = "Options")
    else:
        btn[num].configure(text = "Something went wrong")

#Image Name Generator
def imageNameGen():
    for i in range (0,9):
        for j in range (0,26):
            if i != 3:
                variables.imageName[i][j] = variables.sku_prefix[i]+ '-' + variables.sku_color[j] + '-' + variables.designCode + '-' + variables.sku_printpos[variables.printPos] + '.jpg'
            elif i == 3:
                variables.imageName[i][j] = variables.sku_prefix[i]+ '-' + variables.sku_color2[j] + '-' + variables.designCode + variables.sku_printpos[variables.printPos] + '.jpg'

mw = Tk()
mw.title ("Apparel Mock-Up Generator by Exergo")
mw. geometry ('600x850')

#All Text Fields
Label(mw,text='Apparel Mock-Up Generator by Exergo', font="none 16 bold") .place(height = 30, width = 600)

Label(mw,text='Design Name :').grid(row=2,column=0, sticky = E,pady=(50,0))
Label(mw,text='Design Code :').grid(row=3,column=0, sticky = E)
Label(mw,text='Design File :').grid(row=4,column=0, sticky = E)
Label(mw,text='Print Size (l) :').grid(row=5,column=0, sticky = E)
Label(mw,text='Print Size (w) :').grid(row=6,column=0, sticky = E)
Label(mw,text='Design Discription :').grid(row=7,column=0, sticky = E)
Label(mw,text='Print Position :').grid(row=8,column=0, sticky = E)
Label(mw,text='Category :').grid(row=9,column=0, sticky = E)
Label(mw,text=' ').grid(row=10,column=0, sticky = E)
Label(mw,text='Apparels to print on', font ="none 12 bold").grid(row=11,column=1, sticky = W)

#Options and storage for dropdown (print position)
options = [
    "Front",
    "Back",
    "Left Pocket",
    "Right Pocket"
]
clicked = StringVar(mw,"Front")

#Input Fields for first Half
designName = Entry(mw)
designName.grid(row=2,column =1, sticky = W, pady=(50,3))

designCode = Entry(mw)
designCode.grid(row=3, column=1, sticky = W, pady=3)

designFile = Button(mw, text ="Browse Files", command = browseFiles)
designFile.grid(row=4, column=1, sticky = W, pady=3)

printSizeL = Entry(mw)
printSizeL.grid(row=5, column=1, sticky = W, pady=3)

printSizeH = Entry(mw)
printSizeH.grid(row=6, column=1, sticky = W, pady=3)

designDiscription = Text(mw, height=5, width = 30)
designDiscription.grid(row=7, column=1, sticky = W, pady=3)

printPosition = OptionMenu(mw, clicked , *options )
printPosition.grid(row=8, column=1, sticky = W, pady=3)

productCategory = Entry(mw)
productCategory.grid(row=9, column=1, sticky = W, pady=3)

#Checkbox for second half
"""
0. Round Neck Half Sleeves Tshirt
1. Round Neck Full Sleeves Tshirt
2. V Neck Half Sleeves Tshirt
3. Raglan Tshirt
4. Sweat Shirt
5. Hooded Sweat Shirt
6. Crop Tops
7. Crop Hoodies
8. Long Top T-Shirt
"""
cb_state = [IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar()]
check = [0,0,0,0,0,0,0,0,0]
btn = [0,0,0,0,0,0,0,0,0]

btn[0] = Button (mw, text = "Please select to see options", state = DISABLED, command = lambda: Option0.run())
check[0] = Checkbutton (mw, text = "Round Neck Half Sleeves Tshirt", variable = cb_state[0], onvalue = 1, offvalue = 0, command = lambda : stateCheck(0))
check[0].grid(row = 12, column =1, sticky = W)
btn[0].grid (row=12, column = 2, sticky = W, pady = 1)

btn[1] = Button (mw, text = "Please select to see options", state = DISABLED, command = lambda: Option1.run())
check[1] = Checkbutton (mw, text = "Round Neck Full Sleeves Tshirt", variable = cb_state[1], onvalue = 1, offvalue = 0, command = lambda : stateCheck(1))
check[1].grid(row = 13, column =1, sticky = W)
btn[1].grid (row=13, column = 2, sticky = W, pady = 1)

btn[2] = Button (mw, text = "Please select to see options", state = DISABLED, command = lambda: Option2.run())
check[2] = Checkbutton (mw, text = "V Neck Half Sleeves Tshirt", variable = cb_state[2], onvalue = 1, offvalue = 0, command = lambda : stateCheck(2))
check[2].grid(row = 14, column =1, sticky = W)
btn[2].grid (row=14, column = 2, sticky = W, pady = 1)

btn[3] = Button (mw, text = "Please select to see options", state = DISABLED, command = lambda: Option3.run())
check[3] = Checkbutton (mw, text = "Raglan Tshirt", variable = cb_state[3], onvalue = 1, offvalue = 0, command = lambda : stateCheck(3))
check[3].grid(row = 15, column =1, sticky = W)
btn[3].grid (row=15, column = 2, sticky = W, pady = 1)

btn[4] = Button (mw, text = "Please select to see options", state = DISABLED, command = lambda: Option4.run())
check[4] = Checkbutton (mw, text = "Sweatshirt", variable = cb_state[4], onvalue = 1, offvalue = 0, command = lambda : stateCheck(4))
check[4].grid(row = 16, column =1, sticky = W)
btn[4].grid (row=16, column = 2, sticky = W, pady = 1)

btn[5] = Button (mw, text = "Please select to see options", state = DISABLED, command = lambda: Option5.run())
check[5] = Checkbutton (mw, text = "Hooded Sweatshirt", variable = cb_state[5], onvalue = 1, offvalue = 0, command = lambda : stateCheck(5))
check[5].grid(row = 17, column =1, sticky = W)
btn[5].grid (row=17, column = 2, sticky = W, pady = 1)

btn[6] = Button (mw, text = "Please select to see options", state = DISABLED, command = lambda: Option6.run())
check[6] = Checkbutton (mw, text = "Crop Tops", variable = cb_state[6], onvalue = 1, offvalue = 0, command = lambda : stateCheck(6))
check[6].grid(row = 18, column =1, sticky = W)
btn[6].grid (row=18, column = 2, sticky = W, pady = 1)

btn[7] = Button (mw, text = "Please select to see options", state = DISABLED, command = lambda: Option7.run())
check[7] = Checkbutton (mw, text = "Crop Hoodies", variable = cb_state[7], onvalue = 1, offvalue = 0, command = lambda : stateCheck(7))
check[7].grid(row = 19, column = 1, sticky = W)
btn[7].grid (row = 19, column = 2, sticky = W, pady = 1)

btn[8] = Button (mw, text = "Please select to see options", state = DISABLED, command = lambda: Option8.run())
check[8] = Checkbutton (mw, text = "Long Top T-Shirt", variable = cb_state[8], onvalue = 1, offvalue = 0, command = lambda : stateCheck(8))
check[8].grid(row = 20, column = 1, sticky = W)
btn[8].grid (row = 20, column = 2, sticky = W, pady = 1)

#Export options and execute button
btn_saveOptions = Button (mw, text = "Save Details", command = lambda: saveOptions())
btn_saveOptions.grid (row = 21, column = 0, columnspan = 3, sticky = N, pady = (20,2))

btn_advOptions = Button (mw, text = "Advance Options", state = DISABLED, command = lambda: advanceOptions())
btn_advOptions.grid (row = 22, column = 0, columnspan = 3, sticky = N, pady = 2)

btn_csv = Button (mw, text = "Generate CSV", state = DISABLED, command = lambda: generateCSV())
btn_csv.grid (row = 23, column = 0, columnspan = 3, sticky = N, pady = 2)

btn_exportoptions = Button (mw, text = "Export Options", state = DISABLED, command = lambda: exportOptions())
btn_exportoptions.grid (row = 24, column = 0, columnspan = 3, sticky = N, pady = 2)

btn_run = Button (mw, text = "Create Mock-Ups", state = DISABLED, command = lambda: runPS.run())
btn_run.grid (row = 25, column = 0, columnspan = 3, sticky = N, pady = 2)

mw.mainloop()