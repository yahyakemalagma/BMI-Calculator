import tkinter

# window

my_window = tkinter.Tk()
my_window.title("BMI Calculator")
my_window.minsize(width=150,height=150)


def clicked_button():
    user_input=int(my_entry.get())
    user_input2=int(my_entry2.get())
    abc2= user_input*100*100
    abc3=user_input2*user_input2
    bsi=abc2/abc3
    if bsi >=40.0:
        print("Obese")
        my_label3.config(text="Obese")
    elif bsi >= 25.0:
        print("Overweight")
        my_label3.config(text="Overweight")
    elif bsi >=18.5:
        print("Normal")
        my_label3.config(text="Normal")
    else:
        print("Underweight")
        my_label3.config(text="Underweight")



#label
my_label= tkinter.Label(text="Enter Your Weight (kg)",font=("Arial",10,"normal"))
my_label.pack()

#entry

my_entry= tkinter.Entry()
my_entry.pack()

#label2
my_label2= tkinter.Label(text="Enter Your Height (cm)",font=("Arial",10,"normal"))
my_label2.pack()

#entry2

my_entry2= tkinter.Entry()
my_entry2.pack()

#button

my_button= tkinter.Button(text="Calculate",command=clicked_button)
my_button.pack()

#label sonuç
my_label3=tkinter.Label(text="",font=("Arial",10,"normal"))
my_label3.pack()





my_window.mainloop()
