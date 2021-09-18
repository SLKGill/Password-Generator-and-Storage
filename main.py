from tkinter import *
from random import randint

root = Tk()
root.title = "Password Generator"
root.geometry("500x300")

# want ASCII characters: 33 to 126
my_password = randint(33, 126)  # generates integer
my_password = chr(my_password)  # convert to ASCII


# generating strong password
def new_rand():
    pw_entry.delete(0, END)  # clear entry box
    pw_length = int(my_entry.get())  # pw length and convert to integer
    my_password = ''  # create variable to hold pw, nothing for now

    # loop through password length
    for i in range(pw_length):
        my_password += chr(randint(33, 126))

    # output pw to screen
    pw_entry.insert(0, my_password)

# copy to clipboard


def clipper():
    root.clipboard_clear()  # clear clipboard
    root.clipboard_append(pw_entry.get())  # copy to clipboard

    # pop up saying your password has been copied and is ready to be pasted

# new function for storing/saving your passwords
# add a button for save password, pop up enter for what it is and put it away
# another tab for accessing saved passwords
# delete them, edit them


# label frame
lf = LabelFrame(root, text="Number of Characters: ")
lf.pack(pady=20)

# entry box for number of characters
my_entry = Entry(lf, font=("Helvetica", 20))
my_entry.pack(pady=20, padx=20)

# entry box for returned password, so we can copy the text (can't copy labels)
pw_entry = Entry(root, text='', font=("Helvetica", 20), bd=0, bg="SystemButtonFace")
pw_entry.pack(padx=0, pady=20)

# create a frame for our buttons
my_frame = Frame(root)
my_frame.pack(pady=20)

# create buttons
my_button = Button(my_frame, text="Generate Strong Password", command=new_rand)
my_button.grid(row=0, column=0, padx=10)

clip_botton = Button(my_frame, text="Copy to Clipboard", command=clipper)
clip_botton.grid(row=0, column=1, pady=10)
