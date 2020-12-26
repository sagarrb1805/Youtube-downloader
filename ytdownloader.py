from tkinter import *
import pytube

root = Tk()
root.geometry("500x500")
root.title("Youtube Downloader")
root.config(bg="black")

youtubelink = StringVar()
linkentry_space = Entry(root, textvar=youtubelink, width=60)
linkentry_space.place(x=30, y=250)

down_but = Button(root, text="download", bg="yellow", fg="brown")
down_but.place(x=410, y=246)


root.mainloop()
