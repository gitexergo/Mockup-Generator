"""
Apparel Numbers
0. Round Neck Half Sleeves Tshirt
1. Round Neck Full Sleeves Tshirt
2. V Neck Half Sleeves Tshirt
3. Raglan Tshirt
4. Sweat Shirt
5. Hooded Sweat Shirt
6. Crop Tops
7. Crop Hoodies
8. Long Top T-Shirt

Size
XS, S, M, L, XL, 2XL, 3XL, 4XL, 5XL, 6XL, 7XL = 11

Color
Beige - 0
Black - 1
Bottle Green - 2
Brick Red - 3
Charcoal Melange - 4
Coffee Brown - 5
Flag Green - 6
Golden Yellow -7
Grey Melange -8
Lavender - 9
Light Baby Pink - 10
Maroon - 11
Mustard Yellow - 12
Navy Blue - 13
New Yellow - 14
Olive Green - 15
Orange - 16 
Petrol Blue - 17
Pink - 18
Purple - 19
Red - 20
Royal Blue - 21
Sky Blue - 22
Steel Grey - 23
White - 24
Yellow - 25

"""

#Option Selected
selectedColorOptions = [[0 for i in range (0,26)] for j in range (0,9)]
selectedSizeOptions = [[0 for i in range (0,11)] for j in range (0,9)]

#Apparel Selected
app_sel = [0] * 9

#CSV File Name and Path
csv_file_path = "D:/csv_file.csv"

#Image File Path
image_file_path = "D:/New folder"

#Starting ID for CSV
ID = 10

#Design Code
designCode = "Default Name"

#Design Name
designName = "D01"

#Product Discription
designDiscription = "Default Discription"

#Print Size
printSizeL = 14
printSizeH = 18

#Website Link
websiteLink = "www.t-dog.xyz"

#Images Name
imageName = [[0 for i in range (0,26)] for j in range (0,9)] #9 Apparels, 26 Colours

#Tags
tags = "Default, Tags"

#Colour Options
colorOptions = ["Beige","Black","Bottle Green","Brick Red","Charcoal Melange","Coffee Brown","Flag Green","Golden Yellow","Grey Melange","Lavender","Light Baby Pink","Maroon",
                "Mustard Yellow","Navy Blue","New Yellow","Olive Green","Orange","Petrol Blue","Pink","Purple","Red","Royal Blue","Sky Blue","Steel Grey","White","Yellow"]

#Size Options
sizeOptions = ["X-Small","Small","Medium","Large","X-Large","2X-Large","3X-Large","4X-Large","5X-Large","6X-Large","7X-Large"]

#Categories
Categories = ["Round Neck Half Sleeves Tshirt", "Round Neck Full Sleeves Tshirt", "V Neck Half Sleeves Tshirt", "Raglan Tshirt", "Sweatshirt", "Hooded Sweatshirt", "Crop Tops", "Crop Hoodies", "Long Top TShirt"]

#Start Price - Per Size, array for product 0 to 8
startPrice = [450, 500, 470, 480, 550, 600, 400, 550, 450]

#Oversize MarkUp - Per Size, array for product 0 to 8
oversizeMarkup = [20,20,20,20,30,40,20,40,30]

#SKU Terminology
sku_prefix = ["MRnHs", "MRnFs", "MVnHs", "MRgFs", "USs", "UHd", "FCpTp", "FCpHd", "FLtFs"]
sku_color = ["Be","Bk","Gn","BRd","Cm","bn","Fgn","GYI","Gm","Lv","LBp","Mn","MYl","Nb","NYl","OG","or","pb","Pk","Pu","Rd","Rb","Sb","SG","Wh","Yl"]
sku_color2 = ["Be","WhBk","Gn","BRd","BkCm","bn","Fgn","GYI","Gm","Lv","LBp","Mn","MYl","Nb","NYl","OG","or","pb","Pk","Pu","Rd","Rb","Sb","SG","BkWh","Yl"] #Made for Raglan Color Codes - Black(2), Black Charcoal Melange(5), White (25)
sku_size = ["XS", "S", "M", "L", "XL", "XXL", "3XL", "4XL", "5XL", "6XL", "7XL"]
sku_printpos = ["Fr", "Bk","Lp","Rp"] #Front, Back, Left Pocket, Right Pocket

#Inventory Weight Based on Product Type and Size
invWeight = [[0 for i in range (0,11)] for j in range (0,9)]

#Design File Name
filename ="D:/default.png"

#Print Position
printPos = 0

#Additional Categories
productCategory = "Default Category"

#Export Options
imgH = 1920
imgQ = 100