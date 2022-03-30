import win32com.client
import os
import variables
import shutil

def mockupgen(n):
    doc_mockup = psApp.Open("D:/PS Files/product"+str(n)+".psd")
    psApp.activeDocument = doc_design
    doc_design.Save()

    psApp.activeDocument = doc_mockup
    doc_mockup.ResizeImage(Width = variables.imgH * 0.75, Height = variables.imgH)

    for i in range (0,26):
        if variables.selectedColorOptions[n][i]:
            colorLayer = doc_mockup.ArtLayers["color"+str(i)]
            colorLayer.visible = True
            exportFile = variables.image_file_path +'/'+ variables.imageName[n][i]
            doc_mockup.Export(ExportIn = exportFile, ExportAs = 2, Options = options)
            colorLayer.visible = False

    doc_mockup.Close(2)


def run():
    global psApp, doc_design, options
    psApp = win32com.client.Dispatch("Photoshop.Application")
    options = win32com.client.Dispatch('Photoshop.ExportOptionsSaveForWeb')

    options.Format = 6
    options.Quality = variables.imgQ
    
    try:
        os.remove('D:/PS Files/design.png')
    except:
        pass

    copyFileName = 'D:/PS Files/design.png'
    shutil.copyfile(variables.filename,copyFileName)

    doc_design = psApp.Open(copyFileName)

    for i in range (0,9):
        if variables.app_sel[i]:
            mockupgen(i)

    doc_design.Close(2)
