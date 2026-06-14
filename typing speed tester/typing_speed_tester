from tkinter import *
import time
import random
start_time = 0
root = Tk()
root.geometry("400x500")
root.config(bg="#84B4CC",)

tester_lab = Label(root,bg="black",fg="white",text="TYPING SPEED TESTER",font=("lucida 15 bold"))
tester_lab.pack(fill=X)

test_quest = ("The quick brown fox jumps over the lazy dog",
"Typing fast is fun and very useful",
"Python is a popular programming language",
"Practice makes a person perfect",
"I like to read books on rainy days",
"I’m not lazy, I’m just in energy-saving mode",
"This sentence exists only to confuse your fingers",
"Read, write, and learn",
"She sells seashells",
"Time waits for no one",
)



def strt():
    text_box.delete(1.0,END)
    stop_btn.config(state="normal")
    wpm_lab.config(text="WPM: ")
    acc_lab.config(text="ACCURACY: ")
    global start_time
    rand = random.choice(test_quest)
    start_time = time.time()
    sentence_lab.config(text=f"SENTENCES: {rand}")

def stp():
    global start_time
    end_time = time.time()

    user_type = text_box.get(1.0, END).strip()
    time_taken = end_time - start_time

    time_in_min = time_taken / 60
    words_len = len(user_type.split())

    if time_in_min > 0:
        wpm = words_len / time_in_min
        wpm_lab.config(text=f"WPM: {wpm:.2f}")
        stop_btn.config(state="disable")


    full_text = sentence_lab.cget("text")
    target = full_text.replace("SENTENCES: ", "").strip()

    correct = 0
    for i in range(min(len(target), len(user_type))):
        if target[i] == user_type[i]:
            correct += 1

    if len(target) > 0:
        accuracy = (correct / len(target)) * 100
    else:
        accuracy = 0.0

    acc_lab.config(text=f"ACCURACY: {accuracy:.2f}%")







sentence_lab = Label(root,bg="#84B4CC",wraplength=370,text="SENTENCE: ",font=("lucida 15 bold"))
sentence_lab.pack(anchor=W,padx=30,pady=15)

strt_btn = Button(root,text="START",font=("lucdia 15 bold"),command=strt)
strt_btn.pack(padx=30,fill=X)


# e1_var = StringVar()
# e1_ent = Entry(root,textvariable=e1_var,font=("lucida 15 bold"))
# e1_ent.pack(fill=X,padx=30,pady=15)

text_box = Text(root,font=("lucida 15 bold"),wrap="word",height=5,width=30,)
text_box.pack(pady=10)


stop_btn = Button(root,text="CALCULATE",font=("lucdia 15 bold"),command=stp)
stop_btn.pack(padx=30,fill=X)

wpm_lab = Label(root,bg="#84B4CC",text="WPM: ",font=("lucida 15 bold"))
wpm_lab.place(x=30,y=360)

acc_lab = Label(root,bg="#84B4CC",text="ACCURACY: ",font=("lucida 15 bold"))
acc_lab.place(x=30,y=400)
root.mainloop()
