# Auteur Pascal VINCENT & Ewan GRIGNOUX LEVERT
# coding: utf-8
# mai 2020
from PIL import ImageTk  # On importe la bibliothèque PIL
import sys 
from tkinter import *
import random
from tkinter.messagebox import showerror

# Création de la fenêtre principale
maFenetre = Tk()

# Chargement des images
image_1cent = ImageTk.PhotoImage(file="1cent.png")  
image_2cent = ImageTk.PhotoImage(file="2cent.png")
image_5cent = ImageTk.PhotoImage(file="5cent.png")
image_10cent = ImageTk.PhotoImage(file="10cent.png")
image_20cent = ImageTk.PhotoImage(file="20cent.png")
image_50cent = ImageTk.PhotoImage(file="50cent.png")
image_1euro = ImageTk.PhotoImage(file="1euro.png")
image_2euro = ImageTk.PhotoImage(file="2euro.png")

# Mes fonctions d'initialisation
def initReserve():
    return {2:20, 1:20, 0.5:5, 0.2:5, 0.1:5, 0.05:5, 0.02:5, 0.01:20}

def initPaie():
    return {0.01:0, 0.02:0, 0.05:0, 0.1:0, 0.2:0, 0.5:0, 1:0, 2:0}

def init():
    global sommeRestant

    sommeRestant = 0
    nombrePieces = 0
    piecesReserve = initReserve()
    piecesPaie = initPaie()
    new.grid(row=1, column=1, padx=5, pady=5)
    txt_infoMontant.set(f"Vous pouvez choisir un nouvel article.")
    txt_prix.set(sommeRestant)
    dessinerPieces(piecesReserve)

def choisirArticle():
    global sommeRestant

    new.pack_forget()
    p = float(prix.get())
    if p <=20 and p>0:
        sommeRestant = p
        piecesReserve = initReserve()
        piecesPaie = initPaie()
        nombrePieces = 0
        txt_infoMontant.set(f"Vous avez utilisez {nombrePieces} pièces. \n Il vous reste {sommeRestant}€ à payer.")
        txt_prix.set(sommeRestant)
    else:
        showerror('Attention',"Le prix doit être compris entre 0.01€ et 20 €")

# Les variables
sommeRestant = 0
nombrePieces = 0
piecesReserve = initReserve()
piecesPaie = initPaie()
txt_prix = StringVar()
txt_prix.set(sommeRestant)
txt_infoMontant = StringVar()
txt_infoMontant.set(f"Vous pouvez choisir un nouvel article.")

# Fonctions
def dessinerPieces(reserve):
    '''
    Affiche les pièces de la réserve
    Ne pas modifier
    '''
    canvas.delete('all')
    for indice in range(reserve[0.01]):
        canvas.create_image(38, 150-5*indice, image=image_1cent)

    for indice in range(reserve[0.02]):
        canvas.create_image(110, 150-5*indice, image=image_2cent)

    for indice in range(reserve[0.05]):
        canvas.create_image(190, 150-5*indice, image=image_5cent)
        
    for indice in range(reserve[0.1]):
        canvas.create_image(275, 150-5*indice, image=image_10cent)
        
    for indice in range(reserve[0.2]):
        canvas.create_image(360, 150-5*indice, image=image_20cent)
        
    for indice in range(reserve[0.5]):
        canvas.create_image(450,150-5*indice, image=image_50cent)

    for indice in range(reserve[1]):
        canvas.create_image(548,150-5*indice, image=image_1euro)

    for indice in range(reserve[2]):
        canvas.create_image(646,150-5*indice, image=image_2euro)

def choisirPiece(event):
    global piecesReserve, piecesPaie, sommeRestant, nombrePieces, txt_infoMontant
    
    pieceChoisie = 0
    if event.x < 70:
        pieceChoisie = 0.01
    elif event.x < 150:
        pieceChoisie = 0.02
    elif event.x < 230:
        pieceChoisie = 0.05
    elif event.x < 315:
        pieceChoisie = 0.1
    elif event.x < 400:
        pieceChoisie = 0.2
    elif event.x < 500:
        pieceChoisie = 0.5
    elif event.x < 600:
        pieceChoisie = 1
    else :
        pieceChoisie = 2
    
    if pieceChoisie <= sommeRestant:
        for cle in piecesPaie.keys():
            if pieceChoisie == cle:
                piecesPaie[cle] +=1

        for cle in piecesReserve.keys():
            if pieceChoisie == cle:
                piecesReserve[cle] -=1
        dessinerPieces(piecesReserve)

        nombrePieces += 1
        sommeRestant -= pieceChoisie
        sommeRestant = round(sommeRestant,2)
        
        if sommeRestant == 0:
            txt_infoMontant.set(f"Merci, vous avez donneé {nombrePieces} pièces. \n Vous pouvez choisir un nouvel article.")
            new.grid(row=1, column=1, padx=5, pady=5)
        else:
            txt_infoMontant.set(f"Vous avez donneé {nombrePieces} pièces. \n Il vous reste {sommeRestant}€ à payer.")
    else:
        showerror('Attention', 'Nous ne rendons pas la monnaie!')

def Ordinateur():
    global piecesPaie, sommeRestant, nombrePieces, piecesReserve, txt_infoMontant

    piecesPaie = initPaie()
    nombrePieces = 0
    for cle in piecesReserve.keys():
        while sommeRestant >= float(cle):
            sommeRestant -= float(cle)
            sommeRestant = round(sommeRestant,2)
            nombrePieces += 1
            piecesReserve[cle] -= 1
            piecesPaie[cle] += 1
            dessinerPieces(piecesReserve)
    
    listepiece=""
    for cle, value in piecesPaie.items():
        if piecesPaie[cle] != 0:
            listepiece += f'{cle}: {value}'
            listepiece += "\n"

    txt_infoMontant.set(f"L'ordinateur à utilisé {nombrePieces} pièces.\n {listepiece}")
    new.grid(row=1, column=1, padx=5, pady=5)

# Réglage des paramètres de la fenêtre
maFenetre.title("Mon distributeur")  # Le titre
maFenetre.geometry('700x400+400+200')  # La position
maFenetre.configure(bg = 'red')  # la couleur de fond

canvas = Canvas(maFenetre, bg="black", width=700, height=200)
canvas.grid(row=0, columnspan=3, padx=5, pady=5)
canvas.bind('<Button-1>',choisirPiece)

# PROGRAMME PRINCIPAL
dessinerPieces(piecesReserve)

# Interface
new = Button(maFenetre, text='Nouvel article', command=choisirArticle)
new.grid(row=1, column=1, padx=5, pady=5)

infoMontant = Label(maFenetre, textvariable = txt_infoMontant)
infoMontant.grid(row=1, column=0, padx=5, pady=5)

prix = Entry(maFenetre, textvariable=txt_prix, width=5)
prix.grid(row=1, column=2, padx=5, pady=5)

reinitialiser = Button(maFenetre,text="Réinitialiser", command = init)
reinitialiser.grid(row=2, column=2, padx=5, pady=5)

ordinateur = Button(maFenetre, text="Choix de l'ordinateur", command=Ordinateur)
ordinateur.grid(row=2, column=1, padx=5, pady=5)

# Lancement du gestionnaire d'événements
maFenetre.mainloop()
sys.exit() 