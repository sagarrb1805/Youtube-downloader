from tkinter import *
import pytube

root = Tk()
root.geometry("500x500")
root.title("Youtube Downloader")
root.config(bg="black")


def download():
    url = youtube_link.get()

    youtube = pytube.YouTube(url)

    video = youtube.streams.first()
    video.download()


youtube_link = StringVar()
link_entry_space = Entry(root, textvar=youtube_link, width=60)
link_entry_space.place(x=30, y=250)

down_but = Button(root, text="download", bg="yellow", fg="brown", command=download)
down_but.place(x=410, y=246)


root.mainloop()
