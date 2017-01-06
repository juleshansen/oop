#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

class Circle():
    def __init__(self, cx, cy, radius, color):
        self.cx = cx
        self.cy = cy
        self.radius = radius
        self.color = color

    def f(self, x, y):
        t_dist = math.sqrt((x - self.cx)**2 + (y - self.cy)**2)
        if (t_dist < self.radius):
            return(True)
        else:
            return(False)

class Rectangle():
    def __init__(self, x0, y0, x1, y1, color):
        pass

    def f(self, x, y):
        pass
