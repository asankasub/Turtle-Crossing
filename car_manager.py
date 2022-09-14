from turtle import Turtle
import random
COLORS = ["red", "orange", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_Y_POSITIONS = list(range(-250,251))

class CabManager:
    
    def __init__(self):


        self.all_cars = []
        self.move_inc = 0
       
        
       

    def car_maker(self):

            random_number = random.randint(1,6)
            if random_number == 6:

                new_car = Turtle("square")
                new_car.shapesize(1, 2)
                new_car.penup()
                new_car.color(random.choice(COLORS))
                new_car.goto(300, random.choice(STARTING_Y_POSITIONS))
                new_car.setheading(180)
                self.all_cars.append(new_car)

    def move_car(self):



        for car in self.all_cars:
        
            car.forward(STARTING_MOVE_DISTANCE + self.move_inc)
    
    def turtle_crossed(self):

        self.move_inc += MOVE_INCREMENT