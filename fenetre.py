#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 09:55:28 2020

@author: HUTIN Nathan, Tran Matthieu
"""

"""
fichier contenant la class fenetre
"""


#importation des class util à fenetre
from objets import cPerso, cMechant, cMissile, cBlocks

from tkinter import Tk, Canvas, Button, Label, IntVar



class fenetre(Tk):
    """
    cette class à pour but:
        -gérer les interactions entre les différents objets
        crée dans le fichier objets.py
        -controler la vie et la mort de notre vaisseau
        -le systeme de score
        -crée les widgets de la fenetre
        -gére la suppression et la creation des missiles, blocks et des mechants
    """
    
    # Initialisation de la fenêtre
    def __init__(self,largeur_x_mechant,largeur_y_mechant,largeur_x_missile,largeur_y_missile,
                 largeur_x_perso,largeur_y_perso,freq_missile,freq_mechant,
                 pas_mechant,pas_missile,pas_perso,proba_missile_mechant,nb_mechant,
                 nb_ligne_mechant,largeur_blocks,hauteur_blocks,nbgrosblocks,nbligneblocks,
                 nbcolonneblocks):
        Tk.__init__(self)
        self.__mechant={} #Dictionnaire contenant tous les méchants
        self.__largeur_x_mechant=largeur_x_mechant
        self.__largeur_y_mechant=largeur_y_mechant
        self.__perso=None #variable contenant notre vaisseau
        self.__missiles={} #Dictionnaire contenant tous les missiles
        self.__blocks={} #Dictionniaire contenant les blocks permettant au vaisseau de se sacher
        self.__image_mechant=None
        self.__image_perso=None
        self.__image_missile=None
        self.__image_gameover=None
        self.__image_coeur=None
        self.__image_win=None
        self.__score=IntVar() 
        self.__largeur_x_missile=largeur_x_missile
        self.__largeur_y_missile=largeur_y_missile
        self.__largeur_x_perso=largeur_x_perso
        self.__largeur_y_perso=largeur_y_perso
        self.__freq_missile=freq_missile
        self.__freq_mechant=freq_mechant
        self.__pas_mechant=pas_mechant
        self.__pas_missile=pas_missile
        self.__pas_perso=pas_perso
        self.__proba_missile_mechant=proba_missile_mechant
        self.__nb_mechant=nb_mechant
        self.__nb_ligne_mechant=nb_ligne_mechant
        self.__largeur_blocks=largeur_blocks
        self.__hauteur_blocks=hauteur_blocks
        self.__nbgrosblocks=nbgrosblocks
        self.__nbligneblocks=nbligneblocks
        self.__nbcolonneblocks=nbcolonneblocks
        self.__nbvie=3
        self.__nb_tire=0
        self.creer_widget()


    def creer_widget(self):
        #Fonction permet de créer les widget du canvas ainsi que des boutons pour quitter et lancer le jeu.
        
        
        self.canvas=Canvas(self,width=500,height=500,bg="black")
        self.canvas.place(x=0,y=0)
        
        self.quitter=Button(self,text="quitter",command=self.destroy,activebackground="red")
        self.quitter.place(x=550,y=300)
        
        self.game=Button(self,text="Game",command=self.start,activebackground="red")
        self.game.place(x=550,y=200)

        self.__score.set(0)
        self.label_score=Label(self,textvariable=self.__score) 
        self.label_score.place(x=550,y=100)



        

    def setimage(self,mechant,perso,missile,gameover,coeur,win):
        """
        Fonction permettant de définir les images et crée notre vaisseau
        les parametre de l'entrée sont les images utiles au jeu
        """
        
        self.__image_mechant=mechant
        self.__image_perso=perso
        self.__image_missile=missile
        self.__image_gameover=gameover
        self.__image_coeur=coeur
        self.__image_win=win
        self.__perso=cPerso(self.__largeur_x_perso,self.__largeur_y_perso,
                            self.__image_perso,400,450,self.canvas,self,self.__pas_perso)
        
        
        
        
    def setcoeur(self,event):
        """
        Fonction permettant de nous rajouter des coeurs
        appuyer sur m pendant une parti pour activer cette fonction
        """
        self.__nbvie+=1
        poscoeur=20+(self.__nbvie-1)*40
        self.canvas.create_image(poscoeur,50,image=self.__image_coeur, tags='coeur'+str(self.__nbvie-1))
        
        
        
        
    def setvitessemissile(self,event):
        """
        Fonction qui augmente la fréquence de deplacement des prochains missile
        envoyé
        appyuer sur p pour activer cette fonction
        """
        self.__freq_missile=int(self.__freq_missile//2)

    

    
    def settirer(self,posx,posy,camp):
        """
        Fonction permettant de créer un missile et de l'ajouter au dictionnaire self.__missiles
        en parametre la position de creation  du missile en x et y ,et son camp  (si il est mechant ou gentil)
        """
        pas=self.__pas_missile
        if camp=="perso":
            pas=-pas
        self.__missiles[self.__nb_tire]=cMissile(self.__largeur_x_missile,self.__largeur_y_missile,
                      self.__image_missile,posx,posy,self.canvas,self,self.__nb_tire,camp,pas,self.__freq_missile)
        self.__nb_tire+=1
    
    
    
        
        
    def start(self):
        """
        Fonction permettant de lancer le programme lorsqu'on appuie sur le bouton "game", 
        il crée les méchants et les blocks
        """
        self.__mechant={}
        self.after(self.__freq_mechant,self.fAllmechant)
        X=100
        Y=100
        a=0
        b=self.__nb_mechant//self.__nb_ligne_mechant
        if self.__nb_mechant%self.__nb_ligne_mechant >= 1:
            a=1
        for j in range(self.__nb_ligne_mechant+a):
            X=100
            if j<=self.__nb_ligne_mechant-1:
                for i in range (j*b,j*b+b):
                    self.__mechant[str(i)]=cMechant(self.__largeur_x_mechant,self.__largeur_y_mechant,
                                    str(i),self.__image_mechant,X,Y,self.canvas,self,self.__pas_mechant,
                                    self.__freq_mechant,self.__proba_missile_mechant)
                    X=X+35
                Y+=50
            else:
                for i in range(j*b,j*b+self.__nb_mechant%self.__nb_ligne_mechant):
                    self.__mechant[str(i)]=cMechant(self.__largeur_x_mechant,self.__largeur_y_mechant,
                                    str(i),self.__image_mechant,X,Y,self.canvas,self,self.__pas_mechant,
                                    self.__freq_mechant,self.__proba_missile_mechant)
                    X=X+35
                Y+=50
        self.canvas.delete('image_gameover')
        self.canvas.delete('image_win')
        self.__nbvie=3
        self.__score.set(0)
        poscoeur=20
        for i in range (self.__nbvie):
            self.canvas.create_image(poscoeur,50,image=self.__image_coeur, tags='coeur'+str(i))
            poscoeur=poscoeur+40
        self.game.configure(state='disabled') 

 
        for i in range(self.__nbgrosblocks):
            xi=i*self.__largeur_blocks*2*self.__nbcolonneblocks
            y=350
            for j in range(i*self.__nbligneblocks,i*self.__nbligneblocks+self.__nbligneblocks):
                x=xi
                y+=self.__hauteur_blocks
                for k in range(j*self.__nbcolonneblocks,j*self.__nbcolonneblocks+self.__nbcolonneblocks):
                    x+=self.__largeur_blocks
                    self.__blocks[k]=cBlocks(x,y,self.canvas,self.__largeur_blocks,self.__hauteur_blocks,k)
                    


    
        
        
    
    def  fAllmechant(self):
        """
        Fonction permettant de gérer le déplacement du "bloc" de méchants en particulier 
        lorsque le groupe de méchant doit changer de direction
        """
        a=0
        for i in self.__mechant:
            mX,mY=self.__mechant[i].fGet()
            if mX>=470 or mX<=30:
                a=1
        if a==1:
            for i in self.__mechant:
                self.__mechant[i].fChangecote()
                self.__mechant[i].fChangeposY()
        if self.__nbvie!=0:
            self.after(self.__freq_mechant,self.fAllmechant)
            self.fVaisseau_touche()
            
            

        
    def fGame_over (self):
        #Fonction permettant d'appliqer la défaite en affichant GameOver et en tuant tout les mechant
            self.game.configure(state='normal')
            for cle in self.__mechant.keys():
                self.__mechant[cle].setmort()
            self.canvas.create_image(250,250,image=self.__image_gameover, tags='image_gameover')


    def fVaisseau_touche(self):
        """
        Fonction qui vérifie si les méchant touche notre vaisseau
        Et applique gameover ci cela arrive
        """
        
        vX,vY=self.__perso.fGet()
        a=0
        for mechant in self.__mechant.values():
            mX,mY=mechant.fGet()
            if  vY<=mY:
                a=1
        if a==1:
            self.fGame_over()
                


    def fCollision(self,posX_missile,posY_missile,numero_missile,missile,camp):
        """
        fonction qui gere la collision entre les millies et tout les autres objets(notre perso, les mechants et les blocks)
        En parametre la position du missile, son numéro, le missile qui appele cette fonction et son camp
        Cette fonction est appelée à chaque fois qu'un missile bouge
        """
        
        #variables permettant de contourner les problemes qui python nous donne
        l=[] #util dans la suppresion du mechant et du missile
        b=[]#util dans la suppresion d'un blocks et du missile
        
        #gestion de la collision entre le missile et les mechants
        if camp=="perso":
            for cle, mechant in self.__mechant.items():
                (mX,mY)=mechant.fGet()
                if mX-self.__largeur_x_mechant/2 <= posX_missile <= mX+self.__largeur_x_mechant/2 and mY-self.__largeur_y_mechant/2 <= posY_missile <= mY+self.__largeur_y_mechant/2:
                    l.append(cle)
                    l.append(mechant)
            #suppression du mechant et du missile
            #la suppression n'est pas faites dans la boucle juste au dessus car python refuse de faire cela
            if len(l)!=0:
                del self.__mechant[l[0]]
                del self.__missiles[numero_missile]
                l[1].setmort()
                missile.setmort()
                self.fScore()
                
                
        #gestion de la collision entre le missile et notre vaisseau
        elif camp=="mechant":
            mX,mY=self.__perso.fGet()
            if mX-self.__largeur_x_perso/2 <= posX_missile <= mX+self.__largeur_x_perso/2 and mY-self.__largeur_y_perso/2 <= posY_missile <= mY+self.__largeur_y_perso/2:
                self.canvas.delete("coeur"+str(self.__nbvie-1))
                self.__nbvie=self.__nbvie-1
                del self.__missiles[numero_missile]
                missile.setmort()
                if self.__nbvie==0:
                    self.fGame_over()
                    
           
            
         #gestion de la collision entre le missile et les blocks           
        for cle, blocks in self.__blocks.items():
            (mX,mY)=blocks.fGet()
            if mX-self.__largeur_blocks/2 <= posX_missile <= mX+self.__largeur_blocks/2 and mY-self.__largeur_blocks/2 <= posY_missile <= mY+self.__hauteur_blocks/2:
                b.append(cle)
                b.append(blocks)
                
        if len(b)!=0:
            del self.__blocks[b[0]]
            del self.__missiles[numero_missile]
            b[1].setmort()
            missile.setmort()
            
        #vérifie si le missile reste dans le canvas
        if posY_missile<=0 and posY_missile>=500:
                del self.__missiles[numero_missile]
                missile.setmort()
                
        #applique l'état gagner si il n'y a plus de mechant
        if self.__mechant=={}:
                    self.canvas.create_image(250,250,image=self.__image_win, tags='image_win')
                    self.game.configure(state='normal')
                    self.__nbvie=0
             


    def fScore(self):
        #Fonction qui ajoute des points à notre score
        self.__score.set(self.__score.get()+100000)

