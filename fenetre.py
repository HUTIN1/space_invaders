#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 08:57:47 2020

@author: nathan
"""

from tkinter import Tk, Canvas, Button

class fenetre(Tk):
    def __init__(self,largeur_x_missile,largeur_y_missile,largeur_x_perso,largeur_y_perso):
        Tk.__init__(self)
        self.__mechant=None
        self.__largeur_x_mechant=largeur_x_mechant
        self.__largeur_y_mechant=largeur_y_mechant
        self.__perso=None
        self.__missiles={}
        self.__blocks=[]
        self.__image_mechant=None
        self.__image_perso=None
        self.__image_missile=None
        self.__largeur_x_missile=largeur_x_missile
        self.__largeur_y_missile=largeur_y_missile
        self.__largeur_x_perso=largeur_x_perso
        self.__largeur_y_perso=largeur_y_perso
        self.__image_fond=None
        self.creer_widget()

    def creer_widget(self):
        self.canvas=Canvas(self,width=500,height=500)
        self.canvas.place(x=0,y=0)
        
        self.quitter=Button(self,text="quitter",command=self.destroy)
        self.quitter.place(x=550,y=300)
        
        self.game=Button(self,text="Game")
        self.game.place(x=550,y=200)


    def fCollision(self,posX_missile,posY_missile):
        mX,mY=self.__mechant.get()
        if self.__posX_missile==mX and self.__posY_missile+self.__largeur_y_missile==mY+self.__largeur_y_mechant :
            self.__mechant=None
            self.__missile=