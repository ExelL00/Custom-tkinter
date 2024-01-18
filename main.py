import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

window=ctk.CTk()
window.title("custom tkinter")
window.geometry("400x300")

string_var=ctk.StringVar(value='a custom string')
label=ctk.CTkLabel(
    window,
    text="a label ctk",
    fg_color=('blue','red'),
    text_color='green',
    corner_radius=10,
    textvariable=string_var)
label.pack()

button=ctk.CTkButton(
    window,
    text='A button ctk',
    fg_color='red',
    text_color='black',
    hover_color='yellow',
    command=lambda :ctk.set_appearance_mode('light'))
button.pack()

frame=ctk.CTkFrame(window,fg_color='blue')
frame.pack()

slider=ctk.CTkSlider(frame)
slider.pack()

switch=ctk.CTkSwitch(
    frame,
    text='exercise switch',
    fg_color=('blue','red'),
    progress_color='pink',
    button_color='green',
    button_hover_color='yellow',
    corner_radius=2)
switch.pack()


#run
window.mainloop()