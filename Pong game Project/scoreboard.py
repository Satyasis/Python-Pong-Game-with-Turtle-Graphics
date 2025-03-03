from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 240)
        self.write(self.l_score, align= "center", font=("Courier", 52, "normal"))
        self.goto(100, 240)
        self.write(self.r_score, align= "center", font=("Courier", 52, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
        
    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over", align= "center", font=("Courier", 52, "normal"))
        self.goto(-60, -60)
        self.write(self.l_score, align= "center", font=("Courier", 46, "normal"))
        self.goto(60, -60)
        self.write(self.r_score, align= "center", font=("Courier", 46, "normal"))
        

