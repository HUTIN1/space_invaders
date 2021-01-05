#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 08:57:47 2020

@author: nathan
"""

"""
TO DO
tuer plusieur méchant
pimpé
gameover
enlever le bug du bouton game
"""



from objets import cPerso, cMechant, cMissile

from tkinter import Tk, Canvas, Button
from random import randint



class fenetre(Tk):
    # Initialisation de la fenêtre
    def __init__(self,largeur_x_mechant,largeur_y_mechant,largeur_x_missile,largeur_y_missile,largeur_x_perso,largeur_y_perso):
        Tk.__init__(self)
        self.__mechant={} #Dictionnaire contenant tous les méchants
        self.__largeur_x_mechant=largeur_x_mechant
        self.__largeur_y_mechant=largeur_y_mechant
        self.__perso=None #Création de notre vaisseau
        self.__missiles={} #Dictionnaire contenant tous les missiles
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

        #Fonction permet de créer les widget du canvas ainsi que des boutons pour quitter et lancer le jeu.
    def creer_widget(self):
        self.canvas=Canvas(self,width=500,height=500)
        self.canvas.place(x=0,y=0)
        
        self.quitter=Button(self,text="quitter",command=self.destroy)
        self.quitter.place(x=550,y=300)
        
        self.game=Button(self,text="Game",command=self.start)
        self.game.place(x=550,y=200)

        #Fonction permettant de définir les images et les attribuer à la classe
    def setimage(self,mechant,perso,missile):
        self.__image_mechant=mechant
        self.__image_perso=perso
        self.__image_missile=missile
        
        #Fonction permettant de créer un missile et de l'ajouter au dictionnaire self.__missiles
    def settirer(self,numero,posx,posy):
        self.__missiles[numero]=cMissile(self.__largeur_x_missile,self.__largeur_y_missile,"missile",
                      self.__image_missile,posx,posy,self.canvas,self,numero)
    
        
        #Fonction permettant de lancer le programme lorsqu'on appuie sur le boutton "game", il crée les méchants et notre vaisseau
    def start(self):

        self.__perso=cPerso(self.__largeur_x_perso,self.__largeur_y_perso,
                            self.__image_perso,400,400,self.canvas,self)
        X=100
        Y=100
        for i in range (4):
            self.__mechant[str(i)]=cMechant(self.__largeur_x_mechant,self.__largeur_y_mechant,
                            str(i),self.__image_mechant,X,Y,self.canvas,self)
            X=X+35
        self.after(500,self.fAllmechant)
        
        
    #Fonction permettant de gérer le déplacement du "bloc" de méchants en particulier lorsque le groupe de méchant doit changer de direction
    def  fAllmechant(self):
        a=0
        for i in self.__mechant:
            mX,mY=self.__mechant[i].fGet()
            if mX>=470 or mX<=30:
                a=1
        if a==1:
            for i in self.__mechant:
                self.__mechant[i].fChangecote()
                self.__mechant[i].fChangeposY()
                
        self.after(500,self.fAllmechant)

        #Fonction permettant de finir la partie en cas de défaite en affichant GameOver
    def fGameover (self):
        vX,vY=self.__perso.fGet()
        for i in self.__mechant:
            mX,mY=self.__mechant[i].fGet()
            if vX==mX and vY==mY:
                print("Perdu")



    def fCollision(self,posX_missile,posY_missile,numero_missile,missile):
        l=[]
        for cle, mechant in self.__mechant.items():
            (mX,mY)=mechant.fGet()
            if mX-self.__largeur_x_missile/2 <= posX_missile <= mX+self.__largeur_x_missile/2 and mY-self.__largeur_y_missile/2 <= posY_missile <= mY+self.__largeur_y_missile/2:
                print("collision")
                mechant.setmort()
                l.append(cle)             
                print(self.__missiles,"missile")
                print(self.__mechant,"mechant",type(cle))
                print(numero_missile)
        if len(l)!=0:
            del self.__mechant[cle]
            del self.__missiles[numero_missile]
            print(self.__missiles,"missile")
            print(self.__mechant,"mechant",)


            
