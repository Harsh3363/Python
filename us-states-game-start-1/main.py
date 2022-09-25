import turtle
import pandas

timmy = turtle.Turtle()
screen = turtle.Screen()

timmy.penup()
timmy.hideturtle()

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_score = 0

# these below line of codes to get the coordinates of the place where mouse was clicked ->
# def get_coordinate(x, y):
#     print(x, y)

# turtle.onscreenclick(get_coordinate)
# turtle.mainloop()
def state_game():
    global game_score
    pop_up = screen.textinput(title=f"score: {game_score}/50", prompt="Guess another state")
    pop_up = pop_up.title()

    data = pandas.read_csv("50_states.csv")
    states_data = data.state

    # data2 = pandas.read_csv("correct_ans.csv")
    # correct_states_data = data.state

    for S_name in states_data:
        if S_name == pop_up:
            with open("correct_ans.csv",mode="a") as file:
                file.write(S_name)
            # for correct_states_data in correct_states_data:
            #     if correct_states_data != pop_up:

            game_score+=1
            location = data[data.state == f"{S_name}"]
            x_cor = int(location.x)
            y_cor = int(location.y)
            # print(x_cor, y_cor)
            timmy.goto(x_cor, y_cor)
            timmy.write(S_name)


for i in range(50):
    state_game()

# since we are using turtle.mainloop() so commented the exitonclick as the loop method is more effective
screen.exitonclick()
