from turtle import Turtle

FONT = ('Ariel', 20, "italic")
ALIGNMENT = 'center'


class Scoreboard(Turtle):

    def __init__(self, x):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x, 270)
        self.score = 0
        self.color('white')
        self.display_score()
        self.line = Turtle()

    def display_score(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f'''Game Over

   Score: {self.score}''', align=ALIGNMENT, font=('Ariel', 40, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.display_score()


class Dottedline(Turtle):

    def __init__(self):

        super().__init__()
        self.pencolor('white')
        self.hideturtle()
        self.penup()
        self.pensize(5)
        self.goto(0, 280)
        self.setheading(270)
        self.dashed_line()

    def dashed_line(self):
        for x in range(0, 400):
            self.forward(15)
            self.pendown()
            self.forward(10)
            self.penup()
