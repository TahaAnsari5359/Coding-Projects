from tkinter import *
import sounddevice as sd
import numpy as np
import tkinter.filedialog as fd
from scipy.io.wavfile import write
from PIL import Image,ImageTk
import tkinter.messagebox as tmsg
import threading
import os, sys


root = Tk()
root.geometry("300x400")
root.config(bg="#93EE5F")
root.resizable(False,False)
root.title("Voice Recorder")
main_lab = Label(root,bg="#83D660",text="VOICE RECORDER",font=("Algerian 15 bold"))
main_lab.pack(fill=X)

def resource_path(relative_path):
    try:
        
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

img = Image.open(resource_path("record.png"))
simg = Image.open(resource_path("stoprec.png"))




fs = 44100
recording = []
is_recording = False
stream = None

def callback(indata, frames,status,time):
    if status:
        recording.append(indata.copy())
          

def start_rec():
    global stream, is_recording, recording
    if is_recording:
        return
    recording.clear()
    is_recording = True
    status_lab.config(text="Recording...", bg="red", fg="white")


    threading.Thread(target=record_thread, daemon=True).start()



def record_thread():
        global stream
        stream = sd.InputStream(samplerate=fs, channels=2, dtype='int16', callback=callback)
        with stream:
            while is_recording:
                sd.sleep(100)



def stop_recording():
    global is_recording
    if not is_recording:
        return
    is_recording = False
    status_lab.config(text="  Recording stopped", bg="green", fg="white",)

    if not recording:
        tmsg.showwarning("Warning", "No audio recorded!")
        return

    audio = np.concatenate(recording, axis=0)
    file = fd.asksaveasfilename(defaultextension=".wav", filetypes=[("WAV files","*.wav")], title="Save Recording")
    if file:
        write(file, fs, audio)
        status_lab.config(text=f"Saved at:\n{file}", wraplength=250)



           

btn_f = Frame(root,bg="#93EE5F")
btn_f.pack(side=BOTTOM,pady=20,)


resized = img.resize((50,50))

photo = ImageTk.PhotoImage(resized)







speak_btn = Button(btn_f,bg="#93EE5F",bd=0,image=photo,font=("lucida 10 bold"),command=start_rec)

speak_btn.pack(side=LEFT,padx=15)

    

sresized = simg.resize((50,50))

sphoto = ImageTk.PhotoImage(sresized)






stop_btn = Button(btn_f,bg="#93EE5F",bd=0,image=sphoto,font=("lucida 10 bold"),command=stop_recording)

stop_btn.pack(padx=15)

status_lab = Label(root,bg="#93EE5F",text="",font=("lucida 15 bold"))
status_lab.pack(pady=40,fill=X)


root.mainloop()






# ----------------------------Uses Duration Mode-------------------



# duration = Label(root,bg="#93EE5F",text="Enter duration: ",font=("lucida 13 bold"))
# duration.pack(anchor=W,padx=30,pady=33)
# e1_var = StringVar()

# e1_ent = Entry(root,width=4,relief=GROOVE,bd=5,textvariable=e1_var,font=("lucida 15 bold"))
# e1_ent.place(x=165,y=60)
# secs = Label(root,bg="#93EE5F",text="sec",font=("lucida 13 bold"))
# secs.place(x=225,y=63)







# def speak():
#     try:
#         duration=int(e1_var.get())
        
        
    
#         audio = sd.rec(int(duration * fs), samplerate=fs,channels=2,dtype='int16')
#         sd.wait()
        
#         status_lab.config(text="recording finished..",bg="green",)
        
#         file = fd.asksaveasfilename(defaultextension=".wav",filetypes=[("WAV files","*.wav")],title="SAVING")
        
#         if file:
#             write(file,fs,audio)
#             status_lab.config(text=f"file saved at:  {file}",wraplength=200)

#         return audio
#     except:
#         tmsg.showwarning("warnning","Please Enter Seconds")
#         return
    
# def updates():
#         if (e1_var.get()) == "":
#             tmsg.showwarning("warnning","Please Enter Seconds")
#             e1_var.set("")
#             return
#         try:
#             int(e1_var.get()) 
#         except ValueError:
#             tmsg.showwarning("Warning", "Please enter a valid number")
#             e1_var.set("")
#             return

        
#         status_lab.config(text="recording started..",bg="red",fg="white")
#         root.update()
#         root.after(300)
#         status_lab.config(text="recording started...",bg="red",fg="white")
#         root.update()
#         root.after(300)
#         status_lab.config(text="recording started....",bg="red",fg="white")
#         root.update()
#         root.after(300)
#         status_lab.config(text="recording started.....",bg="red",fg="white")
#         root.update()
#         root.after(300)
#         status_lab.config(text="recording started......",bg="red",fg="white")
#         root.update()
#         root.after(300)
#         threading.Thread(target=speak, daemon=True).start()
        
#  ----------------------------------------------------------------- 
