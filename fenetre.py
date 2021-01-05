#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 08:57:47 2020

@author: nathan
"""



from objets import cPerso, cMechant, cMissile

from tkinter import Tk, Canvas, Button



class fenetre(Tk):
    def __init__(self,largeur_x_mechant,largeur_y_mechant,largeur_x_missile,largeur_y_missile,largeur_x_perso,largeur_y_perso):
        Tk.__init__(self)
        self.__mechant=[]
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
        
        self.game=Button(self,text="Game",command=self.start)
        self.game.place(x=550,y=200)

        
    def setimage(self,mechant,perso,missile):
        self.__image_mechant=mechant
        self.__image_perso=perso
        self.__image_missile=missile
        
    def settirer(self,numero,posx,posy):
        self.__missiles[numero]=cMissile(self.__largeur_x_missile,self.__largeur_y_missile,"missile",
                      self.__image_missile,posx,posy,self.canvas,self,numero)
        
        
    def start(self):
        self.__perso=cPerso(self.__largeur_x_perso,self.__largeur_y_perso,
                            "perso",self.__image_perso,400,400,self.canvas,self)
        self.__mechant.append(cMechant(self.__largeur_x_mechant,self.__largeur_y_mechant,
                            "mechant",self.__image_mechant,100,100,self.canvas,self))
        
        



    def fCollision(self,posX_missile,posY_missile,numero_missile,missile):
        (mX,mY)=self.__mechant[0].fGet()
        print(type(mX))
        if mX-self.__largeur_x_missile/2 <= posX_missile <= mX+self.__largeur_x_missile/2 and mY-self.__largeur_y_missile/2 <= posY_missile <= mY+self.__largeur_y_missile/2:
            print("oui")
            self.__mechant.pop(0)
            del self.__missile[numero_missile]
        else:
            self.after(1000,missile.fDeplacement_missile)

            
