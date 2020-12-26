from tkinter import *
import pytube

root = Tk()
root.geometry("500x500")
root.title("Youtube Downloader")
root.config(bg="black")


def download():
    url = youtube_link.get()
    try:
        youtube = pytube.YouTube(url)
        video = youtube.streams.first()
        video.download()
    except:
        error_msg = Label(root, text="invalid link", width=20, font=("arial", 10, "bold"))
        error_msg.place(x=150, y=30)



youtube_link = StringVar()
link_entry_space = Entry(root, textvar=youtube_link, width=60)
link_entry_space.place(x=30, y=250)

down_but = Button(root, text="download", bg="yellow", fg="brown", command=download)
down_but.place(x=410, y=246)

root.mainloop()
