import tkinter as tk
import numpy as np


class Ball:

    def __init__(self, canvas, wind_size, size=20, length=150, alpha=75, mass=1, gravity=9.8):
        self.rad = size
        self.length = length
        self.alpha = np.radians(alpha)
        self.x = wind_size / 2
        self.y = wind_size * 0.5
        self.center = wind_size / 2
        self.circle = canvas.create_oval(int(self.x - self.rad),
                                         int(self.y - self.rad),
                                         int(self.x + self.rad),
                                         int(self.y + self.rad))
        self.m = mass
        self.g = gravity
        self.w = np.sqrt(self.g / self.length)
        self.time = 0

    def move(self, canvas, root):
        x = self.center + self.length * np.sin(self.alpha*np.cos(self.w * self.time))
        y = self.center + self.length * np.cos(self.alpha*np.cos(self.w * self.time))
        print(x, y)
        canvas.move(self.circle, x - self.x, y - self.y)
        self.x = x
        self.y = y
        root.update()
        self.time += 0.01
