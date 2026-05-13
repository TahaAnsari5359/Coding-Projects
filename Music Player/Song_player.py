from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tmsg
import os
from tkinter import filedialog
from pygame import mixer
from mutagen.mp3 import MP3
import time




import sys
import os

def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
















root = Tk()
root.title("Song Player")
mixer.init()
root.config(bg="black",)
root.geometry("600x500")
root.resizable(False,False)
total_len = 0
progress = None

play_img = PhotoImage(file=resource_path("play.png"))
pause_img = PhotoImage(file=resource_path("pause.png"))
resume_img = PhotoImage(file=resource_path("resume.png"))
stop_img = PhotoImage(file=resource_path("stop.png"))




def play():
    try:
        volumess = float(selected_op.get())
        mixer.music.play()
        mixer.music.set_volume(volumess)
    except:
        tmsg.showerror("error","please select song")

    

def pause():
    mixer.music.pause()
    

def stop():
    mixer.music.stop()

def resume():
    mixer.music.unpause()


def select():
    global total_len
    global progress
    file = filedialog.askopenfilename(filetypes=[("MP3","*.mp3")])
    
    if file:
    
            mixer.music.load(file)
            geting = os.path.basename(file)
            music_lab.config(text=geting)
            audio = MP3(file)
            total_len = audio.info.length
            progress.config(orient=HORIZONTAL,length=300,mode='determinate')
            progress.pack()
            update_len()

def update_len():
    global progress
    global total_len
    current = mixer.music.get_pos() / 1000

    progress['value'] = (current / total_len) * 100
    root.after(1000, update_len)


progress = ttk.Progressbar(root)


music_player = Label(root,bg="black",fg="white",text="MUSIC PLAYER",font=("lucida 20 bold underline italic"))
music_player.pack(pady=20)



resized_p = play_img.subsample(1,1)




play_btn = Button(root,height=50,cursor="cross",relief=GROOVE,borderwidth=3,image=resized_p,font=("lucida 15 bold"),command = play)
play_btn.place(x=30,y=430)


resized_pu = pause_img.subsample(1,1)


pause_btn = Button(root,height=50,cursor="fleur",relief=GROOVE,borderwidth=3, image=resized_pu,text="⏸",font=("lucida 15 bold"),command=pause)
pause_btn.place(x=100,y=430)




resized_r = resume_img.subsample(1,1)

resume_btn = Button(root,height=50,cursor="circle",relief=GROOVE,borderwidth=3,image=resized_r,text="⇄",font=("lucida 15 bold"),command=resume)
resume_btn.place(x=160,y=430)



resized_s = stop_img.subsample(1,1)


stop_btn = Button(root,height=50,cursor="spider",relief=GROOVE,borderwidth=3,image=resized_s,text="⏹",font=("lucida 15 bold"),command=stop)
stop_btn.place(x=240,y=430)

music_lab = Label(root,bg="black",fg="white",wraplength=300,font=("lucida 15 bold"))
music_lab.pack(pady=50)




choose_song = Button(root,relief=GROOVE,borderwidth=3,text="select song",font=('lucida 15 bold'),command=select)
choose_song.place(x=450,y=430)


values = "0.0","0.5","1.0"
selected_op = StringVar()
selected_op.set("0.5")
drop_down = OptionMenu(root,selected_op,*values)
drop_down.place(x=30,y=200)

root.mainloop()
