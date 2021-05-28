#Name: Ahmed Eldeib


from PIL import Image

location= str(input("What's the image location?"))

#The location should be sth like "A:\project\myimage.jpg"
image = Image.open(location)

#Get the original dimensions of the image
width, height = image.size
print("The Original dimensions:",width,",",height)

#Resize the dimensions of the image by half 
image=image.resize((width//2,height//2))

#Get the new dimensions of the image
width, height = image.size

print("The New dimensions:",width,",",height)

#Convert the image to RBG
RGB_Image = image.convert('RGB')

RGB_Image=RGB_Image.rotate(180)
RGB_Image.save('TheNewImage.jpg',"JPEG")