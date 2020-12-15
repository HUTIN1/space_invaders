#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 08:57:47 2020

@author: nathan
"""



from objets import cPerso, cMechant

from tkinter import Tk, Canvas, Button



class fenetre(Tk):
    def __init__(self,largeur_x_missile,largeur_y_missile,largeur_x_pero,largeur_y_pero):
        Tk.__init__(self)
        self.__mechant=None
        self.__perso=None
        self.__missiles=[]
        self.__blocks=[]
        self.__imgae_mechant=None
        self.__image_perso=None
        self.__image_missile=None
        self.__largeur_x_missile=largeur_x_missile
        self.__largeur_y_missile=largeur_y_missile
        self.__largeur_x_pero=largeur_x_pero
        self.__largeur_y_pero=largeur_y_pero
        self.__image_fond=None
        self.creer_widget()

    def creer_widget(self):
        self.canvas=Canvas(self,width=500,height=500)
        self.canvas.place(x=0,y=0)
        
        self.quitter=Button(self,text="quitter",command=self.destroy)
        self.quitter.place(x=550,y=300)
        
        self.game=Button(self,text="Game",command=self.start)
        self.game.place(x=550,y=200)
        
    def setimage(self,mechant,perso,missile):
        self.__image_mechant=mechant
        self.__image_perso=perso
        self.__image_missile=missile
        
    def start(self):
        self.__perso=cPerso(self.__largeur_x_pero,self.__largeur_y_pero,
                            "perso",self.__image_perso,400,400,self.canvas)
        self.__mechant=cMechant(self.__largeur_x_mechant,self.__largeur_y_mechant,
                            "mechant",self.__image_mechant,400,400,self.canvas)
        
        