

class cObjets:
    def __init_(self,largeurX,largeurY,tags,image,posX,posY,canevas,fenetre):
        self.__fen=fenetre
        self.__largeurX=largeurX
        self.__largeurY=largeurY
        self.__tags=tags
        self.__posX=posX
        self.__posY=posY        
        self.__vitesse=20
        self.__canevas=canevas
        self.__image=self.__canevas.create_image(self.__posX,self.__posY,image=image)

    def fGet(self):
        return self.__posX,self.__posY


class cPerso(cObjets):
    def __init__(self,largeurX,largeurY,tags,image,posX,posY,canevas,fenetre):
        self.__nb_tire=0
        self.__fen=fenetre
        self.__largeurX=largeurX
        self.__largeurY=largeurY
        self.__tags=tags
        self.__posX=posX
        self.__posY=posY        
        self.__vitesse=20
        self.__canevas=canevas
        self.__image=self.__canevas.create_image(self.__posX,self.__posY,image=image)
        fenetre.bind('<Button-1>',self.fTirer)
        fenetre.bind('q',self.fBougerGauche)
        fenetre.bind('d',self.fBougerDroite)

    def fBougerGauche(self,event):
        #Déplacement de notre vaisseau à gauche
        if self.__posX>=30:
            self.__vitesse = -20
            self.__posX -= 20
            self.__canevas.move(self.__image,self.__vitesse,0)

    def fBougerDroite(self,event):
        #Déplacement de notre vaisseau à droite
        if self.__posX<=470:
            self.__vitesse = 20
            self.__posX += 20
            self.__canevas.move(self.__image,self.__vitesse,0)

        #Problème avec appel de cMissile (on veut créer plusieurs missiles).      
    def fTirer(self,event):
            self.__fen.settirer(self.__nb_tire,self.__posX,self.__posY)
            self.__nb_tire+=1

        


class cMechant(cObjets):
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
        self.__image=self.__canevas.create_image(self.__posX,self.__posY,image=image)
        self.__fen.after(1000,self.fDeplacement_mechant)

    def fDeplacement_mechant(self):
        if self.__cote==1: #1=le méchant se déplace vers la droite
            self.__vitesse = 20
            self.__posX += 20         
            self.__canevas.move(self.__image,self.__vitesse,0)

        elif self.__cote==2: #2=le méchant se déplace vers la gauche
            self.__vitesse =  -20      
            self.__posX -= 20
            self.__canevas.move(self.__image,self.__vitesse,0)

        self.__fen.after(1000,self.fDeplacement_mechant)



class cMissile(cObjets):
    def __init__(self,largeurX,largeurY,tags,image,posX,posY,canevas,fenetre):
        self.__fen=fenetre
        self.__largeurX=largeurX
        self.__largeurY=largeurY
        self.__tags=tags
        self.__posX=posX
        self.__posY=posY        
        self.__vitesse=20
        self.__canevas=canevas
        self.__image=self.__canevas.create_image(self.__posX,self.__posY,image=image)
        fenetre.after(1000,self.fDeplacement_missile)
        
    def fDeplacement_missile(self):
        self.__vitesse = -20
        self.__posY -= 20
        self.__canevas.move(self.__image,0,self.__vitesse)
        self.__fen.after(1000,self.fDeplacement_missile)




