# BUILDING A COUSTMER REVIEW FLOATING WINDOW
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("FeedbackCenter")
window.minsize(height=800,width=1200)

label_1= ttk.Label(
    padding = 12,text = "We'd love to hear your feedback! Please take a moment to share your experience with us.")
label_1.pack()
label_1.config(font = ('Times New Roman',22,'bold'))

label_2= ttk.Label(
    padding = 12,text = "Please rate our service out of 5 stars ⭐")
label_2.pack(side = "top")
label_2.config(font = ('Times New Roman',22,'underline'))

# 5 Star rating:

radio_value = tk.StringVar()

def get_radio_value01():
    check_option_task01()
    label["text"] = f"1 ⭐ — Very Poor: My experience was very disappointing."
def get_radio_value02():
    check_option_task01()
    label["text"] = f"2 ⭐ — Poor: My experience did not meet expectations."
def get_radio_value03():
    check_option_task01()
    label["text"] = f"3 ⭐ — Average: My experience was satisfactory."
def get_radio_value04():
    check_option_task01()
    label["text"] = f"4 ⭐ — Good: My experience was very good."
def get_radio_value05():
    check_option_task01()
    label["text"] = f"5 ⭐ — Excellent: My experience exceeded my expectations."


button_1 = ttk.Radiobutton(text="⭐                       ", variable=radio_value, value= "1" , command=get_radio_value01)
button_2 = ttk.Radiobutton(text="⭐⭐                 ", variable=radio_value, value="2", command=get_radio_value02)
button_3 = ttk.Radiobutton(text="⭐⭐⭐           ", variable=radio_value, value="3", command=get_radio_value03)
button_4 = ttk.Radiobutton(text="⭐⭐⭐⭐      ", variable=radio_value, value="4", command=get_radio_value04)
button_5 = ttk.Radiobutton(text="⭐⭐⭐⭐⭐", variable=radio_value, value="5", command=get_radio_value05)


button_1.pack(side = "top")
button_2.pack(side = "top")
button_3.pack(side = "top")
button_4.pack(side = "top")
button_5.pack(side = "top")

label = ttk.Label(text = radio_value.get())
label.pack()
label.config(font = ('Times New Roman',15,'bold'))

# Comment Button : ----

text = tk.Text(height = 10,width = 100,bg="gray")
text.pack(side = "top",expand = False,pady = 40)
text.insert("1.0","Write your review here...\n")
text.focus()

# Name Email ---------
label_unknown = ttk.Label(padding = 15 ,text = "Name and Email are optional — you can skip either or both.")
label_unknown.config(font = ('Times New Roman',10,'italic'))
label_unknown.pack()

user_input_name = tk.Entry(width = 30,bg="gray")
user_input_name.insert(0,"Name:  ")
user_input_name.pack()

user_input_email = tk.Entry(width = 50,bg="gray")
user_input_email.insert(0,"Email:  ")
user_input_email.pack(pady = 20)


sep = ttk.Separator(orient = "horizontal")
sep.pack(fill = 'x')

# button disable & enable:------

def check_option_task01():
    if bool(radio_value.get()) != False and check_option_01.get() + check_option_02.get() == 2:
        enable_button_fun()
    else:
        disabled_button_fun()


def enable_button_fun():
    quit_button["state"]  = "normal"
def disabled_button_fun():
    quit_button["state"]  = "disabled"

#terms & condition------ 
check_option_01 = tk.IntVar()

check_button_01 = ttk.Checkbutton( 
    text = "1. I agree to the Terms & Conditions and consent to the use of my feedback for service improvement."  , 
    variable = check_option_01,
     command =check_option_task01 )
check_button_01.pack(pady = 20)

check_option_02 = tk.IntVar()
check_button_02 = ttk.Checkbutton(
     text = "2. I confirm that my feedback is honest and based on my personal experience." ,
      variable = check_option_02, 
      command =check_option_task01 )
check_button_02.pack()


#sumbit & quit

# Sumbit :-----
def get_all_data():
    print((user_input_name.get()).title())
    print((user_input_email.get()).lower())
    print(f"Coustmer Review: {label["text"]}")
    text_data = text.get("1.0","end")
    print(text_data.strip())
    window.destroy()

quit_button = ttk.Button(text = "\n\tSumbit & Quit\t    \n", command = get_all_data)
quit_button.pack(pady = 20,side = "right",expand = True)
quit_button["state"]  = "disabled"

# quit
def not_now():
    window.destroy()

not_now_button = ttk.Button(text = "\nNot Now\n", command = not_now)
not_now_button.pack(pady = 20,side = "left",expand = True)

window.mainloop() 