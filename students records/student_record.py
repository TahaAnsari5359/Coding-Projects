from tkinter import *
from tkcalendar import Calendar
from datetime import datetime
from tkinter import filedialog
import tkinter.messagebox as tmsg




root = Tk()
root.config(bg="black")

def pick():
    def get_date():
        selected = cal.get_date()
        formatted = datetime.strptime(selected, "%m/%d/%y").strftime("%d-%m-%Y")
        date_of_birth_var.set(formatted)
        top.destroy()

    top = Toplevel(root)
    top.grab_set()
    top.title("Choose Date of Birth")

    cal = Calendar(top, selectmode='day')
    cal.pack(pady=10)

    Button(top, text="Select", command=get_date).pack(pady=5)


def save():
    try:
        if not stud_fir_var.get().strip() or not father_var.get().strip() or not mobile_num_var.get().strip():
            tmsg.showerror("Input Error", "Please fill all required fields before saving.")
            return
        file = filedialog.asksaveasfilename(
            title="Save As",
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")]
        )
        
        if file:
            
            with open(file, "a") as f:
                today = datetime.now().strftime("%d-%m-%Y")

                f.write(f"----- STUDENT RECORD -----\nSaved On: {today}\n")

                f.write(f"Name: {stud_fir_var.get()} {father_var.get()} {stud_mid_var.get()}\n")
                f.write(f"Date of Birth: {date_of_birth_var.get()}\n")
                f.write(f"Mobile: {mobile_code_var.get()} {mobile_num_var.get()}\n")
                f.write(f"Email: {email_id_var.get()}\n")
                f.write(f"Gender: {gender_var.get()}\n")
                f.write(f"Course: {course_var.get()}\n")
                f.write(f"Address: {address_ent.get('1.0', END).strip()}\n")
                f.write(f"City: {city_var.get()}\n")
                f.write("---------------------------\n\n")

            tmsg.showinfo("Success", "Record saved successfully!")

    except Exception as e:
        tmsg.showerror("ERROR FOUND", f"Something went wrong:\n{e}")
    root.destroy()

def reset():
    stud_fir_var.set("")
    stud_mid_var.set("")
    father_var.set("")
    date_of_birth_var.set("")
    mobile_code_var.set("+91")
    mobile_num_var.set("")
    email_id_var.set("")
    gender_var.set(None)
    course_var.set("Select Course")
    address_ent.delete(1.0,END)
    city_var.set("")





root.geometry("950x650")
student_reg_lab = Label(root,bg="black",fg="white", text="STUDENT REGISTRATION FORM",font=("lucida 20 bold underline"))
student_reg_lab.pack(pady=20)

stud_name_lab = Label(root, bg="black",fg="white",text="Student Name: ",font=("lucida 15 bold"))
stud_name_lab.place(x=50,y=100)

stud_fir_var = StringVar()
stud_fir_ent = Entry(root,textvariable=stud_fir_var, font=("lucida 15 bold"))
stud_fir_ent.place(x=200,y=100)

stud_mid_var = StringVar()
stud_mid_ent = Entry(root,textvariable=stud_mid_var,font=("lucida 15 bold"))
stud_mid_ent.place(x=450,y=100)


father_name_lab = Label(root, bg="black",fg="white", text="Father Name: ",font=("lucida 15 bold"))
father_name_lab.place(x=50,y=150)

father_var = StringVar()
father_ent = Entry(root,textvariable=father_var, font=("lucida 15 bold"))
father_ent.place(x=200,y=150)

date_of_birth_lab = Label(root, bg="black",fg="white", text="Date of birth: ",font=("lucida 15 bold"))
date_of_birth_lab.place(x=50,y=200)


date_of_birth_var = StringVar()
date_of_birth_ent = Entry(root,textvariable=date_of_birth_var,font=("lucida 15 bold"))
date_of_birth_ent.place(x=200,y=200)



pick_btn = Button(root,text="Pick date",font=("lucida 10 bold"),command=pick)
pick_btn.place(x=500,y=200)

mobile_code_var = StringVar()
mobile_code_var.set("+91")
mobile_code_ent = Entry(root, width=3, textvariable=mobile_code_var,font=("lucida 15 bold"))
mobile_code_ent.place(x=200,y=250)

mobile_num_var = StringVar()
mobile_num_ent = Entry(root, textvariable=mobile_num_var,font=("lucida 15 bold"))
mobile_num_ent.place(x=250,y=250)


mobile_lab = Label(root, bg="black",fg="white", text="Mobile No: ", font=("lucida 15 bold"))
mobile_lab.place(x=50,y=250)


email_id_lab = Label(root, bg="black",fg="white", text="Email Id: ", font=("lucida 15 bold"))
email_id_lab.place(x=500,y=250)

email_id_var = StringVar()
email_id_ent = Entry(root,width=30, textvariable=email_id_var,font=("lucida 15 bold"))
email_id_ent.place(x=600,y=250)


email_id_lab = Label(root, bg="black",fg="white",text="Email Id: ", font=("lucida 15 bold"))
gender_lab = Label(root, bg="black",fg="white", text="Gender: ", font=("lucida 15 bold"))
gender_lab.place(x=50,y=300)

gender_var = StringVar()
gender_var.set(None)

email_id_lab = Label(root,  bg="black",fg="white",text="Email Id: ", font=("lucida 15 bold"))
gender_male = Radiobutton(root,  text="male", variable=gender_var, value="male",font=("lucida 15 bold"))
gender_male.place(x=300,y=300)


email_id_lab = Label(root, bg="black",fg="white",text="Email Id: ", font=("lucida 15 bold"))
gender_female = Radiobutton(root,  text="female", variable=gender_var, value="female",font=("lucida 15 bold"))
gender_female.place(x=200,y=300)


email_id_lab = Label(root, bg="black",fg="white",text="Email Id: ", font=("lucida 15 bold"))
gender_other = Radiobutton(root,  text="Others", variable=gender_var, value="Others",font=("lucida 15 bold"))
gender_other.place(x=400,y=300)


email_id_lab = Label(root, bg="black",fg="white",text="Email Id: ", font=("lucida 15 bold"))
course_lab = Label(root, bg="black",fg="white", text="Course: ", font=("lucida 15 bold"))
course_lab.place(x=50,y=350)


course_var = StringVar()
course_var.set("Select Course")
course_option = ["B.Tech", "B.Sc", "B.Com", "B.A", "M.Tech", "M.Sc", "M.Com"]
option_menu = OptionMenu(root,  course_var,*course_option, )
option_menu.place(x=200,y=350)

address_lab = Label(root, bg="black",fg="white", text="Address: ", font=("lucida 15 bold"))
address_lab.place(x=50,y=400)


address_ent = Text(root,width=40,wrap="word",height=3,font=("lucida 15 bold"))
address_ent.place(x=200,y=400)


city_lab = Label(root, bg="black",fg="white", text="City: ",font=("lucida 15 bold"))
city_lab.place(x=700,y=400)


city_var = StringVar()
city_ent = Entry(root,textvariable=city_var, width=13,font=("lucida 15 bold"))
city_ent.place(x=770,y=400)

reset_btn = Button(root,text="RESET",font=("lucida 15 bold"),command=reset)
reset_btn.pack(fill=X,pady=10,padx=10,side=BOTTOM)

save_btn = Button(root,text="SAVE",font=("lucida 15 bold"),command=save)
save_btn.pack(fill=X,pady=10,padx=10,side=BOTTOM)


root.mainloop()
