from PIL import Image

#1) Read and Display
img = Image.open("tree.jpg")
img.show()

#2) Details: Format, Mode, Size
print("Format:", img.format)  
print("Mode:", img.mode)      
print("Size:", img.size)      

#3) Changing the type
img.save("tree.jpg")

#4) Resize image 
new_img = img.resize((300, 200))
new_img.show()
new_img.save("resized.png")

#5) Crop image 
cropped = img.crop((50, 50, 200, 200))  
cropped.show()
cropped.save("cropped.png")

#6) Rotate image 
rotated = img.rotate(90)
rotated.show()
rotated.save("rotated.png")

#7) Mirror image
mirror = img.transpose(Image.FLIP_LEFT_RIGHT)
mirror.show()
mirror.save("mirror.png")

#8) Flip image 
flipped = img.transpose(Image.FLIP_TOP_BOTTOM)
flipped.show()
flipped.save("flipped.png")
