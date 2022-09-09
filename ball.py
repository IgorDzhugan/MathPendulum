import tkinter as tk
import numpy as np


class Ball:

    def __init__(self, canvas, wind_size, size=20, length=250, alpha=90, mass=1, gravity=9.8):
        self.rad = size
        self.length = length
        self.alpha = np.radians(alpha)
        self.x = wind_size / 2
        self.y = wind_size / 2
        self.center = wind_size / 2
        self.circle = canvas.create_oval(int(self.x - self.rad),
                                         int(self.y - self.rad),
                                         int(self.x + self.rad),
                                         int(self.y + self.rad),
                                         fill='#ff0000')
        self.m = mass
        self.g = gravity
        self.w = np.sqrt(self.g / self.length)
        self.time = 0
        self.line = canvas.create_line(self.center, self.center, self.x, self.y, width=2)
        self.__rect = canvas.create_rectangle(self.center - 20, self.center - 20, self.center + 20, self.center, fill='#000000')

    def move(self, canvas, root):
        x = self.center + self.length * np.sin(self.alpha*np.cos(self.w * self.time))
        y = self.center + self.length * np.cos(self.alpha*np.cos(self.w * self.time))
        canvas.delete(self.line)
        self.line = canvas.create_line(self.center, self.center,
                                       self.center + (self.length - self.rad) * np.sin(self.alpha*np.cos(self.w * self.time)),
                                       self.center + (self.length - self.rad) * np.cos(self.alpha*np.cos(self.w * self.time)))
        canvas.move(self.circle, x - self.x, y - self.y)
        self.x = x
        self.y = y
        root.update()
        self.time += 0.1
