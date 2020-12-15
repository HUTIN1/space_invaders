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

Jeu=fenetre(largeur_x_missile,largeur_y_missile,largeur_x_perso,largeur_y_perso)
Jeu.geometry("700x500")

mechant=PhotoImage(file="mechant.gif")
perso=PhotoImage(file="perso.gif")
missile=PhotoImage(file="missile.gif")

Jeu.setimage(mechant,perso,missile)


Jeu.mainloop()

