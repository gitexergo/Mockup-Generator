import csv
import variables

#SKU Generator
def SkuGen(pre, color, size, position):
    val = ""
    if pre != 3:
        val = variables.sku_prefix[pre] + "-" + variables.sku_color[color] + "-" + variables.sku_size[size] + "-" + variables.designCode + "-" + variables.sku_printpos[position]
    else:
        val = variables.sku_prefix[pre] + "-" + variables.sku_color2[color] + "-" + variables.sku_size[size] + "-" + variables.designCode + "-" + variables.sku_printpos[position]
    return val

#Price Calculator
def priceCalc(pro, size):
    baseprice = variables.startPrice[pro]
    pricejump = variables.oversizeMarkup[pro]
    finalprice = baseprice
    if size > 5:
        finalprice = baseprice + (pricejump *(size-5))
    return finalprice

#All Selected Attributes for colour
def Attribute1Value(n):
    val = ""
    for i in range (0, len(variables.selectedColorOptions[n])):
        if variables.selectedColorOptions[n][i] == 1:
            val = val + variables.colorOptions[i] +", "
    val = val[:len(val)-2] #Removing last ', ' from the string
    return val

def Attribute2Value(n):
    val = ""
    for i in range (0, len(variables.selectedSizeOptions[n])):
        if variables.selectedSizeOptions[n][i] == 1:
            val = val + variables.sizeOptions[i] + ", "
    val = val[:len(val)-2] #Removing last ', ' from the string
    return val

def VariationLineWriter(n, id):
    tempid = id
    for i in range (0, len(variables.selectedColorOptions[n])):
        if variables.selectedColorOptions[n][i] == 1:
            image = "https://" + variables.websiteLink + "/wp-content/uploads/" + variables.imageName[n][i]
            for j in range (0,len(variables.selectedSizeOptions[n])):
                if variables.selectedSizeOptions[n][j] == 1:
                    tempid += 1
                    line = [tempid,"variation", SkuGen(n,i,j,variables.printPos), variables.designName + " - " + variables.Categories[n], 1, "visible", "",
                            "taxable","parent",1, variables.invWeight[n][j], 0, priceCalc(n, j),"", "", image, "id:" + str(id),"Colour",
                            variables.colorOptions[i],"",1,"Size",variables.sizeOptions[j],"",1]
                    writer.writerow(line)
    return tempid + 1

def run():
    #Creating CSV File
    global f, writer
    f = open(variables.csv_file_path,'w', newline='')
    #Creating CSV Writer
    writer = csv.writer(f)
    #Header writing
    header = ["ID","Type","SKU","Name","Published","Visibility in catalog","Description","Tax status","Tax class","In stock?","Weight (kg)",
              "Allow customer reviews?","Regular price","Categories","Tags","Images","Parent","Attribute 1 name","Attribute 1 value(s)",
              "Attribute 1 visible","Attribute 1 global","Attribute 2 name","Attribute 2 value(s)","Attribute 2 visible","Attribute 2 global"]
    writer.writerow(header)
    row = []
    tempID = variables.ID
    
    for i in range (0,len(variables.app_sel)):
        if variables.app_sel[i]:
            row = [tempID,"variable",variables.sku_prefix[i] + "-" + variables.designCode,variables.designName + " - " + variables.Categories[i], 1, "visible", variables.designDiscription, "taxable","",1,"",1,"",
                    variables.Categories[i], variables.tags, "https://"+variables.websiteLink+"/wp-content/uploads/"+variables.imageName[i][variables.selectedColorOptions[i].index(1)], "", "Colour", Attribute1Value(i),
                    1, 1,"Size", Attribute2Value(i), 1, 1]
            writer.writerow(row)
            tempID = VariationLineWriter(i, tempID)
            

    f.close()