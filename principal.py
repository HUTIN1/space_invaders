#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 09:55:28 2020

@author: nathan
"""

from fenetre import fenetre

largeur_x_missile=5
largeur_y_missile=10
largeur_x_pero=30
largeur_y_pero=10

Jeu=fenetre(largeur_x_missile,largeur_y_missile,largeur_x_pero,largeur_y_pero)
Jeu.geometry("700x500")


Jeu.mainloop()

