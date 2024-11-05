import turtle
import random

screen = turtle.Screen() # Setting up the game window
screen.setup(1000, 1000)
screen.title("⋆˚✿˖° Typing Game ⋆𐙚₊˚⊹♡")
screen.bgcolor("darkslateblue")
screen.tracer(0, 0)
turtle.hideturtle()
turtle.up()
turtle.color("white")

score_turtle = turtle.Turtle() # Creating a turtle for displaying the score
score_turtle.color("lightblue")
score_turtle.up()
score_turtle.hideturtle()
turtle.goto(350, 350)
turtle.color("lightblue")
turtle.write("Score: ", align="center", font=("Courier", 25, "bold"))

min_speed = 5
max_speed = 7
letters = []  # List to store letters
speeds = []  # List to store speed of each letter
pos = []  # List to store position of each letter
lts = []  # List of turtle objects for each letter
n = 10  # Number of letters
game_over = False
score = 0

def increase_difficulty(): # Increases the minimum and maximum speed
    global min_speed, max_speed
    min_speed += 1
    max_speed += 1
    screen.ontimer(increase_difficulty, 5000)

def draw_game_over():  # Displays the game over message and the final score.
    turtle.goto(0, 0)
    turtle.color("hotpink")  # for aesthetic :)
    turtle.write(
        "⋆｡‧˚ʚ GAME OVER ɞ˚‧｡⋆", align="center", font=("Helvetica", 90, "bold")
    )
    turtle.goto(0, -60)
    turtle.color("white")
    turtle.write(
        "Your Score is {}".format(score),
        align="center",
        font=("Courier", 30, "bold italic")
    )
    turtle.goto(0, -110)
    turtle.color("lightblue")
    turtle.write("꒰ᐢ. .ᐢ꒱₊˚⊹", align="center", font=("Courier", 20, "bold"))
    turtle.goto(0, -140)
    turtle.color("lightblue")
    turtle.write(
        "Please grade me with mercy, thank you ♡ ",
        align="center",
        font=("Courier", 20, "bold"),
    )
    screen.update()

def draw_score():  # Updates and displays the current score.
    score_turtle.clear()
    score_turtle.goto(420, 350)
    score_turtle.write(
        "{}".format(score), align="center", font=("Courier", 25, "normal")
    )
    screen.update()

def draw_letters(): # Draws the letters on the screen 
    global game_over
    for i in range(len(letters)):
        lts[i].clear()
        lts[i].goto(pos[i])
        lts[i].write(letters[i], align="center", font=("Arial", 25, "normal"))
        pos[i][1] -= speeds[i]
        if pos[i][1] < -500:
            game_over = True
            draw_game_over()
            return
    screen.update()
    screen.ontimer(draw_letters, 50)

def f(c): # Handles keyboard input.
    global score
    if c in letters:
        score += 1
        k = letters.index(c)
        while True:
            l = chr(ord("a") + random.randrange(26))
            if l not in letters:
                letters[k] = l
                break
        pos[k] = [random.randint(-450, 450), 500]
        speeds[k] = random.randint(min_speed, max_speed)
    else:
        score -= 1
    draw_score()

for _ in range(n):  # Initializing the letters, their positions, and speeds
    lts.append(turtle.Turtle())
    while True:
        l = chr(ord("a") + random.randrange(26))
        if l not in letters:
            letters.append(l)
            break
    speeds.append(random.randint(min_speed, max_speed))
    pos.append([random.randint(-450, 450), 500])

for i in range(n):  # Configuring each turtle object for letters
    lts[i].speed(0)
    lts[i].hideturtle()
    lts[i].up()
    lts[i].color("white")

draw_letters()
increase_difficulty()

screen.onkey(lambda: f("a"), "a") # Setting up keyboard bindings for each letter
screen.onkey(lambda: f("b"), "b")
screen.onkey(lambda: f("c"), "c")
screen.onkey(lambda: f("d"), "d")
screen.onkey(lambda: f("e"), "e")
screen.onkey(lambda: f("f"), "f")
screen.onkey(lambda: f("g"), "g")
screen.onkey(lambda: f("h"), "h")
screen.onkey(lambda: f("i"), "i")
screen.onkey(lambda: f("j"), "j")
screen.onkey(lambda: f("k"), "k")
screen.onkey(lambda: f("l"), "l")
screen.onkey(lambda: f("m"), "m")
screen.onkey(lambda: f("n"), "n")
screen.onkey(lambda: f("o"), "o")
screen.onkey(lambda: f("p"), "p")
screen.onkey(lambda: f("q"), "q")
screen.onkey(lambda: f("r"), "r")
screen.onkey(lambda: f("s"), "s")
screen.onkey(lambda: f("t"), "t")
screen.onkey(lambda: f("u"), "u")
screen.onkey(lambda: f("v"), "v")
screen.onkey(lambda: f("w"), "w")
screen.onkey(lambda: f("x"), "x")
screen.onkey(lambda: f("y"), "y")
screen.onkey(lambda: f("z"), "z")

screen.listen()
screen.mainloop()
