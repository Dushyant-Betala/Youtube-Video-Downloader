from tkinter import *
from tkinter import filedialog
import tkinter.font as tkFont

from pytube import YouTube

#this creates the GUI for the Downloader using Tkinter Library
root = Tk()
root.geometry("960x540")
root.resizable(width=False, height= False)
root.title("Youtube Video Downloader")
root.configure(bg="#FF0000")

Downloaded_font= tkFont.Font(family="Helvetica", size = 20, weight= 'bold')

font_1= tkFont.Font(family="Times New Roman", size = 15, weight= 'bold')

redbar= Label(root, text="", bg="#000000")
redbar.place(x=0,y=0,height=25, width = 960, anchor=NW)

des = Label(root, text = "Please enter the video link you wish to download from YouTube", font=font_1, fg="Black",bg="#FF0000")
des.place(x=200, y =40)

lk = StringVar()
link = Entry(root, width =130 , bg ="white", textvariable= lk)
link.place(x=90, y=90)

#This Function gets the URL and storage location from the GUI and downlaods the video from the URL into the location file
def download():
    url=YouTube(lk.get()) 
    vid = url.streams.get_highest_resolution()
    vid.download(output_path=path_entry.get())
    Label(root, text= "The Video has been Dowloaded!", bg='#FF0000', fg = "white", font=Downloaded_font).place(x= 220, y =450 )
    link.delete(0,END)

 
def path_selection():
    folder_selected= filedialog.askdirectory()
    path_entry.delete(0, END)
    path_entry.insert(0, folder_selected)


dowload_button = Button(root, text="Download!", bg="black", fg="White", font='Arial 15 bold',width=30,command=download).place(x=250,y =400)

select_path = Label(root, text="Please select the path where you wish to store the file", font=font_1, fg="Black",bg="#FF0000" ).place(x=220, y = 190)
path_entry = Entry(root, width = 110, bg ="white")
path_entry.insert(0,"Path")
path_entry.place(x=90, y=230)

path_button = Button(root, text="Select path", bg="black", fg="White", font='Arial 7 bold',width=18,command=path_selection)
path_button.place(x=765, y=230 )



blackbar = Label(root, text="", bg ='#000000')
blackbar.place(x=0,y=515,height=25, width = 960)

root.mainloop()
