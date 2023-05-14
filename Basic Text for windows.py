#basic text for windows allows users to wrire HTML, PYTHON and TEXT files easily!! please use this app!!!
#edited text with basic text for windows - HEHE

from tkinter import*
from tkinter import messagebox
from tkinter import filedialog
from tkinter import font
#import python

#configure root
root = Tk()
root.title("Basic Text For Windows")
root.geometry("1200x660")

#open a file
def open_file():
    my_text.delete("1.0", END)
    text_file = filedialog.askopenfilename(title="Open file", filetypes=(("Text Files", "*txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()
    root.title("File is open - Basic Text For Windows")

    status.pack_forget()
    global openfilestatus
    openfilestatus = Label(root, text="File is open      ")
    openfilestatus.pack(pady=3, side=RIGHT)


def save_as_file():
    text_file = filedialog.asksaveasfilename(filetypes=(("Text Files", "*txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    text_file = open(text_file, 'w')
    text_file.write(my_text.get(1.0, END))
    root.title("Basic Text For Windows")

    def destroy():
        openfilestatus.pack_forget()
        status.pack_forget()
        saveASfilestatus.pack_forget()
        status.pack(pady=3, side=RIGHT)

    openfilestatus.pack_forget()
    status.pack_forget()
    saveASfilestatus = Label(root, text="File has been saved      ")
    saveASfilestatus.pack(pady=3, side=RIGHT)
    saveASfilestatus.after(5000, destroy)

def clear():
    my_text.delete(1.0, END)

# toolbar for all the buttons
toolbar_frame = Frame(root)
toolbar_frame = Frame(root)
toolbar_frame.pack(pady=7, side=TOP)

#mew def
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

def help_abbout():
    messagebox.showinfo("Help","Basic text for windows is a free text editer for python that allows users to edit and read HTML, python and text files, the GUI of the application is made via tkinter on windows, The program is a part of the basic text fammily group that has many text editors, if you have a suggestion or experience a bug please email izooizkaan@gmail.com")

#Text box
my_text = Text(root, width=97, height=24, font=("Calbari", 16), selectbackground="Lightgrey", selectforeground="Black", undo=True)
my_text.pack(fill=X, expand=1)

#buttons
open_button = Button (toolbar_frame, text="Open file", command=open_file)
open_button.grid(row=0, column=0, padx=10, pady=5)

saveas_button = Button (toolbar_frame, text="Save file as", command=save_as_file)
saveas_button.grid(row=0, column=1, padx=10, pady=5)

save_button = Button (toolbar_frame, text="Save file as", command=save_as_file)

clear_button = Button(toolbar_frame, text="Clear all", command=clear)
clear_button.grid(row=0, column=2, padx=10)

undo_button = Button (toolbar_frame, text="Undo",command= my_text.edit_undo)
undo_button.grid(row=0, column=5, padx=10)

redo_button = Button (toolbar_frame, text="Redo", command=my_text.edit_redo)
redo_button.grid(row=0, column=6 ,padx=10)

bold_button = Button (toolbar_frame, text="Bold", command=bold_it)
bold_button.grid(row=0, column=3, padx=10)

italics_button = Button (toolbar_frame, text="Italics", command=italics_it)
italics_button.grid(row=0, column=4, padx=10)

help_button = Button (toolbar_frame, text="About", command=help_abbout)
help_button.grid(row=0, column=6 ,padx=10)

exit_button = Button (toolbar_frame, text="Exit program", command=root.destroy)
exit_button.grid(row=0, column=7 ,padx=10)

#Labels
global status
status = Label(root, text="Basic Text For Windows      ")
status.pack(pady=3, side=RIGHT)

print("hello and thanks for using our text editor, We hope you liked it Also make sure to check out til intepreter if you need help into wirte manuals! ")
#this is actually only 91 lines of code but with spaces it is bigger at 116 :) hahaha! only code viewes can see this or now unless someone told :D :HAHA, lol
root.mainloop()
