import turtle
import random


def noisy(number, range=5):
    # adds noise to the number
    if random.randrange(0,100) > 50:
        return number + random.randrange(0, range)
    else:
        return number - random.randrange(0, range)

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)pyt
        t.right(20)
        tree(branchLen-15,t)
        t.left(noisy(40))
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    t.hideturtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)

    t.down()
    t.color("green")
    tree(75 ,t)
    myWin.exitonclick()

main()
