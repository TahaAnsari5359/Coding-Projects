import tkinter as tk
import customtkinter as ctk
import tkinter.messagebox as tmsg


root = ctk.CTk()
root.geometry("400x400")
root.configure(fg_color="#DF9D5C")

main_lab = ctk.CTkLabel(root,text="WORD COUNTER",text_color="white",fg_color="#4E57D2",font=("lucida",25,"bold"))
main_lab.pack(fill="x")


def counts():
    text = text_area.get(1.0,"end-1c").strip()


    if text == "":
        tmsg.showerror("error","Enter Text To calculate")
        return
    
    wordss = len(text.split())
    without_space = text.replace(" ","")
    char = len(without_space)
    
    lines = text.count("\n")+1
    words_lab.config(text=f"COUNTED WORDS: {wordss}")
    char_lab.config(text=f"COUNTED CHARACTERS: {char}")
    lines_lab.config(text=f"COUNTED LINES {lines}")
    





insert_word = tk.Label(root,bg="#DF9D5C",text="INSERT WORD",font=("lucida 13 bold"))
insert_word.place(x=30,y=50)


text_area = ctk.CTkTextbox(root,width=350,height=100,font=("lucida",14,"bold"))
text_area.pack(pady=70)

words_lab = tk.Label(root,bg="#DF9D5C",text="COUNTED WORDS: ",font=('lucida 13 bold'))
words_lab.place(x=30,y=220)



char_lab = tk.Label(root,bg="#DF9D5C",text="COUNTED CHARACTERS: ",font=('lucida 13 bold'))
char_lab.place(x=30,y=250)




lines_lab = tk.Label(root,bg="#DF9D5C",text="COUNTED LINES: ",font=('lucida 13 bold'))
lines_lab.place(x=30,y=280)




count_btn = tk.Button(root,bg="#8BE28A",text="COUNT",width=20,font=("lucida 13 bold"),command=counts)
count_btn.pack(side="bottom",pady=20)





root.mainloop()
