from tkinter import *
import pytube
import tkinter.messagebox

root = Tk()
root.geometry("500x500")
root.title("Youtube Downloader")
root.config(bg="black")


def download():
    url = youtube_link.get()
    try:
        youtube = pytube.YouTube(url)
        try:
            video = youtube.streams.first()
            video.download()
            success = Label(root, text="Video downloaded successfully!!", font=("arial", 10, "bold"))
            success.place(x=150, y=30)
        except:
            error_message = Label(root, text="something went wrong", width=20, font=("arial", 10, "bold"))
            error_message.place(x=150, y=30)
            tkinter.messagebox.showerror("Sorry !!", "Action cannot be performed at this moment")

    except:
        invalid_link_label = Label(root, text="invalid link", width=20, font=("arial", 10, "bold"))
        invalid_link_label.place(x=150, y=30)
        tkinter.messagebox.showerror("Sorry !!", "The link seems to be invalid")


youtube_link = StringVar()
link_entry_space = Entry(root, textvar=youtube_link, width=60)
link_entry_space.place(x=30, y=250)

down_but = Button(root, text="download", bg="yellow", fg="brown", command=download)
down_but.place(x=410, y=246)

root.mainloop()
