from turtle import Turtle

class Create_Turtle:
    def __init__(self):
        self.names_list = []


    def create_turtles(self, positions, text):
        turtle = Turtle()
        turtle.hideturtle()
        turtle.penup()
        turtle.color("red")
        turtle.goto(positions)
        turtle.write(text)
        self.names_list.append(turtle)