import random
from turtle import Turtle


class Food:
    def __init__(self):
        self.food_locals = []
        self.food_local = [50, 50]
        for x in range(-290, 310, 20):
            for y in range(-290, 310, 20):
                self.food_locals.append([x, y])

        self.food_symbol = Turtle(shape='circle')
        self.food_symbol.color("blue")
        self.food_symbol.penup()
        self.new_food_local()

    def new_food_local(self):
        self.food_local = random.choice(self.food_locals)
        self.food_symbol.setpos(x=self.food_local[0], y=self.food_local[1])
