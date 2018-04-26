from tkinter import *

window=Tk()

def km_to_miles():
    print(e1_value.get())
    miles=float(e1_value.get())*1.6
    t1.insert(END,miles)

def converter():
    g=float(e1_value.get())*1000
    gram.insert(END,g)
    lb=float(e1_value.get())*2.20462
    pounds.insert(END,lb)
    oz=float(e1_value.get())*35.274
    ounces.insert(END,oz)

kg=Label(text="                 kg                ",)
kg.grid(row=0,column=0)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

b1=Button(window,text="Convert",command=converter)
b1.grid(row=0,column=2)

gram=Text(window,height=1,width=20)
gram.grid(row=1,column=0)

pounds=Text(window,height=1,width=20)
pounds.grid(row=1,column=1)

ounces=Text(window,height=1,width=20)
ounces.grid(row=1,column=2)

window.mainloop()
