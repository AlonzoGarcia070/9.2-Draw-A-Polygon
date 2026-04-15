from turtle import *

def regular(turtle, sides):
    for i in range(sides):
        turtle.forward(100)
        turtle.right(360/sides)

screen=Screen()
screen.bgcolor("white")
screen.title("shapes")
screen.setup(width=1000,height=500)

polygons = { 3: "triangle", 5 :"pentagon", 6:"hexagon", 7:"septagon", 8: "octogon", 9: "nonogon", 10: "decagon"}

merlaut=Turtle()
merlaut.color("green")

while True:
    sides=int(input("Think of a shape and tell me how many sides does it have: "))
    merlaut.clear()
    if sides<3:
        print("This isn't a shape")
    elif sides !=4:
        regular(merlaut, sides)
        merlaut.write(polygons[sides])
    elif sides==4:
        print("this shape is a Quadrilateral")
        llel=int(input("How many parallel sides does the shape have: "))
        if llel==0:
                print("This is a unknown parallel")
        elif llel == 1:
            print("This is a trapezoid")
            for i in range(2):
                    merlaut.forward(200)
                    merlaut.left(120)
                    merlaut.forward(100)
                    merlaut.left(60)
                    merlaut.forward(100)
                    merlaut.left(60)
                    merlaut.forward(100)
        elif llel==4:
                print("This is a square")
                for i in range(2):
                    merlaut.forward(50)
                    merlaut.right(90)
                    merlaut.forward(50)
                    merlaut.right(90)
        else:
            llel2=(input("Are all the angles the same measure: "))
            if llel2=="no":
                print("This is a rhombus")
                for i in range(2):
                    merlaut.forward(100)
                    merlaut.right(120)
                    merlaut.forward(100)
                    merlaut.right(60)
            elif llel2=="yes":
                print("This is a rectangle")
                # merlaut.begin_fill()
                for i in range(2):
                    merlaut.forward(100)
                    merlaut.right(90)
                    merlaut.forward(50)
                    merlaut.right(90)
                # merlaut.end_fill()


    



# if side<3:
#     print("This isn't a shape")
# elif side ==3:
#     print("this shape is a triangle")
# elif side==4:
#     print("this shape is a Quadrilateral")
# elif side==5:
#     print("this shape is a Pentagon")
# elif side==6:
#     print("this shape is a hexagon")
# else:
#     print("This shape is unknown")
