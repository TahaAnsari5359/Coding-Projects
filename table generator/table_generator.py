from tkinter import *
import tkinter.messagebox as tmsg
import random
root = Tk()
root.geometry("200x400")
root.config(bg="black")
root.title("Table Generator")
root.resizable(False,False)


def genn(Event=None):
    random_colors = "#098A65","#8A092E","#8A6509","#092E8A","#190629","#062908","#B415E0","#270800","#1F2700","#080027"
    colrs = random.choice(random_colors)
    list_box.delete(0,END)
    
    try:
        list_box.pack(side=BOTTOM)
        n = int(e1_var.get())
        for i in range(1,11):
            table = text=f"{n} X {i} = {n*i}"
            table_lab.config(text=f"Table Of: {n}",bg="white",fg="black")
            list_box.config(bg=colrs,fg="white")
            list_box.insert(END,table)
            e1_var.set("")
    except:
        tmsg.showwarning("error","Input a valid number")
        e1_var.set("")
        return
        




e1_var = StringVar()
e1_ent = Entry(root,textvariable=e1_var,justify=CENTER,font=("lucida 15 bold"),width=5)
e1_ent.pack(pady=20)


table_lab = Label(root,bg="black",font=("lucida 13 bold"))
table_lab.pack(fill=X)


gen = Button(root,text="GENERATE",bg="#6F354B",fg="white",font=('lucida 13 bold'),command=genn)
gen.pack(side=BOTTOM,pady=20,fill=X,padx=20)
root.bind('<Return>',genn)





list_box = Listbox(root,justify=CENTER,height=10,width=15,relief=GROOVE,bd=4,font=('lucida 13 bold'))


root.mainloop()
