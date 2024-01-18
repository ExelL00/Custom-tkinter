import customtkinter as ctk
import  tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk

def stretch_image(event):
    global resized_tk

    #size
    width=event.width
    height=event.height
    print(width)

    #create img
    resized_image=image_original.resize((width,height))
    resized_tk= ImageTk.PhotoImage(resized_image)

    #place on the canvas
    canvas.create_image(0,0,image=resized_tk,anchor='nw')

def fill_image(event):
    global resized_tk

    #current ratio
    canvas_ratio=event.width/event.height

    #get coordinates
    if canvas_ratio>image_ratio:
        width=int(event.width)
        height=int(width/image_ratio)#ezby zachowac porporcje obrazu
        # print(width/image_ratio,width)
    else:
        height = int(event.height)
        width = int(height*image_ratio)


    resized_image=image_original.resize((width,height))
    resized_tk = ImageTk.PhotoImage(resized_image)
    # print(event.width/2,event.height/2,event.width,event.height)
    canvas.create_image(
        int(event.width/2),
        int(event.height/2),
        image=resized_tk,
        anchor='center')


window=tk.Tk()
window.title("Image")
window.geometry('600x400')


#gird layou
window.columnconfigure((0,1,2,3),weight=1,uniform='a')
window.rowconfigure(0,weight=1)

#import image
image_original=Image.open('image/image.jpg')
image_ratio=image_original.size[0]/image_original.size[1]

image_tk=ImageTk.PhotoImage(image_original)

python_dark=Image.open('image/dark.png').resize((30,30))
python_light=Image.open('image/light.png').resize((30,30))
python_dark_tk=ImageTk.PhotoImage(python_dark)

python_dark_ctk=ctk.CTkImage(
    light_image=python_dark,
    dark_image=python_light)

#widget
# label=ttk.Label(window,text='img',image=image_tk)
# label.pack()


button_frame=ttk.Frame(window)
button=ttk.Button(button_frame,text='A button',image=python_dark_tk,compound='right')
button.pack(pady=10)

button_ctk=ctk.CTkButton(button_frame,text='A button',image=python_dark_ctk,compound='right')
button_ctk.pack(pady=10)

button_frame.grid(column=0,row=0,sticky='nesw')

#canvas -> img
canvas=tk.Canvas(window,background='black',bd=0,highlightthickness=0,relief='ridge')#od bd do relife to ze canva nie ma obramowania
canvas.grid(column=1,columnspan=3,row=0,sticky='nsew')

canvas.bind('<Configure>',fill_image)


window.mainloop()