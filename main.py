from tkinter import *
from tkinter import ttk
import tkinter as tk
from winsound import *
import random
from time import sleep


class game:

    def __init__(self, root):

        def popupmsg(msg):
            popup = tk.Tk()
            popup.geometry("150x100")
            popup.wm_title("Nice!")
            label = ttk.Label(popup, text=msg, font=("Courier New", 16, 'bold'))
            label.place(x=15,y=15)
            label.pack()
            B1 = Button(popup, padx=30, pady=14, bd=4,command = popup.destroy, bg='white', text="Ok", font=("Courier New", 16, 'bold'))
            popup.resizable(width=False, height=False)
            B1.pack()
            popup.mainloop()

        def click(x , y):
            button1.place(x=x, y=y)
            PlaySound("Evelynn_Ban.wav", SND_ASYNC | SND_FILENAME)
            popupmsg("You Win")

        def click2(x, y):
            button12.place(x=x, y=y)
            PlaySound("Evelynn_Ban.wav", SND_ASYNC | SND_FILENAME)
            sleep(2)
            popupmsg("You Win")

        def moan(event):
            PlaySound("Evelynn.attack15.wav", SND_ASYNC | SND_FILENAME)

        random.randint(0, 300)
        root.geometry("700x700")
        root.resizable(height=0, width=0)
        root.title("Touch Me")

        background_label = tk.Label(root, image=background_image)
        background_label.bind('<Button-1>', moan)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)




        def test(event):
            button1.place(x=random.randint(0,430),y=random.randint(0,430))

        def test2(event):
            button12.place(x=random.randint(0, 430), y=random.randint(0, 430))

        button1 =  Button(root, padx=14, pady=14, bd=4, bg='white', text="Click Me",
                      command=lambda: click(random.randint(0, 430),
                                            random.randint(0, 430)), font=("Courier New", 16, 'bold'))
        button1.bind("<Enter>", test)

        button1.place(x=260, y=263)

        button12 = Button(root, padx=14, pady=14, bd=4, bg='white', text="No Me",
                         command=lambda: click2(random.randint(0, 430),
                                               random.randint(0, 430)), font=("Courier New", 16, 'bold'))
        button12.bind("<Enter>", test2)

        button12.place(x=100, y=100)


root = Tk()
background_image = tk.PhotoImage(file="-engine-blood-moon-evelynn-wallpaper.ppm")
TestGame = game(root)

root.mainloop()

