#!/home/justin/.venv/learn/bin/python
import tkinter

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# Implement the default Matplotlib key bindings.
from matplotlib.figure import Figure

import numpy as np


root = tkinter.Tk()
root.wm_title("Embedding in Tk")

a = 1
fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
sub = fig.add_subplot(111)
sub.plot(t, 2 * np.sin(a * 2 * np.pi * t))
#fig.add_subplot(111).imshow(np.random.normal(0, 1, size=[28, 28]))

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()

#toolbar = NavigationToolbar2Tk(canvas, root)
#toolbar.update()

def increase():
    global a
    global sub
    global canvas
    a += 1
    sub.plot(t, 2 * np.sin(a * 2 * np.pi * t))
    canvas.draw()

button = tkinter.Button(master=root, text="Quit", command=root.quit)
button_change = tkinter.Button(master=root, text="Increase", command=increase)


# Packing order is important. Widgets are processed sequentially and if there
# is no space left, because the window is too small, they are not displayed.
# The canvas is rather flexible in its size, so we pack it last which makes
# sure the UI controls are displayed as long as possible.
button.pack(side=tkinter.BOTTOM)
button_change.pack(side=tkinter.BOTTOM)
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

tkinter.mainloop()
