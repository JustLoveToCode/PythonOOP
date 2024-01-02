from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Instantiating the Screen Object:
screen = Screen()
# Setting up the Screen Background Colors
screen.bgcolor("gray")
# Setting up the Width and Height of the Screen:
screen.setup(width=800, height=600)
screen.title("Ping Pong Game")
# Turn off the Animation:
screen.tracer(0)

# Instantiating 2 different Paddle Object which is the
# r_paddle and the l_paddle and the position of the paddle object:
# Initialize the r_paddle object:
r_paddle = Paddle((350, 0))
# Initialize the l_paddle object:
l_paddle = Paddle((-350, 0))
# Initialize the ball object:
ball = Ball()
# Initialize the scoreboard object:
scoreboard = Scoreboard()

# Listen for event:
screen.listen()
# Using the screen.onkey():
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()




    # Detect the Collision with the Top or Bottom Wall:
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()

    # Detect Collision with Right Paddle and whether it has
    # gone far enough on the Right Paddle:
    if ball.xcor() > 323 and ball.distance(r_paddle) < 50 or ball.xcor() < -323 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    # Detect the R Paddle Miss:
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect the L Paddle Miss:
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()
