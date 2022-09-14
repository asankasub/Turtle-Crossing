from turtle import Turtle
FONT = ("Courier", 24, "normal")
POSITION = (-270, 260)

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.score_track()

    def increase_score(self):
        
        self.score += 1
        self.score_track()


    def score_track(self):
        self.clear()
        self.goto(POSITION)
        self.write(self.score, align = "center", font = FONT)
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align = "center", font = FONT)


    
       

    