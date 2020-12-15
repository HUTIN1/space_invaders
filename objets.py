from Tkinter import

class cObjets:
    def __init_(self,largeurX,largeurY,tags,image,posX,posY,canvas):
        self.largeurX=largeurX
        self.largeurY=largeurY
        self.tags=tags
        self.image=image
        self.posX=posX
        self.posY=posY
        self.canevas=canevas




class cPerso(cObjets):
    def fBouger(self):
        touche=event.keysym

        if touche == 'q':
            PosX -= 20

        if touche == 'd':
            PosX += 20
    
    def fTirer(self):



class cMechant(cObjets):

class cMissile(cObjets):
    def fDeplacement(self):
        posY=posY-20
        




