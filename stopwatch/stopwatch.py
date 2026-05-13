from tkinter import *
from tkinter import font as tkFont
import winsound

root = Tk()
root.geometry("370x600")
root.title('StopWatch')
root.config(bg="#DFDA0F")
stopwatch_lab = Label(root,bg="black",fg="white",text="STOPWATCH",font=("lucida 15 bold"))
stopwatch_lab.pack(fill=X)






# clock_font = tkFont.Font(family="Consolas", size=40, weight="bold")



clock_font = tkFont.Font(family="DS-Digital", size=55, weight="bold")



















prev_milisec = 0
milisecc = 0
timer = 0
running = False
after_id = None
prev_lap_time = 0

lap = 0


def strt():
    reset_btn.place(x=130,y=530)
    lap_btn.place(x=230,y=530)
    global timer, running, after_id
    if running:
        timer += 10  # 10 milliseconds increment

        mins, secs = divmod(timer // 1000, 60)
        milisec = timer % 1000

        watch_timer.config(text=f"{mins:02d}:{secs:02d}:{milisec:03d}")
        after_id = root.after(10, strt)


def stop():
    global lap, running, timer, prev_lap_time, after_id, prev_milisec
    if running:
        running = False
        stop_btn.config(text="Resume")
        

        

        if after_id:
            root.after_cancel(after_id)
    else:
        running = True
        stop_btn.config(text="Stop")
        strt()




def start():
    global running
    if not running:
        running = True
        strt()


def reset():
    global running,timer,lap
    running=False
    timer=0
    lap=0
    watch_timer.config(text="00:00:000")
    lap_timer.config(text="")
    stop_btn.config(text="START")
    list_box.delete(0,END)


def laps():
        global lap, running, timer, prev_lap_time, after_id, prev_milisec
        curr_lap = timer
        diff = curr_lap - prev_lap_time
        prev_lap_time = curr_lap
        lap += 1
        lap_timer.config(text=f"Lap: {lap}")

       
        curr_milisec = timer % 1000
     
        mili_diff = curr_milisec - prev_milisec
        if mili_diff < 0:
            mili_diff += 1000  
        prev_milisec = curr_milisec 

      
        mins, secs = divmod(timer // 1000, 60)
        milisec = timer % 1000

        m2, s2 = divmod(diff // 1000, 60)
        milidiff = diff % 1000

       
        data = f"{mins:02d}:{secs:02d}:{milisec:03d}    +({m2:02d}:{s2:02d}:{milidiff:03d})    Lap: {lap}"
        scroll_bar.pack(fill=Y, side=RIGHT)
        list_box.pack(pady=10, fill=X, padx=10)
        list_box.insert(END, data)
        winsound.Beep(1000,500)




stop_btn = Button(root,bg="red",width=10,height=2,relief=GROOVE,bd=5,fg="white",text="START",font=("lucida 10 bold italic"),command=stop)
stop_btn.place(x=30,y=530)

reset_btn = Button(root,width=10,height=2,relief=GROOVE,bd=5,bg="#F57627",text="RESET",font=("lucida 10 bold italic"),command=reset)



lap_btn = Button(root,width=10,relief=GROOVE,bd=5,height=2,bg="#F57627",text="LAP",font=("lucida 10 bold italic"),command=laps)


watch_timer = Label(root,text="00:00:000",bg="#DFDA0F",font=clock_font)
watch_timer.pack(pady=60)

lap_timer = Label(root,bg="#DFDA0F",font=("lucida 15 bold"))
lap_timer.pack(pady=20)


scroll_bar = Scrollbar(root,)

list_box = Listbox(root,yscrollcommand=scroll_bar.set,height=7,width=6,font=("lucida 15 bold"))



scroll_bar.config(command=list_box.yview)
root.mainloop() 
