from tkinter import*
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title("Basictext3.0")
root.geometry("1200x660")


# creating main frame
my_frame = Frame(root).pack(pady=5)

# create main text box
my_text = Text(my_frame, width=97, height=25, font=("Arial", 16), selectbackground="Lightgrey", selectforeground="Black", undo=True)
my_text.pack()

#new file def
def new_file():
    my_text.delete("1.0", END)
    root.title("New file - Basictext3.0")

#open file def
def open_file():
    my_text.delete("1.0", END)
    text_file = filedialog.askopenfilename(title="Open file", filetypes=(("Text Files", "*txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()
    root.title("File is open - Basictext3.0")

def save_as_file():
    text_file = filedialog.askopenfilename(filetypes=(("Text Files", "*txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    text_file = open(text_file, 'w')
    text_file.write(my_text.get(1.0, END))
def minityper():
    my_text.delete("1.0", END)
    root.title("Basictext3.0")

def clear():
    my_text.delete(1.0, END)

def bold_it():
    bold_font = font.Font(my_text, my_text.cget("font"))
    bold_font.configure(weight="bold")
    my_text.tag_configure("bold", font=bold_font)
    current_tags = my_text.tag_names("sel.first")
    if "bold" in current_tags:
        my_text.tag_remove("bold", "sel.first", "sel.last")
    else:
        my_text.tag_add('bold', "sel.first", "sel.last")

def italics_it():
    italics_font = font.Font(my_text, my_text.cget("font"))
    italics_font.configure(slant="italic")
    my_text.tag_configure("italic", font=italics_font)
    current_tags = my_text.tag_names("sel.first")
    if "Italic" in current_tags:
        my_text.tag_remove("italic", "sel.first", "sel.last")
    else:
        my_text.tag_add('italic', "sel.first", "sel.last")

#Menubars
my_menu = Menu(root)
root.config(menu=my_menu)
    
#filemenu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)
file_menu.add_command(label="Minityper", command=minityper)

#textmenu
text_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Text", menu=text_menu)
text_menu.add_command(label="Clear all", command=clear)
text_menu.add_command(label="Bold", command=bold_it)
text_menu.add_command(label="Italics", command=italics_it)

button_frame = Frame(root)
button_frame = Frame(root)
button_frame.pack(pady=7, fill=X)

clear_button = Button(button_frame, text="Clear all", command=clear)
clear_button.grid(row=0, column=2, padx=10)

open_button = Button (button_frame, text="Open file", command=open_file)
open_button.grid(row=0, column=0, padx=10, pady=5)

saveas_button = Button (button_frame, text="Save as", command=save_as_file)
saveas_button.grid(row=0, column=1, padx=10, pady=5)

bold_button = Button (button_frame, text="Bold", command=bold_it)
bold_button.grid(row=0, column=3, padx=10)

italics_button = Button (button_frame, text="Italics", command=italics_it)
italics_button.grid(row=0, column=4, padx=10)

undo_button = Button (button_frame, text="Undo",command= my_text.edit_undo)
undo_button.grid(row=0, column=5, padx=10)

redo_button = Button (button_frame, text="Redo", command=my_text.edit_redo)
redo_button.grid(row=0, column=6 ,padx=10)

root.mainloop()
#?ijp "Fart"