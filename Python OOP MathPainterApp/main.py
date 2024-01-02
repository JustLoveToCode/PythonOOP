from PIL import Image
import numpy as np


class Canvas:
    def __init__(self, height, width, color):
        self.color = color
        self.height = height
        self.width = width
        #  Create the 3D Numpy Array of the Zeros:
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # Change the [0,0,0] with the User Given Color
        self.data[:] = self.color

    def make(self, imagepath):
        # Convert the Current Array into the Image file:
        # Change the Slice of the Array with the New Values:
        img = Image.fromarray(self.data, "RGB")
        img.save(imagepath)


class Rectangle:
    # Rectangle Shape that can be drawn on the Canvas Object:
    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color

    def draw(self, canvas):
        # Draw itself into the Canvas:
        canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.color


class Square:
    def __init__(self, x, y, side, color):
        self.color = color
        self.x = x
        self.y = y
        self.side = side

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color


canvas_width = int(input("Enter the Canvas Width:"))
canvas_height = int(input("Enter the Canvas Height:"))

# Creating and Accessing the Dictionary:
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
# To access the Dictionary, it will be colors['white']
canvas_color = input("Enter the Canvas Color, it can be either white or black")

# Create the Canvas with the User Data:
canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])
canvas.make('canvas.png')
while True:
    shape_type = input("Do you like to draw Square or Rectangle? Press q to quit the Program").lower()
    if shape_type.lower() == 'rectangle':
        rec_x = int(input("Enter the x of the Rectangle"))
        rec_y = int(input("Enter the y of the Rectangle"))
        rec_height = int(input("Enter the Height of the Rectangle"))
        rec_width = int(input("Enter the Width of the Rectangle"))
        blue = int(input("How much blue should the rectangle have"))
        green = int(input("How much green should the rectangle have?"))
        red = int(input("How much red should the rectangle have?"))

        r1 = Rectangle(x=rec_x, y=rec_y, height=rec_height, width=rec_width, color=(red, green, blue))
        r1.draw(canvas)
        canvas.make('canvas.png')

    if shape_type.lower() == 'square':
        sq_x = int(input("Enter the x of the Square"))
        sq_y = int(input("Enter the y of the Square"))
        sq_side = int(input("Enter the Side of the Square"))
        blue = int(input("How much blue should the Square have?"))
        green = int(input("How much green should the Square have?"))
        red = int(input("How much red should the Square have?"))

        s1 = Square(x=sq_x, y=sq_y, side=sq_side, color=(red, green, blue))
        s1.draw(canvas)
        canvas.make('canvas.png')
    if shape_type.lower() == "q":
        canvas.make('canvas.png')
        break
