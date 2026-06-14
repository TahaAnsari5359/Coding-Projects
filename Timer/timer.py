from tkinter import *
import tkinter.messagebox as tmsg
import winsound

root = Tk()
root.geometry("300x250")
root.title("Timer")
root.config(bg="#9A77F9")
root.resizable(False, False)

timer = 0
running = False

stop_watch = Label(root, text="TIMER", bg="black", fg="white", font=("lucida 15 bold underline"))
stop_watch.pack(fill=X)

Label(root, text="Minutes", bg="#9A77F9", font=("lucida 10 bold")).place(x=100, y=35)
Label(root, text="Seconds", bg="#9A77F9", font=("lucida 10 bold")).place(x=160, y=35)
colan = Label(root,text=":", bg="#9A77F9",font=("lucida 15 bold"))
colan.place(x=148,y=60)

e2_var = StringVar() 
e3_var = StringVar()  

e2_ent = Entry(root, width=4, textvariable=e2_var, font=("lucida 15 bold"), justify=CENTER)
e2_ent.place(x=100, y=60)
e3_ent = Entry(root, width=4, textvariable=e3_var, font=("lucida 15 bold"), justify=CENTER)
e3_ent.place(x=160, y=60)

timer_lab = Label(root, bg="#9A77F9", text="00:00", font=("lucida 20 bold"))
timer_lab.pack(pady=80)

def strt():
    global timer, running
    if running and timer >= 0:
        mins, secs = divmod(timer, 60)
        timer_lab.config(text=f"{mins:02d}:{secs:02d}")
        if timer == 0:
            for i in range(5):
                winsound.Beep(1000, 500)
            running = False
        else:
            timer -= 1
            root.after(1000, strt)

def start_timer():
    if int(e2_var.get()) > 59 or int(e3_var.get()) > 59:
        tmsg.showerror("error","Range 0 to 59 only")
    else:
        global timer, running
        try:
            mins = int(e2_var.get())
            secs = int(e3_var.get())
            timer = mins * 60 + secs
            running = True
            strt()
        except:
            tmsg.showerror("ERROR", "Please enter valid numbers!")

def stop_timer():
    global running
    running = not running
    stop_btn.config(text="RESUME" if not running else "STOP")
    if running:
        strt()

def reset_timer():
    global running, timer
    running = False
    timer = 0
    timer_lab.config(text="00:00")



    
           


Button(root, text="START", bd=5, relief=GROOVE, font=("lucida 10 bold"), command=start_timer).place(x=30, y=200)
stop_btn = Button(root, text="STOP", bd=5, relief=GROOVE, font=("lucida 10 bold"), command=stop_timer)
stop_btn.place(x=120, y=200)
Button(root, text="RESET", bd=5, relief=GROOVE, font=("lucida 10 bold"), command=reset_timer).place(x=210, y=200)

root.mainloop()
