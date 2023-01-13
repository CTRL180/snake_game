from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = -1

        #self.t = Turtle()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(x=0, y=270)
        self.write_score()

    def write_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=('Courier', 20, 'normal'))

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER", move=False, align="center", font=('Courier', 20, 'normal'))

