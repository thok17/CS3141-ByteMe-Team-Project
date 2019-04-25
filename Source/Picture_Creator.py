import PIL.Image
import random
from tkinter import *

pathsToTake = ["unnamed.png", "Scenic.jpg"]
numberOfPaths = 2

path = pathsToTake[random.randint(0, numberOfPaths - 1)]
pathTwo = pathsToTake[random.randint(0, numberOfPaths - 1)]
pathThree = pathsToTake[random.randint(0, numberOfPaths - 1)]
pathFour = pathsToTake[random.randint(0, numberOfPaths - 1)]

def open_image(given):
    newImage = PIL.Image.open(given)
    return newImage


def save_image(image, given):
    image.save(given, 'png')


def create_image(i, j):
    image = PIL.Image.new("RGB", (i, j), "white")
    return image


def get_pixel(image, i, j):
    width, height = image.size
    if i > width or j > height:
        return None

    pixel = image.getpixel((i, j))
    return pixel


def copy_four_corners(image, imageTwo, imageThree, imageFour):
    # Get size
    width, height = image.size
    newWidth = width
    newHeight = height
    newWidth //= 2
    newHeight //= 2
    # Create new Image and a Pixel Map
    newImage = create_image(width, height)
    pixels = newImage.load()
    # Copying pixel to the corners
    for i in range(newWidth):
        for j in range(newHeight):
            # Get Pixel
            pixel = get_pixel(image, i, j)

            # Get R, G, B values (This are int from 0 to 255)
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]

            pixels[i, j] = (red, green, blue)
    for i in range(newWidth):
        for j in range(newHeight):
            # Get Pixel
            pixel = get_pixel(imageTwo, newWidth + i, j)

            # Get R, G, B values (This are int from 0 to 255)
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]

            pixels[newWidth + i, j] = (red, green, blue)
    for i in range(newWidth):
        for j in range(newHeight):
            # Get Pixel
            pixel = get_pixel(imageThree, i, newHeight + j)

            # Get R, G, B values (This are int from 0 to 255)
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]

            pixels[i, newHeight + j] = (red, green, blue)
    for i in range(newWidth):
        for j in range(newHeight):
            # Get Pixel
            pixel = get_pixel(imageFour, newWidth + i, newHeight + j)

            # Get R, G, B values (This are int from 0 to 255)
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]

            pixels[newWidth + i, newHeight + j] = (red, green, blue)
    return newImage

newImage = copy_four_corners(open_image(path), open_image(pathTwo), open_image(pathThree), open_image(pathFour))
save_image(newImage, "newImage.png")

imageDisplay= Tk()
imageDisplay.title("Newly Created Image")
newImage=PhotoImage(file="newImage.png")
justTheImage = Label(imageDisplay, image=newImage, compound=TOP)
justTheImage.pack()
mainloop()

