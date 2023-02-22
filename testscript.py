import os
from time import sleep
from random import randint, uniform, choice
from threading import Thread

# GUI Imports
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


# Keyboard functions
import keyboard

# Mouse movement
import mouse

import pynput
import win32api
import pyautogui


recoil_bool = False
recoil_key = "/"

USUAL_FONT = "Arial"


class Interface(tk.Tk, Thread):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        Thread.__init__(self)

        self.title("Test GUI")

        self.geometry("500x350")

        self.main_body = MainBody(self)
        self.main_body.grid(row=0, column=0)


class MainBody(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        toggles_lbl = ttk.Label(self, text="Recoil S/cript", font=(USUAL_FONT, 16))
        toggles_lbl.grid(row=0, column=0, sticky="W")

        ak_recoil_lbl = ttk.Label(self, text="AK Toggle Button:", font=(USUAL_FONT, 14))
        ak_recoil_lbl.grid(row=1, column=0, sticky="E")

        self.recoil_bool_var = tk.IntVar()
        self.recoil_checkbox = tk.Checkbutton(
            self,
            variable=self.recoil_bool_var,
            command=lambda: self.recoil_bool_check(self.recoil_bool_var),
        )
        self.recoil_checkbox.grid(row=1, column=1, sticky="W")

    def recoil_bool_check(self, var_int=None):
        global recoil_bool

        if var_int == None:  # Called from outside layout
            if recoil_bool:
                self.recoil_checkbox.select()
            else:
                self.recoil_checkbox.deselect()
            return

        if var_int.get() == 1:  # 1 = True, 0 = False
            recoil_bool = True
        else:
            recoil_bool = False


#   class Recoil_Loop(Thread):
#       def __init__(self, *args, **kwargs):
#           super().__init__(self)


def check_recoil_bool():
    global recoil_bool
    if keyboard.is_pressed(recoil_key):
        print("Here")
        recoil_bool = not recoil_bool
        app.main_body.recoil_bool_check()
        sleep(0.3)


def recoil_loop():
    global recoil_bool

    while True:  # Begin a loop / Infinite Loop
        sleep(0.1)  # Every 0.1 seconds
        check_recoil_bool()

        while recoil_bool:  # Loop only if recoil_bool is on
            sleep(0.01)
            check_recoil_bool()

            if win32api.GetAsyncKeyState(0x01) != 0:
                mouse.move(-35, 75, False)


if __name__ == "__main__":
    app = Interface()
    recoil_thread = Thread(target=recoil_loop)

    recoil_thread.start()
    app.start()

    app.mainloop()
