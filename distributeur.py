# Auteur Ewan GRIGNOUX LEVERT
# coding: utf-8
# 
from PIL import ImageTk  # On importe la bibliothèque PIL
import sys 
from tkinter import *
import random

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
    return {0.01:20, 0.02:5, 0.05:5, 0.1:5, 0.2:5, 0.5:5, 1:20, 2:20}

def initPaie():
    return {0.01:0, 0.02:0, 0.05:0, 0.1:0, 0.2:0, 0.5:0, 1:0, 2:0}

# Les variables
piecesReserve = initReserve()
piecesPaie = initPaie()
sommeRestant = 3.2
nombrePieces = 0

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
    '''
    réagit au choix d'une pièce : à compléter
    '''
    global piecesReserve, piecesPaie, sommeRestant
    
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
    print(pieceChoisie)
    
    for cle in piecesPaie.keys():
        if pieceChoisie == cle:
            piecesPaie[cle] +=1
    print(piecesPaie)

    for cle in piecesReserve.keys():
        if pieceChoisie == cle:
            piecesReserve[cle] -=1
    dessinerPieces(piecesReserve)

    sommeRestant -= pieceChoisie
    sommeRestant = round(sommeRestant,2)
    print (sommeRestant)


# Réglage des paramètres de la fenêtre
maFenetre.title("Mon distributeur")  # Le titre
maFenetre.geometry('700x400+400+200')  # La position
maFenetre.configure(bg = 'red')  # la couleur de fond

canvas = Canvas(maFenetre, bg="black", width=700, height=200)
canvas.pack()
canvas.bind('<Button-1>',choisirPiece)

####### PROGRAMME PRINCIPAL
dessinerPieces(piecesReserve)

# Lancement du gestionnaire d'événements
maFenetre.mainloop()
sys.exit() 