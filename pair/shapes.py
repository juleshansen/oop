#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

class Circle():
    def __init__(self, cx, cy, radius, color):
        """Constructs a Circle instance
        centered around (cx,cy) with radius and color."""
        self.cx = cx
        self.cy = cy
        self.radius = radius
        self.color = color

    def f(self, x, y):
        """Characteristic function of the shape.
        Returns True if (x,y) is inside the shape, else False."""
        t_dist = math.sqrt((x - self.cx)**2 + (y - self.cy)**2)
        if (t_dist < self.radius):
            return(True)
        else:
            return(False)


class Rectangle():
    def __init__(self, x0, y0, x1, y1, color):
        """Constructs a Rectangle instance
        with top-left point (x0,y0), bottom-right (x1,y1) and color."""
        pass

    def f(self, x, y):
        """Characteristic function of the shape.
        Returns True if (x,y) is inside the shape, else False."""
        pass
