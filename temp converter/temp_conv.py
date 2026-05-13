from tkinter import *
root = Tk()
root.geometry("700x500")
root.title("Temperature Converter")
root.config(bg="Yellow",)


def calc():
    ctof = int(temp_var.get())
    formula_ctof = (ctof * 9/5) + 32
    formula_ftoc = (ctof - 32) * 5/9
    formula_ctok = (ctof + 273.15)
    formula_ktoc = (ctof - 273.15)
    formula_ftok = (ctof - 32) * 5/9 + 273.15
    formula_ktof = (ctof - 273.15) * 9/5 +32



    ctof_ans.config(text=f"{formula_ctof:.2f}°F")

    Ftoc_ans.config(text=f"{formula_ftoc:.2f}°C")

    ctok_ans.config(text=f"{formula_ctok:.2f}°K")

    ktoc_ans.config(text=f"{formula_ktoc:.2f}°C")

    ftok_ans.config(text=f"{formula_ftok:.2f}°K")

    ktof_ans.config(text=f"{formula_ktof:.2f}°F")

    temp_var.set("")


def reset():
    ctof_ans.config(text="")

    Ftoc_ans.config(text="")

    ctok_ans.config(text="")

    ktoc_ans.config(text="")

    ftok_ans.config(text="")

    ktof_ans.config(text="")






temp_var = StringVar()
temp_ent = Entry(root, textvariable= temp_var, font=("lucida 25 bold"))
temp_ent.place(x=50,y=25)

ctof = Label(root, bg="Yellow", text="Celcius To Fahrenheit : ", font=("lucida 15 bold"))
ctof.place(x=50,y=100)

ctof_ans = Label(root, bg="yellow", font=("lucida 15 bold")) 
ctof_ans.place(x=300,y=100)

Ftoc = Label(root, bg="Yellow", text="Fahrenheit To Celcius : ", font=("lucida 15 bold"))
Ftoc.place(x=50,y=160)

Ftoc_ans = Label(root, bg="yellow", font=("lucida 15 bold")) 
Ftoc_ans.place(x=300,y=160)

ctok = Label(root, bg="Yellow", text="Celcius To kelvin : ", font=("lucida 15 bold"))
ctok.place(x=50,y=220)

ctok_ans = Label(root, bg="yellow", font=("lucida 15 bold")) 
ctok_ans.place(x=300,y=220)

ktoc = Label(root, bg="Yellow", text="kelvin To Celcius : ", font=("lucida 15 bold"))
ktoc.place(x=50,y=280)

ktoc_ans = Label(root, bg="yellow", font=("lucida 15 bold")) 
ktoc_ans.place(x=300,y=280)


ftok = Label(root, bg="Yellow", text="Fahrenheit To Kelvin : ", font=("lucida 15 bold"))
ftok.place(x=50,y=340)

ftok_ans = Label(root, bg="yellow", font=("lucida 15 bold")) 
ftok_ans.place(x=300,y=340)

ktof = Label(root, bg="Yellow", text=" Kelvin To Fahrenheit : ", font=("lucida 15 bold"))
ktof.place(x=50,y=400)

ktof_ans = Label(root, bg="yellow", font=("lucida 15 bold")) 
ktof_ans.place(x=300,y=400)










calculate_btn = Button(root,text="Calculate", font=("lucida 15 bold"), command=calc)
calculate_btn.place(x=570,y=25)


Reset_btn = Button(root,text="Reset", width=8, font=("lucida 15 bold"), command=reset)
Reset_btn.place(x=570,y=75)

root.mainloop()
