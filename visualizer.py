#!/usr/bin/env python3
import turtle


class Visualizer:
    def __init__(self, sequence):
        self.sequence = sequence

    def get_window(self):
        wn = turtle.Screen()
        wn.screensize(1500, 1500)
        return wn

    def draw(self):
        seq = self.sequence
        wn = self.get_window()

        t = turtle.Turtle()
        t.speed("fast")
        t.penup()

        dimx, dimy = wn.screensize()
        it = iter(seq)
        x, y = next(it)
        t.goto(x - dimx / 2, y - dimy / 2)
        t.pendown()
        t.dot()

        for coords in it:
            x, y = coords
            t.goto(x - dimx / 2, y - dimy / 2)
            t.dot()

        wn.exitonclick()
