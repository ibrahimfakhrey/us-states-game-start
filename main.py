import turtle
import  pandas
screen = turtle.Screen()
screen.title("U.S.GAME")

image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score=49
game_ison=True
while game_ison:
    answer=screen.textinput(title=f"Geusse a state,your score{score}/50",prompt="what is the other state").title()
    data =pandas.read_csv("50_states.csv")
    for choice in data.state:
        if answer==choice:
            c=data[data.state==choice]
            new_turlte=turtle.Turtle()
            new_turlte.hideturtle()
            new_turlte.penup()
            new_x=int(c.x)
            new_y=int(c.y)
            new_turlte.goto(new_x,new_y)
            new_turlte.write(choice, True, align="center", font=15)
            score+=1
            if score==50:
                a=screen.textinput(title="you have achived the game ",prompt="do you wanna close the game write y")
                if a=="y":
                    game_ison=False







