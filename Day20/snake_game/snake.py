from turtle import Turtle
# INITIALIZE CONSTANT VARIABLE
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    # CONSTRUCTOR
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # CREATES A SNAKE INSTANCE AND PUTS IT IN SCREEN
    def create_snake(self):

        for position in STARTING_POS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # MOVES THE SNAKE, moves the last piece forward to the second last pos and so on
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    # GO UP IF NOT GOING DOWN
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # GO DOWN IF NOT GOING UP
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # GO LEFT IF NOT GOING RIGHT
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # GO RIGHT IF NOT GOING LEFT
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
