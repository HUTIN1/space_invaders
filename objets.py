"""
Created on Tue Dec 15 09:55:28 2020

@author: HUTIN Nathan, Tran Matthieu
"""
"""
fichier contenant les class cPerso, cMechant, cMissile, cBlocks
"""


#importation des fonctions random
from random import random, randint

class cPerso():
    """
    class de notre vaisseau
    """
    #Initialisation du perso (=vaisseau)
    def __init__(self,largeurX,largeurY,image,posX,posY,canevas,fenetre,pas):
        self.__fen=fenetre
        self.__largeurX=largeurX
        self.__largeurY=largeurY
        self.__posX=posX
        self.__posY=posY        
        self.__pas=pas
        self.__canevas=canevas
        self.__image=self.__canevas.create_image(self.__posX,self.__posY,image=image, tags="perso")
        fenetre.bind('<space>',self.fTirer)
        fenetre.bind('q',self.fBougerGauche)
        fenetre.bind('d',self.fBougerDroite)

    
    def fGet(self):
        """Fonction permettant de retourner la position du perso """
        return self.__posX,self.__posY

    
    def fBougerGauche(self,event):
        """Fonction permettant le déplacement de notre vaisseau à gauche """
        if self.__posX>=30:
            self.__posX -=self.__pas
            self.__canevas.move(self.__image,-self.__pas,0)

    
    def fBougerDroite(self,event):
        """Fonction permettant le déplacement de notre vaisseau à droite """
        if self.__posX<=470:
            self.__posX += self.__pas
            self.__canevas.move(self.__image,self.__pas,0)

      
    def fTirer(self,event):
            """Fonction permettant au vaisseu de tirer"""  
            self.__fen.settirer(self.__posX,self.__posY,"perso")



    

        


class cMechant():
    """
    class des mechants
    """
    #Initialisation du méchant
    def __init__(self,largeurX,largeurY,tags,image,posX,posY,canevas,fenetre,pas,freq,proba_missile):
        self.__cote=1 #Permet de gérer si le méchant bouge à gauche (coté=2) ou à droite (coté=1)
        self.__fen=fenetre
        self.__largeurX=largeurX
        self.__largeurY=largeurY
        self.__tags=tags
        self.__posX=posX
        self.__posY=posY        
        self.__vitesse=20
        self.__canevas=canevas
        self.__pas=pas
        self.__freq=freq
        self.__proba=proba_missile
        self.__vie="vie" #Permet de gérer si le méchant est en vie ou pas (donc son déplacement)
        self.__image=self.__canevas.create_image(self.__posX,self.__posY,image=image, tags="mechant"+tags)
        self.__fen.after(freq,self.fDeplacement_mechant)
        
    
    def fGet(self):
        """Fonction permettant de retourner les positions du méchant"""
        return (self.__posX,self.__posY)

    
    def setmort(self):
        """Fonction permettant de définir si le méchant est mort"""
        self.__vie="mort" 

    
    def fChangecote(self):
        """Fonction permettant de changer le "cote" qui est utilisé dans la fonction fDeplacement_mechant"""
        if self.__cote==1:
            self.__cote=2
        else:
            self.__cote=1

    
    def fChangeposY(self):
        """Fonction permettant de faire descendre les méchants sur l'écran (leur position sur l'axeY)"""
        self.__posY+=self.__pas
        self.__canevas.move(self.__image,0,self.__pas)



    def fDeplacement_mechant(self):
        """Fonction permettant de faire déplacer les méchants vers la droite/gauche en fonction du coté et les tirs des méchants (qui
        sont aléatoires)"""
        if self.__cote==1: #1=le méchant se déplace vers la droite
            self.__posX += self.__pas      
            self.__canevas.move(self.__image,self.__pas,0)

        elif self.__cote==2: #2=le méchant se déplace vers la gauche    
            self.__posX -= self.__pas
            self.__canevas.move(self.__image,-self.__pas,0)

        #Après chaque déplacement le méchant à 'proba_missile_méchant de tirer' (défini dans principal.py)
        if random()<self.__proba:
            self.__fen.settirer(self.__posX,self.__posY,"mechant")
        if self.__vie=="vie":
            self.__fen.after(self.__freq,self.fDeplacement_mechant)
        else:
            self.__canevas.delete("mechant"+self.__tags)



class cMissile():
    """class pour les missiles """
    #Initialisation du missile
    def __init__(self,largeurX,largeurY,image,posX,posY,canevas,fenetre,numero,camp,vitesse,freq):
        self.__fen=fenetre
        self.__largeurX=largeurX
        self.__largeurY=largeurY
        self.__posX=posX
        self.__posY=posY+vitesse   
        self.__numero=numero
        self.__vitesse=vitesse
        self.__canevas=canevas
        self.__freq=freq
        self.__vie="vie" #Permet de savoir si le missile et en vie ou mort
        self.__camp=camp
        self.__image=self.__canevas.create_image(self.__posX,self.__posY,image=image,tags="missile"+str(numero))
        fenetre.after(freq,self.fDeplacement_missile)
        
    
    def fGet(self):
        """Fonction permettant de retourner les positions du missile"""
        return (self.__posX, self.__posY)

    
    def setmort(self):
        """Fonction permettant de définir si le méchant est mort"""
        self.__vie="mort"

        
   
    def fDeplacement_missile(self):
        """Fonction permettant le déplacement du missile """
        self.__posY += self.__vitesse
        self.__canevas.move(self.__image,0,self.__vitesse)
        self.__fen.fCollision(self.__posX,self.__posY,self.__numero,self,self.__camp)
        if self.__vie=="vie":
            self.__fen.after(self.__freq,self.fDeplacement_missile)
        else:
            self.__canevas.delete("missile"+str(self.__numero))
            
            
            
            
            
    
class cBlocks():
    #Initialisation des blocks permettant se protéger
    def __init__(self,posX,posY,canevas,largeur,hauteur,numero):
        self.__posX=posX
        self.__posY=posY
        self.__canevas=canevas
        self.__numero=numero
        canevas.create_rectangle(posX-largeur/2,posY-hauteur/2,posX+largeur/2,posY+hauteur/2,fill=self.couleurandom(),tags="bloque"+str(numero))
    

    def couleurandom(self):
            """Fonction permettant de retourner une couleur aleatoire en hexadecimal"""
            couleur="#"
            l=["a","b","c","d","e","f","0","1","2","3","4","5","6","7","8","9"]
            for i in range(6):
                couleur=couleur+l[randint(0,len(l)-1)]
            return couleur
        
        
       
    def fGet(self):
            """Fonction permettant de retourner la position du block""" 
            return (self.__posX,self.__posY)
        
        
      
    def setmort(self):
            """Fonction permettant de supprimer l'image du block sur la fenetre"""  
            self.__canevas.delete("bloque"+str(self.__numero))