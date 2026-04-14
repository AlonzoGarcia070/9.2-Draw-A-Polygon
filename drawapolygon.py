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
        llel=int(input("How many parallel sides does the shape have: "))
        if llel==0:
                print("This is a unknown parallel")
        elif llel == 1:
            print("trapezoid")
        else:
            llel2=(input("Are all the angles the same measure: "))
            if llel2=="no":
                print("This is a rhombus")
            elif llel2=="yes":
                print("This is a rectangle")
                turtle.forward(100)
                turtle.right(50)
                turtle.right(100)
                turtle.right(50)
            if llel==4:
                print("This is a square")
    elif side==5:
        print("this shape is a Pentagon")
        regular(turtle, sides)
    elif side==6:
        print("this shape is a hexagon")
        regular(turtle, sides)
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

































