# Library Call
from tkinter import Tk
from tkinter import ttk
from pytube import YouTube


# Window Main
window = Tk()
window.title("YouTube Downloader")
frame = ttk.Frame(window)
frame.pack()

# Guide
guide = ttk.Label(frame, text="Enter a YouTube Link (example: https://youtu.be/uvvVY4J_OM8)")
guide.grid(column=0, row=0, padx=100)

# Link
urlLink = ttk.Entry(frame, width=40, justify="center")
urlLink.grid(column=0, row=1, padx=100, pady=15)


# Function To Download
def downloader():
    # Get Link
    link = urlLink.get()

    # Generate
    generate = YouTube(link)

    # Get Stream
    stream = generate.streams.get_highest_resolution()

    # Download
    download = stream.download('D:\YouTube Downloader\Downloads')


# Link Button
urlButt = ttk.Button(frame, width=20,text="Download", command=downloader)
urlButt.grid(column=0, row=2)


# Close Button
close = ttk.Button(frame, text="Close", command=window.destroy)
close.grid(column=0, row=3, pady=15)



# Main Loop Window
window.mainloop()