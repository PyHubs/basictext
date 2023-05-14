from tkinter import*
from tkinter import filedialog

root=Tk()
root.title("BasicTextEditor 1.0")
root.geometry("600x450")

my_text = Text(root, width=50, height=15, font=("Arial", 16))
my_text.pack(pady=20)

#clear function time!
def clear():
    my_text.delete(1.0, END)

def open_text():
    text_file = filedialog.askopenfilename()
    text_file = open(text_file)
    stuff = text_file.read()
    
    my_text.insert(END, stuff)
    text_file.close()

def save_text():
    text_file = filedialog.askopenfilename()
    text_file = open(text_file, 'w')
    text_file.write(my_text.get(1.0, END))

button_frame = Frame(root)
button_frame = Frame(root)
button_frame.pack()

clear_button = Button(button_frame, text="Clear all", command=clear)
clear_button.grid(row=0, column=0)

root.configure(background="Grey")
button_frame.configure(background="lightgrey")

open_button = Button (button_frame, text="Open txt file", command=open_text)
open_button.grid(row=0, column=1)

save_button = Button(button_frame, text="Save txt file", command=save_text)
save_button.grid(row=0, column=2)

root.mainloop()