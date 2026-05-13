import customtkinter as ctk
import tkinter as tk
import pyttsx3
import tkinter.filedialog as fd

root = ctk.CTk()
root.geometry("400x520")
root.title("Text To Speech")  
root.configure(fg_color="cyan")
ctk.set_appearance_mode("System")          
ctk.set_default_color_theme("blue")
  
engin = pyttsx3.init()


main_lab = tk.Label(root, bg="black",fg="white", text="INPUT TEXT TO SPEAK", font=("lucida 14 bold"))
main_lab.pack(fill="x")

def say():
    vols = int(slider.get())
    engin.setProperty("rate",150)
    if vols == 0:
        engin.setProperty("volume",0.0)
    elif vols == 1:
        engin.setProperty("volume",0.5)
    else:
        engin.setProperty("volume",1.0)
    data = text_area.get(1.0, "end")
    engin.say(data)
    engin.runAndWait()
    
def upl():
    file = fd.askopenfilename(filetypes=[("Text file","*.txt"),("All files","*.*")])
    if file:
        with open(file, "r") as f:
            content = f.read()
            text_area.delete(1.0,"end")
            text_area.insert(1.0,content)
        

def clr():
    engin.setProperty("rate",150)
    engin.say("Data Cleared Successfully")
    
    engin.runAndWait()
    text_area.delete(1.0,"end")


text_area = tk.Text(root, relief="groove",bd=5, height=18, wrap="word", width=32, font=("lucida", 12, "bold"))
text_area.pack(pady=15, padx=20)


btn_frame = ctk.CTkFrame(root,fg_color="cyan")
btn_frame.pack(pady=10)


btn_ctk = ctk.CTkButton(
    btn_frame,
    corner_radius=10,
    text="SPEAK",
    font=("lucida", 13, "bold"),
    command=say,
    width=150,text_color="black",
    hover_color="lime", border_width=2,border_color = "#444"
)
btn_ctk.grid(row=0, column=0, padx=10, pady=5)


upload_ctk = ctk.CTkButton(
    btn_frame,
    corner_radius=10,
    text="UPLOAD TEXT",
    font=("lucida", 13, "bold"),
    width=150,text_color="black",border_width=2,border_color = "#444",hover_color="lime",command=upl
)
upload_ctk.grid(row=0, column=1, padx=10, pady=5)



clr_btn = ctk.CTkButton(root,corner_radius=10,width=150,text_color="black",border_width=2,border_color = "#444",hover_color="lime",text="CLEAR",font=("lucida",13,"bold"),command=clr)
clr_btn.pack(side="bottom",pady=10)





slider = ctk.CTkSlider(root,from_=0,to=2,number_of_steps=2,orientation="vertical",)
slider.place(x=30,y=100)



root.mainloop()
