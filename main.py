import turtle
from turtle import Screen

screen = Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


import pandas

data = pandas.read_csv("50_states.csv")
state_data = data.state.to_list()
print(state_data)


# count = 0
# game_is_on = True
# while game_is_on:
guessed_state = []
while len(guessed_state) < 50:
    answer = screen.textinput(title=f"Your score is{len(guessed_state)}/50", prompt="theres another state name").title( )
    if answer == 'Exit':
        missing_state =[]
        for state in state_data:
            if state not in guessed_state:
                missing_state.append(state)
        print(missing_state)
        break
    if answer in state_data:
        guessed_state.append(answer)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state = data[data.state == answer]
        t.goto(int(state.x),int(state.y))
        t.write(answer)
#     line = data[data["state"] == answer]
#     if line in state_data:
#         cor = turtle.Turtle()
#         cor.penup()
#         cor.hideturtle()
#         cor.goto(int(line['x']),int(line['y']))
#         cor.write(answer, font=("Verdana",10, "normal"))
#         count +=1
