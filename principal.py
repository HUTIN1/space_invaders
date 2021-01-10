#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 09:55:28 2020

@author: nathan
"""

from tkinter import PhotoImage

from fenetre import fenetre



largeur_x_missile=10
largeur_y_missile=20
largeur_x_perso=40
largeur_y_perso=25
largeur_x_mechant=35
largeur_y_mechant=30
freq_missile=100
freq_mechant=200
pas_mechant=20
pas_missile=10
pas_perso=20
proba_missile_mechant=0.02
nb_mechant=9
nb_ligne_mechant=2



Jeu=fenetre(largeur_x_mechant,largeur_y_mechant,largeur_x_missile,
            largeur_y_missile,largeur_x_perso,largeur_y_perso,
            freq_missile,freq_mechant,pas_mechant,pas_missile,pas_perso,
            proba_missile_mechant,nb_mechant,nb_ligne_mechant)

Jeu.geometry("700x500")

mechant=PhotoImage(file="mechant.gif")
perso=PhotoImage(file="perso.gif")
missile=PhotoImage(file="missile.gif")

Jeu.setimage(mechant,perso,missile)


Jeu.mainloop()
