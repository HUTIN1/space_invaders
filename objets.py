from Tkinter import

class cObjets:
    def __init_(self,largeurX,largeurY,tags,image,posX,posY,canvas):
        self.__largeurX=largeurX
        self.__largeurY=largeurY
        self.__tags=tags
        self.__posX=posX
        self.__posY=posY        
        self.__vitesse=vitesse
        self.__canevas=canevas
        self.__image=self.__canevas.create_image(self.__posX,self.__posY,image=image)



class cPerso(cObjets):
    def fBouger(self):
        touche=event.keysym

        if touche == 'q': #Déplacement de notre vaisseau à gauche
            self.__vitesse = -20
            self.__posX -= 20
            self.__canevas.move(self.__image,self.__vitesse,0)
  

        if touche == 'd': #Déplacement de notre vaisseau à gauche
            self.__vitesse = 20
            self.__posX += 20
            self.__canevas.move(self.__image,self.__vitesse,0)
  

        #Problème avec appel de cMissile (on veut créer plusieurs missiles).      
    def fTirer():
        tirer=cMissile()


class cMechant(cObjets):
    def __init__(self,cote):
        self.__cote=cote

    def fDeplacement_mechant(self):
        if self.__cote==1: #1=le méchant se déplace vers la droite
            self.__vitesse = 20
            self.__posX += 20           
            self.__canevas.move(self.__image,self.__vitesse,0)

        elif self.__cote==0: #2=le méchant se déplace vers la gauche
            self.__vitesse =  -20      
            self.__posX -= 20
            self.__canevas.move(self.__image,self.__vitesse,0)


        elif self.__cote==2: #3=le méchant descend d'un étage
            self.__vitesse = 20
            self.__posY += 20
            self.__canevas.move(self.__image,0,self.__vitesse)



class cMissile(cObjets):
    def fDeplacement_missile(self):
        self._vitesse = -20
        self.__posY -= 20
        self.__canevas.move(self.__image,0,self.__vitesse)

        





