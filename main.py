import turtle
import math

screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("pink") 
screen.title("personalized carousel")

screen.register_shape("small bunny.gif")
screen.register_shape("small dolphin.gif")
screen.register_shape("small bird.gif")

carosuel_name = screen.textinput("carousel name", "what do you wish to name your carousel?")
screen.title(f"{carosuel_name}")
num_animals = int(screen.numinput("animals", "how many animals do you want on the carousel? (max 10)", minval=1, maxval=10))
mass = float(screen.numinput("total animal mass", "enter the total mass of the animals (kg, max=50):", minval=1, maxval=50))
velocity = float(screen.numinput("velocity", "enter the carousel's velocity:", minval=0.1, maxval=10))
acceleration = float(screen.numinput("acceleration", "enter the acceleration of the carousel (m/s^2):", minval=0.1))

animal_options = ["bunny", "dolphin", "bird"]
animals = []
for i in range(num_animals):
    choice = screen.textinput("animal type", f"animal {i+1}: choose bunny, dolphin, or bird").lower()
    animals.append(choice)

center = turtle.Turtle()
center.shape("circle")
center.color("pink")  
center.shapesize(3)
center.penup()

base = turtle.Turtle()
base.penup()
base.goto(0, -200)
base.pendown()
base.color("white")  
base.begin_fill()
base.circle(200)
base.end_fill()
base.hideturtle()

animal_turtles = []
for i in range(num_animals):
    animal = turtle.Turtle()
    animal.penup()
    angle = (360 / num_animals) * i
    x = 150 * math.cos(math.radians(angle))
    y = 150 * math.sin(math.radians(angle))
    animal.goto(x, y)

    if animals[i] == "bunny":
        animal.shape("small bunny.gif")
    elif animals[i] == "dolphin":
        animal.shape("small dolphin.gif")
    elif animals[i] == "bird":
        animal.shape("small bird.gif")
    animal_turtles.append(animal)

force = mass * acceleration
def display_force():
    info_box = turtle.Turtle()
    info_box.penup()
    info_box.hideturtle()
    info_box.goto(-370, 350) 
    info_box.color("white")
    info_box.write(f"force of carousel: {force:.2f} N", align="left", font=("Arial", 12, "normal"))

def rotate():
    for animal in animal_turtles:
        x, y = animal.pos()
        angle = math.atan2(y, x) + math.radians(velocity)
        new_x = 150 * math.cos(angle)
        new_y = 150 * math.sin(angle)
        animal.goto(new_x, new_y)
    screen.ontimer(rotate, 50)

rotate()
display_force()
screen.mainloop()
