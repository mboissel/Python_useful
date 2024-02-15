## Jeu Bataille Navale OK !
## version 5 : tout aleatoire,
## bateaux  verticaux ET horizontaux
## test fin du jeu + image bravo ou gameover
## adaptabilité de la fenetre ET de la grille


from Tkinter import *
from random import *

fen=Tk()

BatOrdi={"b1":[1],"b2":[2,2],"b3":[3,3,3],"b4":[4,4,4,4],"b5":[5,5,5,5,5]}
BatJoueur={"b1":[1],"b2":[2,2],"b3":[3,3,3],"b4":[4,4,4,4],"b5":[5,5,5,5,5]}

c=40 ## taille de chaque case (par defaut)
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
    Lreste1.configure(text="vous avez 5 navires")
    Lreste2.configure(text="5 navires a couler")

## les deux grilles apparaissent sur les deux canvas
## can1 est le canvas du joueur
## can2 est le canvas de l'ordi

#### placement des bateaux aléatoire
############################################ pour le joueur

    cpt1=0
    while cpt1 != 55:
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
    
        ## placement des bateaux
        for cle in BatJoueur:
            if (len(BatJoueur[cle]))%2==0:
                i=randint(0,9)
                j=randint(0,9-(len(BatJoueur[cle])))
                for k in range (len(BatJoueur[cle])):
                    can1.create_rectangle(c*i,c*(j+k),c*(i+1),c*(j+1+k),fill="grey")
                    mat1[i][j+k]=BatJoueur[cle][0]
                ## les bateux de longueur 2 et 4 sont verticaux
            else:
                i=randint(0,9-(len(BatJoueur[cle])))
                j=randint(0,9)
                for k in range (len(BatJoueur[cle])):
                    can1.create_rectangle(c*(i+k),c*j,c*(i+1+k),c*(j+1),fill="grey")
                    mat1[i+k][j]=BatJoueur[cle][0]
                ## les bateux de longueur 3 et 5 sont horizontaux
                    
        ## test pour sortir du While
        ## on somme les nombres qui sont dans la matrice et on veux que cpt==55
        ## car 55 = 5*5+4*4+3*3+2*2+1
        ## si le cpt != 55 les bateaux sont superposés
        for el in mat1:
            cpt1+=sum(el)
        if cpt1!=55:
            cpt1=0

## Meme demarche de placement des bateaux
############################################## pour l'ordi
        
    cpt2=0
    while cpt2 != 55:
        can2.delete(ALL)
        for i in range(11):
            can2.create_line(c*i, 0,c*i,10*c)
            can2.create_line(0, c*i,10*c ,c*i)
        mat2=[]
        for i in range(10):
            col = []
            for j in range(10):
                col.append(0)
            mat2.append(col)
        for cle in BatOrdi:
            if (len(BatOrdi[cle]))%2==0:
                i=randint(0,9)
                j=randint(0,9-(len(BatOrdi[cle])))
                for k in range (len(BatOrdi[cle])):
                    ## can2.create_rectangle(c*i,c*(j+k),c*(i+1),c*(j+1+k),fill="grey") #### si on veut visualiser la reponse!!
                    mat2[i][j+k]=BatOrdi[cle][0]
            else:
                i=randint(0,9-(len(BatOrdi[cle])))
                j=randint(0,9)
                for k in range (len(BatOrdi[cle])):
                    ## can2.create_rectangle(c*(i+k),c*j,c*(i+1+k),c*(j+1),fill="grey") #### si on veut visualiser la reponse!!
                    mat2[i+k][j]=BatOrdi[cle][0]
        ##### test cpt 
        for el in mat2:
            cpt2+=sum(el)
        if cpt2!=55:
            cpt2=0
            

def correspond(x,y):
    return [x/c,y/c] ## donne les coordonnées du clic


###############  la fonction utilisé lors du jeu ##########################

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
        can2.create_line(c*i,c*j,c*(i+1),c*(j+1))
        can2.create_line(c*(i+1),c*j,c*i,c*(j+1)) ## creer un croix ## c'est touché
        
    ##  test le nombre de bateaux restant :
        nb=mat2[i][j]
        mat2[i][j]=0
        temp=True
        for ligne in mat2:
            temp=temp and nb not in ligne
        if temp: ## si on ne rencontre plus le nombre correspondant au bateau qui vient d'etre touché, c'est que le bateau est coulé (en entier)
            Nmoi-=1 
            Lreste2.configure(text="il reste ne reste que "+str(Nmoi)+" bateaux a couler ")
    ## test fin du jeu
    if Nmoi==0:
        can2.delete(ALL)
        Lreste2.configure(text="")
        can2.create_image(210,200,image=monIm) ## image bravo
        ## réinitialisation du nombre de bateaux pour la partie d'apres.
        Nmoi=5
        Nordi=5
        
#### puis l'ordi joue (avec les memes demarches)
    i=randint(0,9)
    j=randint(0,9)
    if mat1[i][j]==0:
        can1.create_oval(c*i,c*j,c+c*i,c+c*j) ## creer un cercle si c'est a l'eau
    else :
        can1.create_line(c*i,c*j,c*(i+1),c*(j+1))
        can1.create_line(c*(i+1),c*j,c*i,c*(j+1)) ## creer un croix si c'est touché

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


def quitter():
    fen.quit()
    fen.destroy()


################# Interface graphique ################################# 

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

## permet l'adaptabilité de la fenetre
for i in range (15):
    fen.grid_rowconfigure(i,weight=1)
for i in range (21):
    fen.grid_columnconfigure(i,weight=1)

## permet de detecter les clics du joueur sur le canvas
can2.bind("<Button-1>",jeu)


fen.mainloop()
