import tkinter as tk
from tkinter import *

class Viewer:
    def __init__(self, root):
        f = open("axis_v.txt", "r")
        AXv = f.read()
        f.close()
        f = open("axis_w.txt", "r")
        AXw = f.read()
        f.close()
        f = open("axis_x.txt", "r")
        AXx = f.read()
        f.close()
        f = open("axis_y.txt", "r")
        AXy = int(f.read())
        f.close()
        f = open("axis_z.txt", "r")
        AXz = int(f.read())
        f.close()
        self.root = root
        self.root.title("5 Axis Viewer")
        self.root.geometry("450x620")
        self.root.resizable(0, 0)
        self.hex = ''
        hex_label = Label(self.root, text="Axis V ", font=('arial', 10, 'bold'))
        hex_label.place(x=40, y=300)
        self.hex_entry = Entry(self.root, width=12, font=('arial', 10))
        self.hex_entry.place(x=40, y=320)
        rgb_label = Label(self.root, text="Axis W ", font=('arial', 10, 'bold'))
        rgb_label.place(x=40, y=340)
        self.rgb_entry = Entry(self.root, width=12, font=('arial', 10))
        self.rgb_entry.place(x=40, y=360)
        hsv_label = Label(self.root, text="Axis X ", font=('arial', 10, 'bold'))
        hsv_label.place(x=40, y=380)
        self.hsv_entry = Entry(self.root, width=12, font=('arial', 10, 'bold'))
        self.hsv_entry.place(x=40, y=400)
        wavelength_label = Label(self.root, text="Axis Y ", font=('arial', 10, 'bold'))
        wavelength_label.place(x=40, y=420)
        self.wavelength_entry = Entry(self.root, width=12, font=('arial', 10, 'bold'))
        self.wavelength_entry.place(x=40, y=440)
        frequency_label = Label(self.root, text="Axis Z", font=('arial', 10, 'bold'))
        frequency_label.place(x=40, y=460)
        self.frequency_entry = Entry(self.root, width=12, font=('arial', 10, 'bold'))
        self.frequency_entry.place(x=40, y=480)
        full_label = Label(self.root, text="Code : ", font=('arial', 10, 'bold'))
        full_label.place(x=10, y=590)
        self.full_entry = Entry(self.root, width=40, font=('arial', 10, 'bold'))
        self.full_entry.place(x=7, y=590)

        C = Canvas(root, bg="white", height=250, width=400)
        C.create_line(0, 0, 3, 0)
        C.create_line(0, 0, 0, 3)
        C.create_line(3, 3, 3, 0)
        C.pack(side=TOP, padx=50, pady=50)

root = tk.Tk()
Viewer(root)
root.mainloop()
