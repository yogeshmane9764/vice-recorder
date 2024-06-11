# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 09:21:31 2024

@author: Yogesh
"""

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import sounddevice as sound
from scipy.io.wavfile import write
import time
import wavio as wv

root=Tk()
root.geometry("600x700+400+90")
root.resizable (False,False) 
root.title("Vice Recorder")
root.configure(background="#4a4a4a")


def Record():
    freq=44100
    dur=int(duration.get())
    recording=sound.rec(dur*freq,
                        samplerate=freq,channels=2)
    #timer
    try :
        temp=int(duration.get())
    except:
        print("Plese enter the right value")
    while temp:
        root.update()
        time.sleep(1)
        temp-= 1
        
        if(temp==0):
            messagebox.showinfo("Time Conutdown","Times up")
        Label(text=f"{str(temp)}",font="arial 30",width=4,background="#4a4a4a").place(x=230,y=590)
        
    sound.wait()
    write("recording.wav",freq,recording)


#icon
image_icon=PhotoImage(file="Record.png")
root.iconphoto(False,image_icon)


#logo
photo=PhotoImage(file="Record.png")
myimage=Label(image=photo,background="#4a4a4a")
myimage.pack(padx=5,pady=5)

#name

Label(text="Vice Recorder",font="arial 30 bold",background="#4a4a4a",fg="white").pack()

#entrybox
duration=StringVar()
entry=Entry(root,textvariable=duration,font="arial 30",width=15).pack(pady=10)
Label(text="Enter a time second",font="arial 15",background="#4a4a4a",fg="white").pack()

#button
record=Button(root,font="arial 15",text="recored",background="red",fg="white",border=0,command=Record).pack(pady=30)

root.mainloop()

