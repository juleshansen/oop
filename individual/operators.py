#!/usr/bin/env python
# -*- coding: utf-8 -*-

class UnionShape():
    def __init__(self, a, b):
        """Constructs a UnionShape as union of given shapes a and b.
        Note: color or union is average between colors of a and b."""
        pass

    def f(self, x, y):
        """Characteristic function of the shape.
        Returns True if (x,y) is inside the shape, else False."""
        pass


class IntersectionShape():
    def __init__(self, a, b):
        """Constructs a IntersectionShape as union of given shapes a and b.
        Note: color or intersection is average between colors of a and b."""
        pass

    def f(self, x, y):
        """Characteristic function of the shape.
        Returns True if (x,y) is inside the shape, else False."""
        pass


class DiffShape():
    def __init__(self, a, b):
        """Constructs a DiffShape as union of given shapes a and b.
        Note: color or difference is the color of a."""
        pass

    def f(self, x, y):
        """Characteristic function of the shape.
        Returns True if (x,y) is inside the shape, else False."""
        pass
