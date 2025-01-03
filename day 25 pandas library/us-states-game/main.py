import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()
guess_state = []

while len(guess_state) < 50:
    answer_state = screen.textinput(title=f"{len(guess_state)}/50 State Guess",
                                    prompt="what is the state's name?").title()

    if answer_state == "Exit":
        missing_state = [state for state in all_state if state not in guess_state]
        # missing_state = []
        # for state in all_state:
        #     if state not in guess_state:
        #         missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("state_to_learn.csv")
        break
    if answer_state in all_state:
        guess_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data['x'].iloc[0]), int(state_data['y'].iloc[0]))
        t.write(answer_state)
