#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

class SimpleGUI():
    """

    """
    def __init__(self):
        self.width = 640
        self.height = 480
        self.clear()

    def show(self):
        """Shows the current image on display (uses matplotlib)"""
        plt.imshow(np.asarray(self.img), aspect='equal')
        plt.axis('off')
        plt.show()

    def clear(self):
        """ resets the image to white, draw a black border around """
        self.img = Image.new( 'RGB', (self.width, self.height), "white")
        self.pixels = self.img.load()
        # horizontal borders
        for i in xrange(self.width):
            self.pixels[i,0] = (0,0,0)
            self.pixels[i,self.height-1] = (0,0,0)
        # vertical borders
        for j in xrange(self.height):
            self.pixels[0,j] = (0,0,0)
            self.pixels[self.width-1,j] = (0,0,0)

    def test(self):
        """ displays a test image """
        self.clear()
        for i in xrange(self.width):
            for j in xrange(self.height):
                self.pixels[i,j] = (i % 255, j % 255, 128)
        self.show()

    def draw(self, arealist):
        """ draw a list of shapes as defined in module shapes"""
        # clears the image
        self.clear()

        # checks for every pixel in the image
        for i in xrange(self.width):
            for j in xrange(self.height):
                # if we are in one of the areas in the list
                for o in arealist:
                    if o.f(i,j):
                        # drop a pixel in there, using color of the area
                        self.pixels[i,j] = o.color

        # systematically show the resulting image
        self.show()
