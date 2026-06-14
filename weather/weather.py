from tkinter import *
import tkinter.messagebox as tmsg
import requests
root = Tk()
root.geometry("400x500")

root.config(bg="#3EAACF")
root.title("Weather App")
root.resizable(False,False)

main_lab = Label(root,fg="white",bg="#2C5B69",text="WEATHER",font=("lucida 15 bold"))
main_lab.pack(fill=X)






apikeys = "4298c031d651c9a2a3edaffe112ac322"

def fetch(event=None):
        try:
        
            
            
                cities = e1_var.get()
                url = f"https://api.openweathermap.org/data/2.5/weather?q={cities}&appid={apikeys}&units=metric"
                data = requests.get(url).json()

                temp = data['main']['temp']
                temp_lab.config(text=f"Temperature: {temp}°C",font=("lucida 14 bold underline italic"))
                humidity = data['main']['humidity']
                humi_lab.config(text=f"Humidity: {humidity}%",font=("lucida 14 bold underline italic"))
                description = data['weather'][0]['description']
                des_lab.config(text=f"Description: {description}",font=("lucida 14 bold underline italic"))
                wind = data['wind']['speed']
                wind_lab.config(text=f"Wind: {wind} m/s",font=("lucida 14 bold underline italic"))
                e1_var.set("")

        except:    
                tmsg.showerror("error","please input a valid city Name")
                e1_var.set("")
                return
        


city_lab = Label(root,bg="#3EAACF",text="Enter City Name and Country Code: ",font=("lucida 13 bold"))
city_lab.place(x=50,y=50)
e1_var = StringVar()
e1_ent = Entry(root,relief=SUNKEN,bd=3,textvariable=e1_var,font=("lucida 15 bold"),justify=CENTER)
e1_ent.place(x=50,y=100)

temp_lab = Label(root,bg="#3EAACF",text="Temperature: ",font=("lucida 14 bold"))
temp_lab.place(x=30,y=150)

humi_lab = Label(root,bg="#3EAACF",text="Humidity: ",font=("lucida 14 bold"))
humi_lab.place(x=30,y=200)


des_lab = Label(root,bg="#3EAACF",text="Description: ",font=("lucida 14 bold"))
des_lab.place(x=30,y=250)

wind_lab = Label(root,bg="#3EAACF",text="Wind: ",font=("lucida 14 bold"))
wind_lab.place(x=30,y=300)




featch = Button(root,relief=GROOVE,bd=5,text="FETCH WEATHER",font=("lucida 10 bold"),command=fetch)
featch.pack(side=BOTTOM,fill=X,padx=30,pady=30)
root.bind('<Return>',fetch)






root.mainloop()
