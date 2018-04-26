from tkinter import *
from ScreenWriter import ScreenWriter
import sys
import threading


def play_command():
    recorder.startRecord()

def stop_command():
    recorder.stopRecord()



play = threading.Thread(target=play_command, name='Recording')
stop = threading.Thread(target=stop_command, name='stop')

window=Tk()
window.geometry("300x40")
window.title("Screen Recorder")


display_width  = window.winfo_screenwidth()
display_height = window.winfo_screenheight()

print("Width: " + str(display_width))
print("Height: " + str(display_height))
switch = True
recorder = ScreenWriter(switch,display_width,display_height)

playImg =PhotoImage(file='Play.png')
playBT = Button(window,image=playImg,command=play.start)
playBT.grid(row=0,column=0)

stopImg = PhotoImage(file='stop.png')
stopBT = Button(window,image=stopImg,command=stop.start)
stopBT.grid(row=0,column=1)


window.mainloop()
