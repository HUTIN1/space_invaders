#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 09:55:28 2020

@author: HUTIN Nathan, Tran Matthieu
"""
"""
Programme principal
"""


#importation de la class fenetre et photoimage de tkinter
from tkinter import PhotoImage
from fenetre import fenetre


#-----------------------Les variables------------------------# 

#toute les variables du missile
largeur_x_missile=10
largeur_y_missile=20
freq_missile=100
pas_missile=10



#toutes les variables du personna
largeur_x_perso=40
largeur_y_perso=25
pas_perso=20


#toutes les varibles des mechants
largeur_x_mechant=35
largeur_y_mechant=30
freq_mechant=200
pas_mechant=20
proba_missile_mechant=0.02
nb_mechant=6
nb_ligne_mechant=2


#toutes les variables des blocks
largeur_blocks=20
hauteur_blocks=20
nbgrosblocks=4
nbligneblocks=3
nbcolonneblocks=3



#initialisation de l'objet Jeu
Jeu=fenetre(largeur_x_mechant,largeur_y_mechant,largeur_x_missile,
            largeur_y_missile,largeur_x_perso,largeur_y_perso,
            freq_missile,freq_mechant,pas_mechant,pas_missile,pas_perso,
            proba_missile_mechant,nb_mechant,nb_ligne_mechant,largeur_blocks,hauteur_blocks,
            nbgrosblocks,nbligneblocks,nbcolonneblocks)



#taille de la fenetre
Jeu.geometry("700x500")



#importation des images
mechant=PhotoImage(file="mechant.gif")
perso=PhotoImage(file="perso.gif")
missile=PhotoImage(file="missile.gif")
gameover=PhotoImage(file="gameover.gif")
coeur=PhotoImage(file="coeur.gif")
win=PhotoImage(file="Win.gif")

#importation des images dans notre objets fenetre
Jeu.setimage(mechant,perso,missile,gameover,coeur,win)

"""À ne pas lire"""
Jeu.bind('m',Jeu.setcoeur) #Commance de triche permettant de s'ajouter une vie lorqu'on appuie sur "m"
Jeu.bind('p',Jeu.setvitessemissile) #Commande de triche permattant d'accélerer la vitesse de tous les tirs (alliés et ennemis) lorqu'on appuie sur "p"

Jeu.mainloop()
