from tkinter import *


root = Tk()
background_image = PhotoImage(file="download.pgm")
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

root.mainloop()