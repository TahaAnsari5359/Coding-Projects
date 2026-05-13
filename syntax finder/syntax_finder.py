import customtkinter as ctk
import tkinter as tk
import tkinter.messagebox as tmsg



ctk.set_appearance_mode("System")          
ctk.set_default_color_theme("blue")     

root = ctk.CTk()
root.configure(fg_color="#098095")
root.geometry("400x500")
root.title("Coding Lang Syntax Finder")

main_lab = ctk.CTkLabel(root, fg_color="black",text_color="white", text="Code Syntax Pro", font=("Lucida", 18, "bold"))
main_lab.pack(pady=10,fill="x")


def codes():
    
    data = opts_var.get()
    cods = {
        "Python": 'print("Hello, World!")',
        "C": '#include <stdio.h>\n\nint main() {\n    printf("Hello, World!\\n");\n    return 0;\n}',
        "C++": '#include <iostream>\nusing namespace std;\n\nint main() {\n    cout << "Hello, World!" << endl;\n    return 0;\n}',
        "Java": 'public class HelloWorld {\n    public static void main(String[] args) {\n        System.out.println("Hello, World!");\n    }\n}',
        "HTML": '<!DOCTYPE html>\n<html>\n<head>\n    <title>Hello World</title>\n</head>\n<body>\n    Hello, World!\n</body>\n</html>',
        "PHP": '<?php\necho "Hello, World!";\n?>',
        "C#": 'using System;\nclass Program {\n    static void Main() {\n        Console.WriteLine("Hello, World!");\n    }\n}',
        "SQL": """CREATE DATABASE MyDatabase;
        USE MyDatabase;
        CREATE TABLE Users (id INT PRIMARY KEY, name VARCHAR(50), age INT);
        INSERT INTO Users (id, name, age) VALUES (1, 'Alice', 25);
        SELECT * FROM Users;"""
        }
   
    if data not in cods:
        tmsg.showwarning("error","Select a valid programming language")
        return
    else:
        gets = (cods[data])
        text_area.delete(1.0,"end")
        text_area.insert(1.0,gets)
    
        
    


def copy():
    gets = text_area.get(1.0,"end")
    root.clipboard_clear()
    root.clipboard_append(gets)
    tmsg.showinfo("copied","copied to clipboard")



   





select_lang = ctk.CTkLabel(root,text_color="black", text="Select Programming Language", font=("Lucida", 15, "bold"))
select_lang.pack(pady=5, fill="x")


values = ["Python", "C", "C++", "C#", "Java", "HTML", "SQL", "PHP"]

opts_var = ctk.StringVar(value="PROGRAMMING LANGUAGES")

option_menu = ctk.CTkOptionMenu(root,fg_color="#CF073C", variable=opts_var, values=values)
option_menu.pack(pady=20)


text_area = tk.Text(root,wrap="word",height=15,width=35,font=('lucida 10 bold'))
text_area.pack(pady=20)





btn_f = ctk.CTkFrame(root,fg_color="#098095")
btn_f.pack(side="bottom")
code_btn = ctk.CTkButton(btn_f,fg_color="#00C117",text_color="black", hover_color="red",corner_radius=15, width=150, text="CODE", font=("Lucida", 16, "bold"),command=codes)
code_btn.pack(side="left", pady=20,padx=10)

copy_btn = ctk.CTkButton(btn_f,fg_color="#00C117",text_color="black", hover_color="red",corner_radius=15, width=150, text="COPY", font=("Lucida", 16, "bold"),command=copy)
copy_btn.pack(side="right", pady=20,padx=10)


root.mainloop()

