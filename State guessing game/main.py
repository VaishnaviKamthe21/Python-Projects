import turtle
import pandas

screen = turtle.Screen()
screen.title("States Game")
political_map = "Python-Projects\State guessing game\political-map-india.gif"
screen.addshape(political_map)
turtle.shape(political_map)

states_data = pandas.read_csv("Python-Projects\State guessing game\states.csv" , delimiter='\t')
states_list = states_data.state.to_list()
print(states_list)
score = 0

while len(states_list) > 0:
    answer = screen.textinput(title=f"Score: {score}/31", prompt="What's the name of the state?")
    answer=answer.title()

    if answer == "Exit":
        missing_states = pandas.DataFrame(states_list)
        missing_states.to_csv("Python-Projects\State guessing game\missing_states.csv")
        break

    if answer in states_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states_data[states_data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)
        states_list.remove(answer)
        score += 1
    

