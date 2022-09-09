import tkinter as tk
import ball
from time import sleep


if __name__ == '__main__':
    wind_size = 700
    root = tk.Tk(className='Маятник')
    root.geometry(str(wind_size) + 'x' + str(wind_size))
    canvas = tk.Canvas(root, bg='white', height=wind_size, width=wind_size)
    canvas.pack()
    ball = ball.Ball(canvas, wind_size)
    x, y = 20, 250
    canvas.create_text(wind_size / 2, 50, text = 'Маятник', font = ('Arial', 30))
    while True:
        ball.move(canvas, root)
        sleep(0.03)
    root.mainloop()



