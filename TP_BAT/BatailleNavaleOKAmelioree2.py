## Jeu Bataille Navale
## version 6 : LE JOUEUR CHOISIT LE PLACEMENT DES SES BATEAUX
## bateaux  verticaux ET horizontaux
## test fin du jeu + image bravo ou gameover
## adaptabilité de la fenetre ET de la grille


from Tkinter import *
from random import *

fen=Tk()

BatOrdi={"b1":[1],"b2":[2,2],"b3":[3,3,3],"b4":[4,4,4,4],"b5":[5,5,5,5,5]}
BatJoueur={"b1":[1],"b2":[2,2],"b3":[3,3,3],"b4":[4,4,4,4],"b5":[5,5,5,5,5]}

couleur={"b1":"blue","b2":"yellow","b3":"pink","b4":"green","b5":"black"}

c=40  ## taille de chaque case (par defaut)
Nmoi=5 ## nombre de bateaux au depart
Nordi=5 ## nombre de bateaux au depart


def creermat():    
    mat1=[]
    for i in range(10):
        col = []
        for j in range(10):
            col.append(0)
        mat1.append(col)
    ## ma matrice
    mat2=[]
    for i in range(10):
        col = []
        for j in range(10):
            col.append(0)
        mat2.append(col)
    ## la matrice de l'ordi
    return mat1 , mat2

mat1,mat2=creermat() ## les deux matrices sont créées pour sauvegarder la position des bateaux

def commencer():

    global mat1
    global mat2
    global c
    
    ## c= taille des cases. si l'on agrandit la fenetre, la taille change
    c= (min (can1.winfo_width(),can1.winfo_height())) /10

    Bcom.configure(text="Recommencer ?",command=commencer)
    Eport.delete("0",END)
    Ecrois.delete("0",END)
    Econtr.delete("0",END)
    Etorp.delete("0",END)
    Esous.delete("0",END)
    Lreste1.configure(text="vous avez 5 navires")
    Lreste2.configure(text="5 navires a couler")


## les deux grilles apparaissent sur les deux canvas
## can1 est le canvas du joueur
## can2 est le canvas de l'ordi

## pour le joueur : on trace seulement la grille 
    can1.delete(ALL)
    ## trace la grille
    for i in range(11):
        can1.create_line(c*i, 0,c*i,10*c)
        can1.create_line(0, c*i,10*c ,c*i)
    ## réinitialisation de ma matrice : 
    mat1=[]
    for i in range(10):
        col = []
        for j in range(10):
            col.append(0)
        mat1.append(col)

#### placement des bateaux aléatoire
############################################# pour l'ordi
        
    cpt2=0
    while cpt2 != 55:
        can2.delete(ALL)
        ## trace la grille
        for i in range(11):
            can2.create_line(c*i, 0,c*i,10*c)
            can2.create_line(0, c*i,10*c ,c*i)

        ## réinitialisation de ma matrice : 
        mat2=[]
        for i in range(10):
            col = []
            for j in range(10):
                col.append(0)
            mat2.append(col)
            
        ## placement des bateaux
        for cle in BatOrdi:
            coul=couleur[cle]
            if (len(BatOrdi[cle]))%2==0:
                i=randint(0,9)
                j=randint(0,9-(len(BatOrdi[cle])))
                for k in range (len(BatOrdi[cle])):
                    ##can2.create_rectangle(c*i,c*(j+k),c*(i+1),c*(j+1+k),fill=coul)
                    ###### décommenter la ligne du dessus pour visualiser les reponses 
                    mat2[i][j+k]=BatOrdi[cle][0]
                ## les bateux de longueur 2 et 4 sont verticaux
            else:
                i=randint(0,9-(len(BatOrdi[cle])))
                j=randint(0,9)
                for k in range (len(BatOrdi[cle])):
                    ##can2.create_rectangle(c*(i+k),c*j,c*(i+1+k),c*(j+1),fill=coul)
                    ###### décommenter la ligne du dessus pour visualiser les reponses
                    mat2[i+k][j]=BatOrdi[cle][0]
                ## les bateux de longueur 3 et 5 sont horizontaux
                
        ## test pour sortir du While
        ## on somme les nombres qui sont dans la matrice et on veux que cpt==55
        ## car 55 = 5*5+4*4+3*3+2*2+1
        ## si le cpt != 55 les bateaux sont superposés
        for el in mat2:
            cpt2+=sum(el)
        if cpt2!=55:
            cpt2=0
            
    

def correspond(x,y):
    return [x/c,y/c] ## donne les coordonnées du clic


###############  le fonction utilisé lors du jeu ##########################

def jeu(event):
    global mat1
    global mat2
    global Nmoi
    global Nordi

    [i,j]=correspond(event.x,event.y)
#### le joueur joue en cliquant sur le canvas 2 (celui de l'ordi)
    if mat2[i][j]==0: ## s'il n'y a pas de bateaux a l'endroit du clic
        can2.create_oval(c*i,c*j,c+c*i,c+c*j) ## creer un cercle ## c'est a l'eau
    else : ## s'il y a un bateau a l'endroit du clic
        can2.create_line(c*i,c*j,c*(i+1),c*(j+1),fill="red")
        can2.create_line(c*(i+1),c*j,c*i,c*(j+1),fill="red") ## creer un croix ## c'est touché
        
    ## test le nombre de bateaux restant :
        nb=mat2[i][j]
        mat2[i][j]=0
        temp=True
        for ligne in mat2:
            temp=temp and nb not in ligne
        if temp: ## si on ne rencontre plus le nombre correspondant au bateau qui vient d'etre touché, c'est que le bateau est coulé (en entier)
            Nmoi-=1
            Lreste2.configure(text="il reste ne reste que "+str(Nmoi)+" bateaux a couler ")
    if Nmoi==0: ## test fin du jeu
        can2.delete(ALL)
        Lreste2.configure(text="")
        can2.create_image(210,200,image=monIm) ## image bravo
        ## réinitialisation du nombre de bateaux pour la partie d'apres.
        Nmoi=5
        Nordi=5
        
#### puis l'ordi joue
    i=randint(0,9)
    j=randint(0,9)
    if mat1[i][j]==0:
        can1.create_oval(c*i,c*j,c+c*i,c+c*j) ## creer un cercle si c'est a l'eau
    else :
        can1.create_line(c*i,c*j,c*(i+1),c*(j+1),fill="red")
        can1.create_line(c*(i+1),c*j,c*i,c*(j+1),fill="red") ## creer un croix si touché

        nbb=mat1[i][j]
        mat1[i][j]=0
        temp1=True
        for ligne in mat1:
            temp1=temp1 and nbb not in ligne
        if temp1:
            Nordi-=1
            Lreste1.configure(text="il ne vous reste que "+str(Nordi)+" navires")
    if Nordi==0:
        ## fin du jeu
        can1.delete(ALL)
        Lreste1.configure(text="")
        can1.create_image(200,200,image=gameover) ## image Game over
        Nordi=5
        Nmoi=5


## Fonction qui va permettre au joueur de placer ses bateaux comme il veut.
def placer():
    cpt=0
    ## on recupère les cases de depart pour chaque bateau
    cinq=Eport.get()
    quatre=Ecrois.get()
    trois=Econtr.get()
    deux=Etorp.get()
    un=Esous.get()
    
    place=[un,deux,trois,quatre,cinq] ## les 5 cases sont mises dans une liste
    nb=1 ## initialisation pour le parcours de la liste
    coul=couleur.values() ## liste de toutes les couleurs
    
    for bat in place:
        cl=coul[(nb)-1]
        for i in range(10):
            if bat[0]==(chr(65+i)): ## on regarde la lettre entrée par le joueur
                x=i ## et on la convertit en abscisse
        y=int(bat[1])-1 ## on convertit le chiffre entré par le joueur en ordonnée
        if int(bat[1])==1 and bat[2]==str(0): ## cas particulier : si le chiffre entré par le joueur est '10'
            y=9 
        if bat[-1]=='H': ## placement horizontal
            for k in range (nb):
                can1.create_rectangle(c*(x+k),c*y,c*(x+1+k),c*(y+1),fill=cl)
                mat1[x+k][y]=nb
        elif bat[-1]=='V': ## placement vertical
            for k in range (nb):
                can1.create_rectangle(c*x,c*(y+k),c*(x+1),c*(y+1+k),fill=cl)
                mat1[x][y+k]=nb
        nb+=1 ## pour parcourir les listes 'place' et 'coul'           


def quitter():
    fen.quit()
    fen.destroy()


############### Interface graphique ################################# 

## les Widgets

## les labels chiffre et lettre autour des deux grilles        
Lnb=[]
Llet=[]
Llet2=[]
for i in range(10):    
    Lnb+=[Label(fen,text=str(1+i),fg="blue",bg="grey")]
    Lnb[i].grid(row=2+i,column=10,sticky=NSEW)
    Llet+=[Label(fen,text=str(chr(65+i)),fg="blue",bg="grey")]
    Llet[i].grid(row=12,column=i,sticky=NSEW)
    Llet2+=[Label(fen,text=str(chr(65+i)),fg="blue",bg="grey")]
    Llet2[i].grid(row=12,column=11+i,sticky=NSEW)

## Label, bouton, canvas
Ltitre=Label(fen,text="Bataille Navale",fg="blue")
L1=Label(fen,text="*** Ma grille ***",fg="blue")
L2=Label(fen,text="*** Grille adversaire ***",fg="blue")
can1=Canvas(fen,height=400,width=400,bg="white")
can2=Canvas(fen,height=400,width=400,bg="white")
Bcom=Button(fen,text="Jouer",command=commencer)
BQ=Button(fen,text="quitter",command=quitter)
Lreste1=Label(fen,text="vous avez 5 navires",fg="blue")
Lreste2=Label(fen,text="5 navires a couler",fg="blue")

## les deux images 
monIm=PhotoImage(file="/users/lmass3/e21001703/Desktop/BAT/bravo.gif")
gameover=PhotoImage(file="/users/lmass3/e21001703/Desktop/BAT/gameover.gif")

## quand le joueur voudra placer ses bateaux :
Lplacer=Label(fen,text="Placez vos navires : (saisie en Majuscule)")
Lport=Label(fen,text="Porte Avions : prend 5 cases")
Eport=Entry(fen,width=5)
Lcrois=Label(fen,text="Croiseur : prend 4 cases")
Ecrois=Entry(fen,width=5)
Lcontr=Label(fen,text="Contre Torpilleurs : prend 3 cases")
Econtr=Entry(fen,width=5)
Ltorp=Label(fen,text="Torpilleurs : prend 2 cases")
Etorp=Entry(fen,width=5)
Lsous=Label(fen,text="Sous Marin : prend 1 case")
Esous=Entry(fen,width=5)
Bok=Button(fen,text="ok",command=placer)

Lindic0=Label(fen,text="Explication : ")
Lindic=Label(fen,text="Entrez la case choisit et 'H' ou 'V' pour Horizontal ou Vertical")
Lindic1=Label(fen,text="Exemple de saisie : 'A1H' : Le bateau sera a la")
Lindic2=Label(fen,text=" 1ere ligne, 1ere colonne et horzontal")

## Placement des widgets
Ltitre.grid(row=0,column=0,columnspan=21,sticky=EW)
L1.grid(row=1,column=0,columnspan=10,sticky=EW)
L2.grid(row=1,column=11,columnspan=10,sticky=EW)
can1.grid(row=2,column=0,rowspan=10,columnspan=10,sticky=NSEW)
can2.grid(row=2,column=11,rowspan=10,columnspan=10,sticky=NSEW)
Bcom.grid(row=14,column=10,sticky=EW)
BQ.grid(row=15,column=10,sticky=EW)
Lreste1.grid(row=14,column=1,columnspan=8)
Lreste2.grid(row=14,column=12,columnspan=8)

Lplacer.grid(row=15,column=1,columnspan=8)
Lport.grid(row=16,column=1,columnspan=8)
Eport.grid(row=16,column=10)
Lcrois.grid(row=17,column=1,columnspan=8)
Ecrois.grid(row=17,column=10)
Lcontr.grid(row=18,column=1,columnspan=8)
Econtr.grid(row=18,column=10)
Ltorp.grid(row=19,column=1,columnspan=8)
Etorp.grid(row=19,column=10)
Lsous.grid(row=20,column=1,columnspan=8)
Esous.grid(row=20,column=10)
Bok.grid(row=21,column=10)

Lindic0.grid(row=16,column=11,columnspan=10)
Lindic.grid(row=17,column=11,columnspan=10)
Lindic1.grid(row=18,column=11,columnspan=10)
Lindic2.grid(row=19,column=11,columnspan=10)

##  permet l'adaptabilité de la fenetre
for i in range (21):
    fen.grid_rowconfigure(i,weight=1)
for i in range (21):
    fen.grid_columnconfigure(i,weight=1)


## permet de detecter les clics du joueur
can2.bind("<Button-1>",jeu)


fen.mainloop()
