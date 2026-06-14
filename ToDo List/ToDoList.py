from tkinter import *
import tkinter.messagebox as tmsg
from tkinter import filedialog
root = Tk()
root.geometry("700x500")
root.title("Todo List")
root.configure(bg="cyan")

main_lab = Label(root,text="TODO LIST",bg="cyan", font=("lucida 25 bold underline"))
main_lab.pack(pady=15)

def addd():
    entry = e1var.get()
    if entry == "":
        tmsg.showinfo("Error", "Please Enter Items To add")
        
        
    else:
        list_box.insert(END, entry)
        e1var.set("")
        return
        
def clr():
    selected = list_box.curselection()
    for i in reversed(selected):
        list_box.delete(i)

def clrall():
    list_box.delete(0,END)


def save():
    try:
        items = list_box.get(0, END)
        if not items: 
            tmsg.showinfo("Error", "There are no items to save.")
            return
        
        file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("TXT file", ".txt")])
        if file:
            with open(file, "w") as f:
                for item in items:
                    f.write(item + "\n")
                    tmsg.showinfo("Succesfully","sucessfully saved")
                    root.destroy()
                    return
                    
    except Exception as e:
        tmsg.showinfo("Error", f"Could not save file:\n{e}")
        





e1var = StringVar()
e1_end = Entry(root, font=("lucida 20"), textvariable=e1var)
e1_end.place(x=50, y=100)

list_box = Listbox(root, width=25, height=12, font=("Lucida", 16))
list_box.place(x=370, y=100)

add_btn = Button(root, text="Add Items", width=20, font=("lucida 15"), command=addd)
add_btn.place(x=50, y=150)

clear_btn = Button(root, text="Clear Items", width=20, font=("lucida 15"), command=clr)
clear_btn.place(x=50, y=200)

clear_all_btn = Button(root, text="Clear All Items", width=20, font=("lucida 15"), command=clrall)
clear_all_btn.place(x=50, y=250)

save_btn = Button(root, text="Save", width=20, font=("lucida 15"), command=save)
save_btn.place(x=50, y=300)





root.mainloop()
