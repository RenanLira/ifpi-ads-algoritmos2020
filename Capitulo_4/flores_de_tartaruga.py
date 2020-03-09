import turtle
def main():
    bob = turtle.Turtle()
    #flor_1
    flor(bob, 100, 60, 7)
    
    #flor_2
    #flor(bob, 100, 80, 10)

    #flor_3
    #flor(bob, 100, 20, 22)
    turtle.mainloop()


def flor(t, r, angle, num_petu):
    for i in range(num_petu):
        petula(t, r, angle)
        t.lt(360.0/num_petu)

def petula(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)

def arc(t, r, angle):
    arc_length = 2 * 3.14 * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)





main()