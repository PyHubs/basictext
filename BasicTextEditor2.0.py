from tkinter import*
from tkinter import filedialog
from tkinter import font

root=Tk()
root.title("Basictext2.0")
root.geometry("1199x650")

# creating main frame
my_frame = Frame(root).pack(pady=5)

# create main text box
my_text = Text(my_frame, width=97, height=25, font=("Arial", 16), selectbackground="Lightgrey", selectforeground="Black", undo=True)
my_text.pack()

#new file def
def new_file():
    my_text.delete("1.0", END)
    root.title("New file - Basictext2.0")
    status_bar.config(text="New file")

#open file def
def open_file():
    my_text.delete("1.0", END)
    text_file = filedialog.askopenfilename(title="Open file", filetypes=(("Text Files", "*txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()

def save_as_file():
    text_file = filedialog.asksaveasfilename(filetypes=(("Text Files", "*txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
#Menubars
my_menu = Menu(root)
root.config(menu=my_menu)
    
#filemenu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save")
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

#editmenu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

#status bar
status_bar = Label(root, text="File in edit ", anchor=E).pack(fill=X, side=BOTTOM, ipady=5)

root.mainloop()
