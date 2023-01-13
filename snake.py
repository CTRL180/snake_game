from turtle import Turtle


class Snake:
    def __init__(self, init_size):
        self.turtles = []
        self.path = init_size * [0]
        self.new_path = init_size * [0]

        for i in range(init_size):
            self.turtles.append(Turtle(shape="square"))
            self.turtles[i].color("white")
            self.turtles[i].penup()
            if i == 0:
                self.turtles[i].setpos(x=-10, y=10)
            else:
                self.turtles[i].setpos(x=-10 - i * 20, y=10)
            self.turtles[i].speed("fastest")

        self.turn_right = False
        self.turn_left = False
        self.invert_x = False
        self.invert_y = False
        self.current_head_x_position = self.turtles[0].xcor()
        self.current_head_y_position = self.turtles[0].ycor()
        # self.last_head_x_position = self.turtles[0].xcor()
        # self.last_head_y_position = self.turtles[0].ycor()

    def move_right(self):
        self.turn_right = True

    def move_left(self):
        self.turn_left = True

    def move(self):
        for i in range(0, len(self.path)):
            if self.path[i] == 0:
                self.turtles[i].forward(20)
            elif self.path[i] == 1:
                self.turtles[i].right(90)
                self.turtles[i].forward(20)
            elif self.path[i] == 2:
                self.turtles[i].left(90)
                self.turtles[i].forward(20)
            elif self.path[i] == -1:
                # self.turtles[i].hideturtle()
                x_cor = self.turtles[i].xcor()
                if x_cor > 0:
                    self.turtles[i].setx(-290)
                else:
                    self.turtles[i].setx(290)
                # self.turtles[i].setx(-self.turtles[i].xcor())
                # self.turtles[i].forward(20)
                # self.turtles[i].showturtle()
            elif self.path[i] == -2:
                # self.turtles[i].hideturtle()
                y_cor = self.turtles[i].ycor()
                if y_cor > 0:
                    self.turtles[i].sety(-290)
                else:
                    self.turtles[i].sety(290)
                # self.turtles[i].sety(-self.turtles[i].ycor())
                # self.turtles[i].forward(20)
                # self.turtles[i].showturtle()
            elif self.path[i] == -3:
                # self.turtles[i].hideturtle()
                x_cor = self.turtles[i].xcor()
                y_cor = self.turtles[i].ycor()
                if x_cor > 0:
                    self.turtles[i].setx(-290)
                else:
                    self.turtles[i].setx(290)
                if y_cor > 0:
                    self.turtles[i].sety(-290)
                else:
                    self.turtles[i].sety(290)
                # self.turtles[i].setx(-self.turtles[i].xcor())
                # self.turtles[i].sety(-self.turtles[i].ycor())
                # self.turtles[i].forward(20)
                # self.turtles[i].showturtle()

    def arrange_path(self):
        for j in range(1, len(self.path)):
            self.new_path[j] = self.path[j - 1]
            if j == (len(self.path) - 1):
                self.new_path[0] = 0
                self.path = self.new_path.copy()

    def next_move(self):
        # print(self.turtles[0].xcor())
        # print(f"y: {self.turtles[0].ycor()}")
        # self.last_head_x_position = self.current_head_x_position
        # self.last_head_y_position = self.current_head_y_position
        self.current_head_x_position = self.turtles[0].xcor()
        self.current_head_y_position = self.turtles[0].ycor()

        if round(self.current_head_x_position >= 310) or round(self.current_head_x_position) <= -310:
            self.invert_x = True
        if round(self.current_head_y_position >= 310) or round(self.current_head_y_position) <= -310:
            self.invert_y = True

        if self.invert_x and not self.invert_y:
            self.path[0] = -1
            self.invert_x = False
        elif self.invert_y and not self.invert_x:
            self.path[0] = -2
            self.invert_y = False
        elif self.invert_y and self.invert_x:
            self.path[0] = -3
            self.invert_y = False
            self.invert_x = False
        elif self.turn_right:
            self.path[0] = 1
            self.turn_right = False
        elif self.turn_left:
            self.path[0] = 2
            self.turn_left = False

    def extend_snake(self):
        size_turtles = len(self.turtles)
        first_piece_orientation = round(self.turtles[0].heading())
        first_piece_position = self.turtles[0].position()
        self.turtles = [(Turtle(shape="square"))] + self.turtles
        self.turtles[0].color("white")
        self.turtles[0].penup()

        if first_piece_orientation == 0:
            self.turtles[0].setpos(x=round(first_piece_position[0]) + 20, y=round(first_piece_position[1]))
            self.turtles[0].setheading(0)
        elif first_piece_orientation == 90:
            self.turtles[0].setpos(x=round(first_piece_position[0]), y=round(first_piece_position[1]) + 20)
            self.turtles[0].setheading(90)
        elif first_piece_orientation == 180:
            self.turtles[0].setpos(x=round(first_piece_position[0]) - 20, y=round(first_piece_position[1]))
            self.turtles[0].setheading(180)
        elif first_piece_orientation == 270:
            self.turtles[0].setpos(x=round(first_piece_position[0]), y=round(first_piece_position[1]) - 20)
            self.turtles[0].setheading(270)

        self.path = [0] + self.path
        self.new_path = len(self.path)*[0]

    def collision_detection(self):
        head_x_position = round(self.turtles[0].xcor())
        head_y_position = round(self.turtles[0].ycor())

        for i in range(1, len(self.path)):
            if round(self.turtles[i].xcor()) == head_x_position and head_y_position == round(self.turtles[i].ycor()):
                return False
        return True












