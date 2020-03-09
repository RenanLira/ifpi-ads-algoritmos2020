import turtle
def main():
    bob = turtle.Turtle()

    print(arc(bob, 20, 160))

    turtle.mainloop()


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def circle(t, r):
    circunferencia = 2 * 3.14 * r
    n = 50
    length = circunferencia / n
    polygon(t, length, n)

def arc(t, r, angle):
    arc_length = 2 * 3.14 * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

main()