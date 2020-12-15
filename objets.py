

class cObjets:
    def __init_(self,largeurX,largeurY,tags,image,posX,posY,canevas):
        self.__largeurX=largeurX
        self.__largeurY=largeurY
        self.__tags=tags
        self.__image=image
        self.__posX=posX
        self.__posY=posY
        self.__canevas=canevas




class cPerso(cObjets):
    def fBouger(self):
        touche=event.keysym

        if touche == 'q': #Déplacement de notre vaisseau à gauche
            self.posX -= 20

        if touche == 'd': #Déplacement de notre vaisseau à gauche
            self.posX += 20

        #Problème avec appel de cMissile (on veut créer plusieurs missiles).      
    def fTirer():
        tirer=cMissile()


class cMechant(cObjets):
    def __init__(self,cote):
        self.__cote=cote


    def fDeplacement_mechant():
        if cote==1: #1=le méchant se déplace vers la droite
            self.posX=self.posX+20
        elif cote==0: #2=le méchant se déplace vers la gauche
            self.posX==self.posX-20
        elif cote==2: #3=le méchant descend d'un étage
            self.posY==self.posY+20

        





class cMissile(cObjets):
    def __init_(self):
        self.fIm()
    
    def fDeplacement_missile(self):
        self.posY=self.posY-20

#Im= Image missile
    def fIm(self):
        canevas.create_image(self.posX,self.posY)
        




