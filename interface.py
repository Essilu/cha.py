import os
import time
from tkinter import *

def run_chapy():
    os.system('chapy.py')
    img = PhotoImage(file="NewCat.png")
    img_label = Label(gui, image=img)
    img_label.image = img
    img_label.pack()

#create a window
gui = Tk()
gui.geometry("500x500")
gui.title("Cha.py")

#Creation texte
champ_label = Label(gui, text="Faites un choix")
champ_label.pack()

#Création bouton
btn_chapy = Button(gui, text="Créer un chat !", bg ="white", fg="black", command=run_chapy)
btn_chapy.pack()




gui.mainloop()