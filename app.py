from tkinter import*
import tkinter
import webbrowser

def open_github_profil():
    webbrowser.open_new("https://github.com/superhughhh")

#création de la fenetre
master = Tk()

#personnalisation de la fenetre
master.title("My Application")
master.geometry("400x400")
master.minsize(300, 300)
master.iconphoto(False, tkinter.PhotoImage(file="logo.png")) #icone App
master.config(background="#005f86")

#Creation de la frame
frame = Frame(master, bg="#005f86", bd=1, relief=SUNKEN)

#Ajout du texte
label_subtitle = Label(frame, text="GitHub Teleporter", font=("Courrier", 20), bg="#005f86", fg="white") #on gere les propriété du label
label_subtitle.pack()#on gere sa position

label_descritption = Label(frame, text="Hello, ici Superhughhh", font=("Courrier", 10), bg="#005f86", fg="white") #on gere les propriété du label
label_descritption.pack()#on gere sa position

#ajout d'un bouton
link_button = Button(frame, text="Cliquez pour découvrir mon GitHub", font=("Courrier", 10), bg="white", fg="#005f86", command=open_github_profil)
link_button.pack(pady=2, fill=X)


frame.pack(expand=YES)

#affichage(boucle de l'app)
master.mainloop()