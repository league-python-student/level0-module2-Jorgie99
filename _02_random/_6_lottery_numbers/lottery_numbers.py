import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    # TODO 1) Get 6 random numbers to put on your lottery ticket
    lt1 = random.randint(1, 9)
    str(lt1)
    lt2 = random.randint(1, 9)
    str(lt2)
    lt3 = random.randint(1, 9)
    str(lt3)
    lt4 = random.randint(1, 9)
    str(lt4)
    lt5 = random.randint(1, 9)
    str(lt5)
    lt6 = random.randint(1, 9)
    str(lt6)
    # TODO 2) Display the selected numbers to the user in a pop-up
    messagebox.showinfo(title='Lottery Ticket', message=''+ str(lt1) + str(lt2) + str(lt3) + str(lt4) + str(lt5) + str(lt6))
    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
