from turtle import Screen
import time
from Objects import Paddle, Ball
from scene import Scoreboard, Dottedline

screen = Screen()
screen.title('Pong')
screen.tracer(0)
screen.setup(800, 600)
screen.bgcolor('black')
screen.listen()
player_1 = Paddle((-380, 0))
score_1 = Scoreboard(-200)
score_2 = Scoreboard(200)
line = Dottedline()
ball = Ball()
player_2 = Paddle((380, 0))
screen.onkeypress(player_1.up, 'w')
screen.onkeypress(player_1.down, 's')
screen.onkeypress(player_2.up, 'Up')
screen.onkeypress(player_2.down, 'Down')


game_is_on = True
while game_is_on:
    ball.move()
    ball.bounce()
    ball.collision_paddle(player_1.location())
    ball.collision_paddle(player_2.location())
    if ball.out_left():
        score_2.increase_score()
    elif ball.out_right():
        score_1.increase_score()
    time.sleep(0.07)
    screen.update()


screen.exitonclick()

