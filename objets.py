


class cPerso():
    #Initialisation du perso (=vaisseau)
    def __init__(self,largeurX,largeurY,image,posX,posY,canevas,fenetre):
        self.__fen=fenetre
        self.__largeurX=largeurX
        self.__largeurY=largeurY
        self.__posX=posX
        self.__posY=posY        
        self.__vitesse=20
        self.__canevas=canevas
        self.__image=self.__canevas.create_image(self.__posX,self.__posY,image=image, tags="perso")
        fenetre.bind('<Button-1>',self.fTirer)
        fenetre.bind('q',self.fBougerGauche)
        fenetre.bind('d',self.fBougerDroite)

       #Fonction permettant de retourner la position du perso 
    def fGet(self):
        return self.__posX,self.__posY

        #Fonction permettant le déplacement de notre vaisseau à gauche
    def fBougerGauche(self,event):
        if self.__posX>=30:
            self.__vitesse = -20
            self.__posX -= 20
            self.__canevas.move(self.__image,self.__vitesse,0)

        #Fonction permettant le déplacement de notre vaisseau à droite
    def fBougerDroite(self,event):
        if self.__posX<=470:
            self.__vitesse = 20
            self.__posX += 20
            self.__canevas.move(self.__image,self.__vitesse,0)

        #Problème avec appel de cMissile (on veut créer plusieurs missiles).      
    def fTirer(self,event):
            self.__fen.settirer(self.__posX,self.__posY,-10,"perso")

        


class cMechant():
    #Initialisation du méchant
    def __init__(self,largeurX,largeurY,tags,image,posX,posY,canevas,fenetre):
        self.__cote=1
        self.__fen=fenetre
        self.__largeurX=largeurX
        self.__largeurY=largeurY
        self.__tags=tags
        self.__posX=posX
        self.__posY=posY        
        self.__vitesse=20
        self.__canevas=canevas
        self.__vie="vie"
        self.__image=self.__canevas.create_image(self.__posX,self.__posY,image=image, tags="mechant"+tags)
        self.__fen.after(500,self.fDeplacement_mechant)
        
        #Fonction permettant de retourner les positions du méchant
    def fGet(self):
        return (self.__posX,self.__posY)
    
    def setmort(self):
        self.__vie="mort" 

        #Fonction permettant de changer le "cote" qui est utilisé dans la fonction fDeplacement_mechant
    def fChangecote(self):
        if self.__cote==1:
            self.__cote=2
        else:
            self.__cote=1

        #Fonction permettant de faire descendre les méchants sur l'écran
    def fChangeposY(self):
        self.__posY+=20
        self.__vitesse=20
        self.__canevas.move(self.__image,0,self.__vitesse)


        #Fonction permettant de faire déplacer les méchants vers la droite/gauche en fonction du coté (cf fChangecote)
    def fDeplacement_mechant(self):
        if self.__cote==1: #1=le méchant se déplace vers la droite
            self.__vitesse = 20
            self.__posX += 20         
            self.__canevas.move(self.__image,self.__vitesse,0)

        elif self.__cote==2: #2=le méchant se déplace vers la gauche
            self.__vitesse =  -20      
            self.__posX -= 20
            self.__canevas.move(self.__image,self.__vitesse,0)
            
        if self.__vie=="vie":
            self.__fen.after(500,self.fDeplacement_mechant)
        else:
            self.__canevas.delete("mechant"+self.__tags)
            print("del image mechant",self.__tags)



class cMissile():
    #Initialisation du missile
    def __init__(self,largeurX,largeurY,image,posX,posY,canevas,fenetre,numero,camp,vitesse):
        self.__fen=fenetre
        self.__largeurX=largeurX
        self.__largeurY=largeurY
        self.__posX=posX
        self.__posY=posY-20   
        self.__numero=numero
        self.__vitesse=20 
        self.__canevas=canevas
        self.__vitesse=vitesse
        self.__vie="vie"
        self.__camp=camp
        self.__image=self.__canevas.create_image(self.__posX,self.__posY,image=image,tags="missile"+str(numero))
        fenetre.after(100,self.fDeplacement_missile)
        
        #Fonction permettant de retourner les positions du missile
    def fGet(self):
        return (self.__posX, self.__posY)
    
    def setmort(self):
        self.__vie="mort"

        
        #Fonction permettant le déplacement du missile
    def fDeplacement_missile(self):
        self.__posY += self.__vitesse
        self.__canevas.move(self.__image,0,self.__vitesse)
        self.__fen.fCollision(self.__posX,self.__posY,self.__numero,self,self.__camp)
        if self.__vie=="vie":
            self.__fen.after(100,self.fDeplacement_missile)
        else:
            self.__canevas.delete("missile"+str(self.__numero))
        

        




