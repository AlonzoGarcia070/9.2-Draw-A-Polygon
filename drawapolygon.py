from turtle import *

def regular(turtle, sides):
    for i in range(sides):
        turtle.forward(100)
        turtle.right(360/sides)



screen=Screen()
screen.bgcolor("white")
screen.title("shapes")
screen.setup(width=1000,height=500)

merlaut=Turtle()
merlaut.color("green")


while True:
    side=int(input("Think of a shape and tell me how many sides does it have: "))
    merlaut.clear()
    if side<3:
        print("This isn't a shape")
    elif side ==3:
        print("this shape is a triangle")
    elif side==4:
        print("this shape is a Quadrilateral")
        quad=int(input("How many paralel sides does the shape have"))
        if quad<2:
                print("This is a unknown parallel")
        if quad==2:
            print("This is a trapezoid")
        if quad==4:
            print("This is a square")
    elif side==5:
        print("this shape is a Pentagon")
    elif side==6:
        print("this shape is a hexagon")
    else:
        print("This shape is unknown")
    regular(merlaut, side)

    



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

































