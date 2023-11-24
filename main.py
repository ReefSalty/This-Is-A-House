from PIL import Image, ImageDraw, ImageFont

Green1 = '#dada3b'
Green2 = '#9dbc29'
Yellow1 = '#ffdd54'
Yellow2 = '#ffb454'
Red1 = '#ff405c'
Red2 = '#e20059'
White1 = '#fff2de'
White2 = '#fde4c3'
Brown = '#a34f3e'
Brown2 = '#c86e59'
Clear = '#c8ffff'
Black = '#000000'

img = Image.new('RGB', (1024, 1024), color='#ffffff')
draw = ImageDraw.Draw(img)

#Sun
draw.ellipse(xy=(760, 100, 994, 335), fill=Yellow2)
draw.pieslice((760, 100, 994, 335), start=90, end=270, fill=Yellow1)

#Grass
draw.rounded_rectangle(xy=(50, 924, 974, 974), radius=20, fill=Green2)
draw.rounded_rectangle(xy=(50, 924, 512, 974), radius=20, fill=Green1)
draw.rectangle(xy=(500, 725, 512, 974), fill=Green1)

#Tree Big
draw.ellipse(xy=(300, 100, 700, 550), fill=Green2)
draw.pieslice(xy=(300, 100, 700, 550), start=90, end=270, fill=Green1)
draw.rounded_rectangle(xy=(300, 300, 500, 650), radius=20, fill=Green1)
draw.rectangle(xy=(500, 300, 700, 650), fill=Green2)

draw.line(xy=(425, 345, 500, 400), fill=Brown2, width=50)
draw.ellipse(xy=(405, 325, 455, 371), fill=Brown2)

draw.ellipse(xy=(475, 275, 525, 325), fill=Brown)
draw.pieslice(xy=(475, 275, 525, 325), fill=Brown2, start=90, end=270)
draw.rectangle(xy=(475, 305, 525, 750), fill=Brown2)
draw.rectangle(xy=(500, 305, 525, 750), fill=Brown)

#Tree - Left
draw.rectangle(xy=(206, 600, 250, 925), fill=Brown)
draw.rectangle(xy=(206, 600, 227, 925), fill=Brown2)

draw.ellipse(xy=(155, 250, 310, 700), fill=Green2)
draw.pieslice((154, 250, 310, 700), start=90, end=270, fill=Green1)

draw.ellipse(xy=(136, 300, 325, 750), fill=Green2)
draw.pieslice((135, 300, 325, 750), start=90, end=270, fill=Green1)

draw.ellipse(xy=(114, 350, 345, 800), fill=Green2)
draw.pieslice((113, 350, 345, 800), start=90, end=270, fill=Green1)

draw.ellipse(xy=(94, 400, 360, 850), fill=Green2)
draw.pieslice((94, 400, 360, 850), start=90, end=270, fill=Green1)

#House
draw.rectangle(xy=(350, 625, 923, 923), fill=White1)
draw.rectangle(xy=(637, 625, 923, 923), fill=White2)
draw.polygon(xy=(350, 625, 637, 375, 923, 625), fill=White1)
draw.polygon(xy=(637, 625, 637, 375, 920, 625), fill=White2)

#Door
draw.rounded_rectangle(xy=(417, 675, 570, 923), fill=Brown, radius=20)
draw.rectangle(xy=(417, 900, 570, 923), fill=Brown)

#Window
draw.rounded_rectangle(xy=(694, 675, 859, 840), fill=Brown, radius=20)
draw.rectangle(xy=(743, 724, 810, 791), fill=Clear)

#roof
draw.rounded_rectangle(xy=(825, 400, 870, 575), fill=Red1, radius=20)

draw.line(xy=(620, 380, 943, 625), fill=Red2, width=55)
draw.line(xy=(330, 625, 650, 380), fill=Red1, width=55)

draw.polygon(xy=(635, 360, 680, 415, 635, 425), fill=Red2)

draw.ellipse(xy=(310, 595, 360, 650), fill=Red1)
draw.ellipse(xy=(915, 595, 963, 650), fill=Red2)

draw.ellipse(xy=(605, 361, 670, 420), fill=Red2)
draw.pieslice(xy=(605, 361, 670, 420), start=90, end=270, fill=Red1)

#Text
font = ImageFont.truetype("Gidole-Regular.ttf", size=50)
draw.text((850, 950), 'Reef', fill=Black, font=font)
img.save('ThisIsAHouse.png')
