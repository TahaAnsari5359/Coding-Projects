from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("315x360")
root.config(bg="RED")
root.title("TIC TAC TOE")
root.resizable(False,False)
player = "X"

player_X_var = StringVar()
player_x_ent = Entry(root,width=20,textvariable=player_X_var)
player_x_ent.place(x=100,y=300)
x_lab = Label(root,bg="red",fg="white",text='player X : ',font=("lucida 10 bold"))
x_lab.place(x=20,y=300)


player_0_var = StringVar()
player_0_ent = Entry(root,width=20,textvariable=player_0_var)
player_0_ent.place(x=100,y=330)
zero_lab = Label(root,bg="red",fg="white",text='player 0 : ',font=("lucida 10 bold"))
zero_lab.place(x=20,y=330)

x_0_lab = Label(root,bg="red",fg="white",text="X and O GAME \n Click Start",font=("algerian 25 bold underline"))
x_0_lab.pack(pady=20)





def strt():
    player_X = player_X_var.get().strip()
    player_0 = player_0_var.get().strip()

    if player_X == "" or player_0 == "":
        tmsg.showwarning("Missing Name", "Please enter both player names!")
        return
    x_0_lab.config(text="",bg="red")
    def tap1():
        global player
        if b1["text"] == "":
            b1.config(text=player,)
            player = "O" if player == "X" else "X"
            check_winner()

    def tap2():
        global player
        if b2["text"] == "":
            b2.config(text=player, )
            player = "O" if player == "X" else "X"
            check_winner()

    def tap3():
        global player
        if b3["text"] == "":
            b3.config(text=player,)
            player = "O" if player == "X" else "X"
            check_winner()

    def tap4():
        global player
        if b4["text"] == "":
            b4.config(text=player,)
            player = "O" if player == "X" else "X"
            check_winner()

    def tap5():
        global player
        if b5["text"] == "":
            b5.config(text=player, )
            player = "O" if player == "X" else "X"
            check_winner()

    def tap6():
        global player
        if b6["text"] == "":
            b6.config(text=player,)
            player = "O" if player == "X" else "X"
            check_winner()

    def tap7():
        global player
        if b7["text"] == "":
            b7.config(text=player, )
            player = "O" if player == "X" else "X"
            check_winner()

    def tap8():
        global player
        if b8["text"] == "":
            b8.config(text=player,)
            player = "O" if player == "X" else "X"
            check_winner()

    def tap9():
        global player
        if b9["text"] == "":
            b9.config(text=player, )
            player = "O" if player == "X" else "X"
            check_winner()

    def reset():
        asking = tmsg.askyesno("Question","Thanks For Playing. Do You Want To play Again?")
        if asking:
            b1.config(text="",)
            b2.config(text="",)
            b3.config(text="", )
            b4.config(text="", )
            b5.config(text="", )
            b6.config(text="",)
            b7.config(text="",)
            b8.config(text="",)
            b9.config(text="",)
        else:
            root.destroy()

    def check_winner():

        if b1.cget("text") == b2.cget("text") == b3.cget("text") != "":
            winner = b1.cget("text")
            player_0 = player_0_var.get()
            player_X = player_X_var.get()
            if winner == "X":
                tmsg.showinfo("Winner", f"Player {player_X} wins!")
            else:
                tmsg.showinfo("Winner", f"Player {player_0} wins!")


            reset()

            

        elif b4.cget("text") == b5.cget("text") == b6.cget("text") != "":
            winner = b4.cget("text")
            
            player_0 = player_0_var.get()
            player_X = player_X_var.get()
            if winner == "X":
                tmsg.showinfo("Winner", f"Player {player_X} wins!")
            else:
                tmsg.showinfo("Winner", f"Player {player_0} wins!")
            reset()

        elif b7.cget("text") == b8.cget("text") == b9.cget("text") != "":
            winner = b7.cget("text")
            
            player_0 = player_0_var.get()
            player_X = player_X_var.get()
            if winner == "X":
                tmsg.showinfo("Winner", f"Player {player_X} wins!")
            else:
                tmsg.showinfo("Winner", f"Player {player_0} wins!")
            reset()

        # FOR DIAGNOLS CONDITION
        elif b1.cget("text") == b5.cget("text") == b9.cget("text") != "":
            winner = b1.cget("text")
            
            player_0 = player_0_var.get()
            player_X = player_X_var.get()
            if winner == "X":
                tmsg.showinfo("Winner", f"Player {player_X} wins!")
            else:
                tmsg.showinfo("Winner", f"Player {player_0} wins!")
            reset()


        elif b3.cget("text") == b5.cget("text") == b7.cget("text") != "":
            winner = b3.cget("text")
            
            player_0 = player_0_var.get()
            player_X = player_X_var.get()
            if winner == "X":
                tmsg.showinfo("Winner", f"Player {player_X} wins!")
            else:
                tmsg.showinfo("Winner", f"Player {player_0} wins!")
            reset()
            
        elif b1.cget("text") == b4.cget("text") == b7.cget("text") != "":
            winner = b1.cget("text")
            
            player_0 = player_0_var.get()
            player_X = player_X_var.get()
            if winner == "X":
                tmsg.showinfo("Winner", f"Player {player_X} wins!")
            else:
                tmsg.showinfo("Winner", f"Player {player_0} wins!")
            reset()
        
        elif b2.cget("text") == b5.cget("text") == b8.cget("text") != "":
            winner = b2.cget("text")
            
            player_0 = player_0_var.get()
            player_X = player_X_var.get()
            if winner == "X":
                tmsg.showinfo("Winner", f"Player {player_X} wins!")
            else:
                tmsg.showinfo("Winner", f"Player {player_0} wins!")
            reset()

        elif b3.cget("text") == b6.cget("text") == b9.cget("text") !="":
            winner = b3.cget("text")
            
            player_0 = player_0_var.get()
            player_X = player_X_var.get()
            if winner == "X":
                tmsg.showinfo("Winner", f"Player {player_X} wins!")
            else:
                tmsg.showinfo("Winner", f"Player {player_0} wins!")
            reset()

        elif all(b.cget("text") != "" 
                for b in [b1, b2, b3, b4, b5, b6, b7, b8, b9]):
            tmsg.showinfo("Draw", "Match Draw! No One Wins")
            
            reset()
        
    

    b1 = Button(root,width=5,height=2,font=("lucida 15 bold"),command=tap1)
    b1.place(x=20,y=20)

    b2 = Button(root,width=5,height=2,font=("lucida 15 bold"),command=tap2)
    b2.place(x=120,y=20)

    b3 = Button(root,width=5,height=2,font=("lucida 15 bold"),command=tap3)
    b3.place(x=220,y=20)

    b4 = Button(root,width=5,height=2,font=("lucida 15 bold"),command=tap4)
    b4.place(x=20,y=120)

    b5 = Button(root,width=5,height=2,font=("lucida 15 bold"),command=tap5)
    b5.place(x=120,y=120)

    b6 = Button(root,width=5,height=2,font=("lucida 15 bold"),command=tap6)
    b6.place(x=220,y=120)

    b7 = Button(root,width=5,height=2,font=("lucida 15 bold"),command=tap7)
    b7.place(x=20,y=220)

    b8 = Button(root,width=5,height=2,font=("lucida 15 bold"),command=tap8)
    b8.place(x=120,y=220)


    b9 = Button(root,width=5,height=2,font=("lucida 15 bold"),command=tap9)
    b9.place(x=220,y=220)


menu_bar = Menu(root)
def infoo():
        tmsg.showinfo("About","Made By Taha")

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="ABOUT",command=infoo)
menu_bar.add_cascade(label="INFO", menu=file_menu,)
root.config(menu=menu_bar)

strt_btn = Button(root,text="Start",font=("lucida 15 bold"),command=strt)
strt_btn.place(x=240,y=300)



root.mainloop()
