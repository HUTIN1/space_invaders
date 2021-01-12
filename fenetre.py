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



from objets import cPerso, cMechant, cMissile, cBlocks

from tkinter import Tk, Canvas, Button, Label, IntVar



class fenetre(Tk):
    #Initialisation de la fenêtre
    def __init__(self,largeur_x_mechant,largeur_y_mechant,largeur_x_missile,largeur_y_missile,
                 largeur_x_perso,largeur_y_perso,freq_missile,freq_mechant,
                 pas_mechant,pas_missile,pas_perso,proba_missile_mechant,nb_mechant,
                 nb_ligne_mechant,largeur_blocks,hauteur_blocks,nbgrosblocks,nbligneblocks,
                 nbcolonneblocks):
        Tk.__init__(self)
        #Initialisation méchant
        self.__mechant={} #Dictionnaire contenant tous les méchants
        self.__largeur_x_mechant=largeur_x_mechant #Hitxbox méchant
        self.__largeur_y_mechant=largeur_y_mechant
        self.__image_mechant=None
        self.__freq_mechant=freq_mechant #Fréquence à laquelle le méchant bouge (en ms)
        self.__nb_mechant=nb_mechant
        self.__nb_ligne_mechant=nb_ligne_mechant
        self.__proba_missile_mechant=proba_missile_mechant
        self.__pas_mechant=pas_mechant
         
        #Initialisation perso (=vaisseau)
        self.__missiles={} #Dictionnaire contenant tous les missiles
        self.__perso=None #Création de notre vaisseau
        self.__image_perso=None
        self.__largeur_x_perso=largeur_x_perso #Hitxbox vaisseau
        self.__largeur_y_perso=largeur_y_perso
        self.__nbvie=3
        self.__pas_perso=pas_perso

        #Initialisation missiles
        self.__image_missile=None
        self.__largeur_x_missile=largeur_x_missile #Hitbox missile
        self.__largeur_y_missile=largeur_y_missile
        self.__freq_missile=freq_missile #Fréquence à laquelle les missiles bougent (en ms)
        self.__pas_missile=pas_missile
        self.__nb_tire=0

        #Initialisation blocks (permettant au personnage de se protéger des missiles ennemis)
        self.__blocks={} #Dictionniaire contenant les blocks
        self.__largeur_blocks=largeur_blocks ; #Hitbox block
        self.__hauteur_blocks=hauteur_blocks
        self.__nbgrosblocks=nbgrosblocks #Nombre de "paquet" de blocks 
        self.__nbligneblocks=nbligneblocks #Nombre de blocks par "paquet"
        self.__nbcolonneblocks=nbcolonneblocks

        self.__image_gameover=None
        self.__image_coeur=None
        self.__image_win=None
        self.__score=IntVar()
        self.creer_widget()

    """Fonction permetttant de créer les widgets de la fenêtre. Le bouton 'Game' sert à lancer/relancer une partie,
     le bouton 'quitter' sert à quitter et le label permet de gérer le score"""

    def creer_widget(self):
        self.canvas=Canvas(self,width=500,height=500,bg="black")
        self.canvas.place(x=0,y=0)
        
        self.quitter=Button(self,text="quitter",command=self.destroy,activeforeground="red")
        self.quitter.place(x=550,y=300)
        
        self.game=Button(self,text="Game",command=self.start,activeforeground="red")
        self.game.place(x=550,y=200)

        self.__score.set(0)
        self.label_score=Label(self,textvariable=self.__score) 
        self.label_score.place(x=550,y=100)

        

    """Fonction permettant de définir les images et les attribuer à la classe
    Les variables 'mechant, perso, missile, gameover, coeur et win' sont les images .gif définies dans principal.py"""
    def setimage(self,mechant,perso,missile,gameover,coeur,win):
        self.__image_mechant=mechant
        self.__image_perso=perso
        self.__image_missile=missile
        self.__image_gameover=gameover
        self.__image_coeur=coeur
        self.__image_win=win
        #Le vaisseau est initialisé une seul fois et n'est jamais supprimé contrairement aux méchants,missiles et blocks.
        self.__perso=cPerso(self.__largeur_x_perso,self.__largeur_y_perso, 
                            self.__image_perso,400,450,self.canvas,self,self.__pas_perso) 

        self.__perso=cPerso(self.__largeur_x_perso,self.__largeur_y_perso,
                            self.__image_perso,400,450,self.canvas,self,self.__pas_perso)
        
    def setcoeur(self,event):
        self.__nbvie+=1
        poscoeur=20+(self.__nbvie-1)*40
        self.canvas.create_image(poscoeur,50,image=self.__image_coeur, tags='coeur'+str(self.__nbvie-1))
        
    def setvitessemissile(self,event):
        self.__freq_missile=int(self.__freq_missile//2)
        print(type(self.__freq_missile))

    """Fonction permettant de créer un missile et de l'ajouter au dictionnaire self.__missiles.
    Les variables posx et posy donnent la position au missile crée et camp permet de définir si le missile provient d'un méchant ou du vaisseau"""
    def settirer(self,posx,posy,camp):
        pas=self.__pas_missile
        if camp=="perso":
            pas=-pas
        self.__missiles[self.__nb_tire]=cMissile(self.__largeur_x_missile,self.__largeur_y_missile,
                      self.__image_missile,posx,posy,self.canvas,self,self.__nb_tire,camp,pas,self.__freq_missile)
        self.__nb_tire+=1
    
        
    """Fonction permettant de lancer/relancer le jeu lorsqu'on appuie sur le bouton "game", il reinitialise puis crée les méchants et les 
    vies de notre vaisseau. Il permet aussi d'enlever l'affichage de Victoire/Défaite et de reinitialiser le score """
    def start(self):
        self.__mechant={}
        self.after(self.__freq_mechant,self.fAllmechant) #Permet de gérer le déplacement du "block" de méchant (lorsque tous les méchants change de ligne par exemple)
        X=100 #Position du premier méchant de la premier ligne
        Y=100
        a=0
        b=self.__nb_mechant//self.__nb_ligne_mechant
        if self.__nb_mechant%self.__nb_ligne_mechant >= 1: #Ces boucles 'for' permettent de créer les méchants en fonction du nombre de ligne
            a=1                                            # et du nombre de méchants définis dans principal.py
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
        poscoeur=10

        for i in range (self.__nbvie): #Cette boucle permet de supprimer les images de nos vies en fonction du nombre de vie
            poscoeur=poscoeur+40
            self.canvas.create_image(poscoeur,50,image=self.__image_coeur, tags='coeur'+str(i))
        poscoeur=20
        for i in range (self.__nbvie):
            self.canvas.create_image(poscoeur,50,image=self.__image_coeur, tags='coeur'+str(i))
            poscoeur=poscoeur+40
        self.game.configure(state='disabled') 

        self.game.configure(state='disabled') #Désactive le bouton game une fois que la partie est lancée

        #Cette boucle permet de générer les blocks en fonction des paramètres de principal.py
        for i in range(self.__nbgrosblocks):
            xi=i*self.__largeur_blocks*2*self.__nbcolonneblocks
            y=350
            for j in range(i*self.__nbligneblocks,i*self.__nbligneblocks+self.__nbligneblocks):
                x=xi
                y+=self.__hauteur_blocks
                for k in range(j*self.__nbcolonneblocks,j*self.__nbcolonneblocks+self.__nbcolonneblocks):
                    x+=self.__largeur_blocks
                    self.__blocks[k]=cBlocks(x,y,self.canvas,self.__largeur_blocks,self.__hauteur_blocks,k)
                    


    
        
        
    """Fonction permettant de gérer le déplacement du "block" de méchants en particulier lorsque le groupe de méchant doit changer de direction"""
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
        if self.__nbvie!=0: 
            self.after(self.__freq_mechant,self.fAllmechant) #Permet à la fonction de s'appeler elle même pour faire bouger les méchants si on a encore des vies
            self.fVaisseau_touche()
            
            

    """Fonction permettant de finir la partie en cas de défaite en affichant GameOver, réactive le bouton 'game' pour pouvoir rejouer
     et supprime les méchants restant"""
    def fGame_over (self):
            self.game.configure(state='normal')
            for cle in self.__mechant.keys():
                self.__mechant[cle].setmort()
            self.canvas.create_image(250,250,image=self.__image_gameover, tags='image_gameover')

    """Fonction permettant de savoir lorsque le vaisseau est touché par un méchant (et non pas par des missiles méchants)
    et d'appeler fGame_Over """
    def fVaisseau_touche(self):
        vX,vY=self.__perso.fGet()
        a=0
        for mechant in self.__mechant.values():
            mX,mY=mechant.fGet()
            if  vY<=mY:
                a=1
        if a==1:
            self.fGame_over()
                


    def fCollision(self,posX_missile,posY_missile,numero_missile,missile,camp):
        l=[]
        b=[]
        if camp=="perso":
            for cle, mechant in self.__mechant.items():
                (mX,mY)=mechant.fGet()
                if mX-self.__largeur_x_mechant/2 <= posX_missile <= mX+self.__largeur_x_mechant/2 and mY-self.__largeur_y_mechant/2 <= posY_missile <= mY+self.__largeur_y_mechant/2:
                    l.append(cle)
                    l.append(mechant)
            if len(l)!=0:
                del self.__mechant[l[0]]
                del self.__missiles[numero_missile]
                l[1].setmort()
                missile.setmort()
                self.fScore()
        elif camp=="mechant":
            mX,mY=self.__perso.fGet()
            if mX-self.__largeur_x_perso/2 <= posX_missile <= mX+self.__largeur_x_perso/2 and mY-self.__largeur_y_perso/2 <= posY_missile <= mY+self.__largeur_y_perso/2:
                self.canvas.delete("coeur"+str(self.__nbvie-1))
                self.__nbvie=self.__nbvie-1
                del self.__missiles[numero_missile]
                missile.setmort()
                if self.__nbvie==0:
                    self.fGame_over()
                    
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
            
                
        if posY_missile<=0 and posY_missile>=500:
                del self.__missiles[numero_missile]
                missile.setmort()

        if self.__mechant=={}:#Permet d'afficher l'image de victoire de réactiver le bouton 'game'
                    self.canvas.create_image(250,250,image=self.__image_win, tags='image_win')
                    self.game.configure(state='normal')
                    self.__nbvie=0
             
    """Fonction permettant d'ajouter 100 000 points à notre score après avoir tué un ennemi"""
    def fScore(self):
        self.__score.set(self.__score.get()+100000)

