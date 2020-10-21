from tkinter import *
root = Tk()

texto = Text(root)
texto.pack()
texto.config(width=30, height=10, font=("Consolas",12), padx=10, pady=10, selectbackground="red")#Se pone en caracteres


root.mainloop()