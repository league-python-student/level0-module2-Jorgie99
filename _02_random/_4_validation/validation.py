import random
from tkinter import messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    random_number = random.randint(1, 5)

    print(random_number)

    # TODO 1) Use each value of random_number to give the user a random compliment
    for i in range(10):
        if random_number == 1:
            messagebox.showinfo(title='Compliment 1', message='You are amazing')
        elif random_number == 2:
            messagebox.showinfo(title='Compliment 2', message='You are nice')
        elif random_number == 3:
            messagebox.showinfo(title='Compliment 3', message='You are great')
        elif random_number == 4:
            messagebox.showinfo(title='Compliment 4', message='You are kind')
        elif random_number == 5:
            messagebox.showinfo(title='Compliment 5', message='You are funny')
    # TODO 2) Repeat all the code above 10 times

    # TODO 3) Find someone to test out your program. They will like it :)
