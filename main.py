from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

x= 405
y = 78

screen_width = 600
screen_height = 600

screen = Screen()
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)

snake = Snake(3)
food = Food()
text = ScoreBoard()
game = True

screen.listen()
screen.onkey(key="d", fun=snake.move_right)
screen.onkey(key="a", fun=snake.move_left)
screen.onkey(key="w", fun=snake.move_left)


while game:
    #screen.update()
    #time.sleep(0.1)
    snake.move()
    screen.update()
    time.sleep(0.1)

    if snake.collision_detection():
        pass
    else:
        text.game_over()
        game = False

    if round(snake.turtles[0].position()[0]) == food.food_local[0] and round(snake.turtles[0].position()[1]) == food.food_local[1]:
        food.new_food_local()
        snake.extend_snake()
        text.write_score()

    snake.arrange_path()

    snake.next_move()




"""
while game:
    for j in range(len(turtles)):
        turtles[j].forward(20)
        
turtle_test = Turtle(shape="square")
turtle_test.color("red")
turtle_test.penup()
turtle_test.setpos(x=270, y=10)

turtle_test = Turtle(shape="square")
turtle_test.color("blue")
turtle_test.penup()
turtle_test.setpos(x=280, y=0)     
        
"""
screen.exitonclick()
