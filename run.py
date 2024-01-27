from tkinter import *
from customtkinter import *
from PIL import ImageTk, Image
import threading

class Widget:
    def __init__(self):
        self.root = CTk()
        set_appearance_mode("system")
        
        self.root.title('Nemo')
        self.root.geometry('400x450')

        self.on = True

        def togglemode():
            current_bg = self.root.cget("bg")
            if current_bg == "gray14":
                set_appearance_mode("light")
            else:
                set_appearance_mode("dark")

        def update_button_appearance():
            if self.on:
                self.button.config(state=NORMAL)
            else:
                self.button.config(state=DISABLED)

        photo = ImageTk.PhotoImage(file='Data//Nemo_logo.png')
        self.button = Button(master=self.root, image=photo, command=self.clicked)
        self.button.pack(pady=80)

        night_btn = ImageTk.PhotoImage(Image.open('Data//Dark_Light.png'))
        self.my_button = Button(self.root, image=night_btn, command=lambda: (togglemode(), update_button_appearance()), borderwidth=0)
        self.my_button.pack(side='right')

        self.root.mainloop()

    def clicked(self):
        # Toggle between "on" and "off" states
        self.on = not self.on

        if self.on:
            # Run the 'run' function in a separate thread
            threading.Thread(target=self.run_in_thread).start()

    def run_in_thread(self):
        from main import run
        run()

if __name__ == '__main__':
    widget = Widget()
