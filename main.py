from turtle import Screen
from paddle import Paddle
from ball import PongBall
import time
from scoreboard import ScoreBoard

POSITION = [(-350, 0), (350, 0)]
TOP, BOTTOM = 290, -290

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player1 = Paddle(POSITION[0])
player2 = Paddle(POSITION[1])
ball = PongBall()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(player1.paddle_up, "w")
screen.onkey(player1.paddle_down, "s")
screen.onkey(player2.paddle_up, "Up")
screen.onkey(player2.paddle_down, "Down")

game_is_on = True
bounce = False
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > TOP or ball.ycor() < BOTTOM:
        ball.bounce_y()
    if ball.distance(player2) < 50 and ball.xcor() > 340 or ball.distance(player1) < 50 and ball.xcor() < -340:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()