from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.shapesize(0.4, 3)
        self.color('white')
        self.penup()
        self.goto(position)
        self.setheading(90)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)

    def location(self):
        x = self.xcor()
        y = self.ycor()
        my_tuple = (x, y)
        return my_tuple


class Computer:

    def __init__(self):
        self.comp = Paddle()
        game = True
        while game:

            self.comp.up()
            if self.comp.ycor() > 270 or self.com.ycor() < -270:
                self.comp.right(180)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(0.5, 0.5)
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_move *= -1

    def collision_paddle(self, position):
        if (self.distance(position) < 20 and self.xcor() < 390) or (self.distance(position) < 20 and self.xcor() > -390):
            self.x_move *= -1

    def out_right(self):
        if self.xcor() > 405:
            self.restart()
            return True

    def out_left(self):
        if self.xcor() < -405:
            self.restart()
            return True

    def restart(self):
        self.goto(0, 0)
        self.x_move *= -1



