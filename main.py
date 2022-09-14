from turtle import Screen, Turtle
import time
import random
from player import Player, FINISH_LINE_Y
from car_manager import CabManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)
turtle = Player()
car_manager = CabManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(turtle.player_move, "Up")

game_is_on = True

while game_is_on:
    

    time.sleep(0.1)
    screen.update()

    if turtle.ycor() >= FINISH_LINE_Y:
        scoreboard.increase_score()
        car_manager.turtle_crossed()

    turtle.player_end()
    car_manager.car_maker()
    car_manager.move_car()

    for i in range(len(car_manager.all_cars)):
        if turtle.distance(car_manager.all_cars[i]) <= 20:
            game_is_on = False
            scoreboard.game_over()
        
            





    
    
   
    






screen.exitonclick()



