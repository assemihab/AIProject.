from tkinter import *
import tkinter
def s_d_gui():
    gui=Tk()
    #choosing the alg.
    label=Label(gui, text="Select the Algorithm Type: ", fg='red', font=("Helvetica", 10))
    label.place(x=10, y=10)
    algorithmSelected=IntVar()
    algorithmSelected.set(1)
    r1=Radiobutton(gui, text="Minimax algorithm", variable=algorithmSelected, value=1)
    r2=Radiobutton(gui, text=" Alpha-Beta pruning algorithm", variable = algorithmSelected,value=2)
    r1.place(x=35,y=40)
    r2.place(x=200, y=40)

    #choosing the diff level.
    label2=Label(gui, text="Select the difficulty level of the game: ", fg='red', font=("Helvetica", 10))
    label2.place(x=10, y=70)
    difficultySelected=IntVar()
    difficultySelected.set(1)
    r1=Radiobutton(gui, text="Easy", variable= difficultySelected, value=2)
    r2=Radiobutton(gui, text=" Meduim", variable = difficultySelected,value=3)
    r3=Radiobutton(gui, text="Hard", variable= difficultySelected, value=5)
    r1.place(x=35,y=100)
    r2.place(x=100, y=100)
    r3.place(x=200, y=100)
    button = tkinter.Button(gui, text = "Start Game", fg = "red")
    button.place(x=225, y=150)
    gui.title('Connect 4')
    gui.geometry("500x200+10+20")
    gui.mainloop()
    alg=algorithmSelected.get()
    diffLevel=difficultySelected.get()
    return alg,diffLevel
