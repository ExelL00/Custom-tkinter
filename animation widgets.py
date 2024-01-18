import customtkinter as ctk
from random import choice


class SlidePanel(ctk.CTkFrame):
    def __init__(self,parent,start_pos,end_pos):
        super().__init__(master=parent)

        #general setup
        self.start_pos=start_pos#1
        self.end_pos=end_pos#0.7
        self.width=abs(self.start_pos-self.end_pos)#0.3

        #animation logic
        self.pos=start_pos
        self.in_start_pos=True

        self.place(relx=self.start_pos,rely=0.05,relwidth=self.width,relheight=0.9)


    def animate(self):
        if self.in_start_pos:
            self.animation_forward()
        else:
            self.animation_backwards()
    def animation_forward(self):
        if self.pos>self.end_pos:#1>0.7
            self.pos-=0.008
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10,self.animation_forward)
        else:
            self.in_start_pos=False


    def animation_backwards(self):
        if self.pos<self.start_pos:#0.7<1
            self.pos+=0.008
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10,self.animation_backwards)
        else:
            self.in_start_pos=True


#window
window=ctk.CTk()
window.title("animation widgets")
window.geometry("400x400")

slide_panel=SlidePanel(window,1,0.7)
ctk.CTkLabel(slide_panel,text='Label 1').pack(expand=True,fill='both',padx=2,pady=10)
ctk.CTkLabel(slide_panel,text='Label 2').pack(expand=True,fill='both',padx=2,pady=10)
ctk.CTkButton(slide_panel,text='Button',corner_radius=10).pack(expand=True,fill='both',padx=2,pady=10)
ctk.CTkTextbox(slide_panel,fg_color=('#dbdbdbd','#2b2b2b')).pack(expand=True,fill='both',padx=2,pady=10)

#button
button_x=0.5
button=ctk.CTkButton(window,text='toggle button',command=slide_panel.animate)
button.place(relx=button_x,rely=0.5,anchor='center')

#run
window.mainloop()