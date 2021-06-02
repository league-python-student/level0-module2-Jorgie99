import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    simpledialog.askstring(title=None, prompt='Ask a question')
    # Make a variable and initialize it to a random number between 0 and 3
    ballnumber = random.randint(0, 3)
    # If the random number is 0
    if ballnumber == 0:
        messagebox.showinfo(title=None, message='yes')
        # tell the user "Yes"

    # If the random number is 1
    if ballnumber == 1:
        # tell the user "No"
        messagebox.showinfo(title=None, message='No')
    # If the random number is 2
    if ballnumber == 2:
        # tell the user "Maybe you should ask Google?"
        messagebox.showinfo(title=None, message='Maybe you should ask Google?')
    # If the random number is 3
    if ballnumber == 3:
        # write your own answer
        messagebox.showinfo(title=None, message='Ask again later')