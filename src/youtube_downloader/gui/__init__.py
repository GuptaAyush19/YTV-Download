from ..download.single_video import Video
from tkinter import messagebox, Label, Button, FALSE, Tk, Entry, LEFT, END


# def try_login():
#     print("Trying to login...")
#     if url_text.get() == username:
#         messagebox.showinfo("-- COMPLETE --", "You Have Now Logged In.", icon="info")
#     else:
#         messagebox.showinfo("-- ERROR --", "Please enter valid infomation!", icon="warning")

def download_video():
    try:
        yt = Video(url_text.get().strip(), "./resources")
    except Exception:
        messagebox.showinfo("ERROR", "Please enter a valid YouTube url!", icon="warning")
        print("Not a valid arguement")
    else:
        yt.download()

def get_url():
    url = url_text.get()
    print(url)
    
def clr_url():
    url_text.delete(0, END)
    url_text.insert(0, "https://www.youtube.com/watch?v=")
    
#Gui Things
window = Tk()
window.resizable(width=FALSE, height=FALSE)
window.title("YouTube Video Downloader")
window.geometry("520x200")

display_text = "The URL to the YouTube Video =>"

#Creating the username & password entry boxes
message = Label(window, text=display_text, font="Calibri 14", pady=15)
url_text = Entry(window, width=40, font="Calibri 16")
clr_url()

#attempt to login button
download = Button(text="Download", command=download_video, font="Calibri 14", width=15, pady=5).place(y=100, x=90)
cancel = Button(text="Reset", font="Calibri 14", width=15, pady=5, command=clr_url).place(y=100, x=270)

message.pack()
url_text.pack()
# download.pack()
# cancel.pack()


#Main Starter
window.mainloop()