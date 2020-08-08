#Generate a random minimalist cat drawing with random colored furr and background

from PIL import Image as img
import random

#Choose the base cat
number = str(random.randint(1,3))
catPicture = r"C:\Users\Ulysse\Desktop\Code\chapy/" + "cat" + number +".png"



#Load base cat image and create a new one (use the r before the string to stop the antislash)
baseCat = img.open(catPicture)
length, height = baseCat.size

newCat = img.new("RGB",(length, height))

#Create the new color (first bg, and then cat)
newBackgroundColor = (random.randint(110,255),random.randint(110,255),random.randint(110,255))
newCatColor = (random.randint(110,255),random.randint(110,255),random.randint(110,255))

print(newBackgroundColor, newCatColor)

for y in range(height):
    for x in range(length):
        pixel = baseCat.getpixel((x,y))
        
        #Check if it's the background (green), if so, you replace it with the new color
        if pixel[1] == 255:
            newCat.putpixel((x,y), newBackgroundColor)
            
        #Check if it's the cat (red), if so, you replace it with the new color
        elif pixel[0] == 254:
            newCat.putpixel((x,y), newCatColor)

newCat.save("NewCat.png")
print("Done!")