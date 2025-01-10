import turtle
import math
import pygame
import threading

def play_music():
    try:
        import os
        music_file = "music.wav"
        print(f"Looking for music file at: {os.path.abspath(music_file)}")
        if not os.path.exists(music_file):
            print(f"Error: {music_file} not found!")
            return
            
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play(-1)
        print("Music started!")
    except pygame.error as e:
        print(f"Error initializing or playing music: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

music_thread = threading.Thread(target=play_music)
music_thread.start()

screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("pink") #might change into custom image
screen.title("personalized carousel")

screen.register_shape("small bunny.gif")
screen.register_shape("small dolphin.gif")
screen.register_shape("small bird.gif")

# user questions
carosuel_name = screen.textinput("carosuel name", "what do you wish to name your carosuel?")
#change screen.title to answer
num_animals = int(screen.numinput("animals", "how many animals do you want on the carousel? (max 10)", 4, minval=1, maxval=10))
velocity = float(screen.numinput("velocity", "enter the carousel's rotation velocity (0.1~10:", 2, minval=0.1, maxval=10))
#ask for whole mass of animals
animal_options = ["bunny", "dolphin", "bird"]
animals = []
for i in range(num_animals):
    choice = screen.textinput("animal type", f"animal {i+1}: choose bunny, dolphin, or bird").lower()
    while choice not in animal_options:
        choice = screen.textinput("Choose Animal", f"Invalid choice! Animal {i+1}: Choose bunny, dolphin, or bird").lower()
    animals.append(choice)

#calculate the acting forces 

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

# animals
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

def rotate():
    for animal in animal_turtles:
        x, y = animal.pos()
        angle = math.atan2(y, x) + math.radians(velocity)
        new_x = 150 * math.cos(angle)
        new_y = 150 * math.sin(angle)
        animal.goto(new_x, new_y)
    screen.ontimer(rotate, 50)

rotate()
#add a box that has all the acting forces
screen.mainloop()
