from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
WALL_LIMIT = 300

class Snake:

    def __init__(self,screen,restart_callback):
        self.screen = screen
        self.restart_callback = restart_callback 
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.game_is_on = True
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color("red")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        last_segment_position = self.segments[-1].position()
        self.add_segment(last_segment_position)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move(self):
        if not self.game_is_on:
            return

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

         # Check for collision with walls
        if (
            self.head.xcor() > WALL_LIMIT or
            self.head.xcor() < -WALL_LIMIT or
            self.head.ycor() > WALL_LIMIT or
            self.head.ycor() < -WALL_LIMIT
        ):
            self.game_over()

    def game_over(self):
        print("Game Over!")
        self.game_is_on = False
        game_over_text = Turtle()
        game_over_text.hideturtle()
        game_over_text.penup()
        game_over_text.color("black")
        game_over_text.goto(0,30)
        game_over_text.write("Game Over!", align="center", font=("Arial", 24, "bold"))

        self.create_buttons()

    def create_buttons(self):
        # Restart Button
        restart_button = Turtle()
        restart_button.shape("square")
        restart_button.color("green")
        restart_button.shapesize(stretch_wid=1, stretch_len=5)
        restart_button.penup()
        restart_button.goto(-100, -80)
        restart_button.write("Restart", align="center", font=("Arial", 12, "normal"))
        restart_button.onclick(self.restart_game)

        # Exit Button
        exit_button = Turtle()
        exit_button.shape("square")
        exit_button.color("red")
        exit_button.shapesize(stretch_wid=1, stretch_len=5)
        exit_button.penup()
        exit_button.goto(100, -80)
        exit_button.onclick(self.exit_game)
        exit_button.write("Exit", align="center", font=("Arial", 12, "normal"))


    def restart_game(self,x,y):
        self.screen.clear()
        self.restart_callback()

    def exit_game(self,x,y):
        self.screen.bye()