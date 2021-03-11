from ..download.single_video import Video
from tkinter import messagebox, Label, Button, FALSE, Tk, Entry, END

def download_video():
    #TODO: Add user-defined directory to download mp4
    try:
        yt = Video(url_text.get().strip(), "./resources")
        yt.valid_url()
    except Exception:
        messagebox.showinfo("ERROR", "Please enter a valid YouTube url!", icon="warning")
        print("Not a valid arguement")
    else:
        window.title(f'Downloading {yt.title.upper()}...')
        yt.download()
        print("Video Downloaded at ./resources/")
        messagebox.showinfo("SUCCESSFUL", f'{yt.title.upper()} downloaded at "/YTV-DOWNLOAD/resources/" directory', icon="info")
        clr_url()

# def get_url():
#     url = url_text.get()
#     print(url)
    
def clr_url():
    window.title("YouTube Video Download")
    url_text.delete(0, END)
    url_text.insert(0, "https://www.youtube.com/watch?v=")
    
# Set window geometry
window = Tk()
window.resizable(width=FALSE, height=FALSE)
window.title("YouTube Video Download")
window.geometry("520x200")

display_text = "The URL to the YouTube Video =>"

# Create Entry and Label
message = Label(window, text=display_text, font="Calibri 14", pady=15)
url_text = Entry(window, width=40, font="Calibri 16")
clr_url()

# Download and Clear buttons
download = Button(text="Download", command=download_video, font="Calibri 14", width=15, pady=5).place(y=110, x=90)
clear = Button(text="Reset", font="Calibri 14", width=15, pady=5, command=clr_url).place(y=110, x=270)

message.pack()
url_text.pack()

#Main Starter
window.mainloop()