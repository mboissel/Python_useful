#### Compilation des cours de SAS - Licence et Master MASS - Univ Caen ####

################
##            ##
##   DEBUT    ##
## Licence L1 ##
##            ##
################

##########
## TP 1 ##
##########

# definition de 
# quelques constantes
pi= 3.14159
e= 2.71
mi= 1

# travail sur une chaine
# partir de l'indice 0 en Python.
ch= "python "
ch1="est une "
d=  ch[5] + ch[4] + ch[3] + ch[2] + ch[1] + ch[0]
e= ch [2:] + ch [0:2]
f= ch[-1]
g= ch1[:]
x= "informatique"
print ch + g +"langage "+x, "formidable"

# calculs de quelques termes d'une suite

x0= -2
x1= 4*x0 + 3
x2= 4*x1 + 3
x3= 4*x2 + 3
x4= 4*x3 + 3
x5= 4*x4 + 3
print "finalement on trouve x5=", x5

# autre suite  un+1= 20/un
x0= 6
x1= 20/x0 
x2= 20/x1

#dialogue
n=raw_input ("quel est votre pseudo?")
print "bonjour", n
a=input ("votre annee de naissance  ?")
print " ah vous avez ", 2010 - a, "ans"
print "au revoir"

## interaction "input" 
a=input("quel est votre age?")
b=raw_input ("etes vous un homme ou une femme ? Repondez par H ou F.")
if b=="H":
    if a>=20:
        print "vous payez un impot"
    else:
        print "vous ne payez pas d'impot"
else:
    if b=="F":
        if 18<a<35:
            print "vous payez un impot"
        else:
            print"vous ne payez pas d'impot"


##########
## TP 2 ##
##########

#1/
ch="bonjour a tous"
n=1
while n<=10:
	print n, ch
	n=n+1

#2/
a, somme = 25, 0
while a<=75:
        somme=somme+a**3
        a=a+1
print somme

#3/
n=1
while n<=100:
        if n%4==0 and n%7==0:
                print n,"(*)",
        elif n%7==0:
                print n,
        n=n+1

#4/
a=2
b=0
somme=0
while b<=63:
        somme=somme+a**b
        b=b+1
print somme

#5/
N=input("entrer un entier : ")
if N%3==0 and N%5==0:
        print N, "est divisible par 3 et 5"
elif N%3==0 and N%5!=0:
        print N, "est divisible par 3 mais pas par 5"
elif N%5==0 and N%3!=0:
        print N, "est divisible par 5 mais pas par 3"
else:
        print N, "n'est pas divisible ni par 3 ni par 5"

#2-Suites définies pas récurrence
#a/

u, p = 2, 1
a=input ("entrer un entier : ")
while p<=a:
        u=(7-u)**0.5
        p=p+1
print u

#b/
u0=input ("entrer un entier : ")
u=u0
n=0
while n<=10:
        if u%2!=0:
                u=3*u+1
                n=n+1
        else:
                u=0.5*u-1
                n=n+1
print u


## Compter les e.
ch="evertcverte"
cp, i = 0, 0
n=len(ch)
while i<n:
    x=ch[i]
    if x=="e":
        cp=cp+1
    i=i+1
print cp

##########
## TP 3 ##
##########

## Definition de fonction 

# y fahrenheit
# x degré

def CenF (x):
    y=(9./5.)*x+32
    return y

def FenC (y):
    x=(y-32)*(5./9.)
    return x

# 1.a. 380°F donne 193.3°C
#      37°7 C donne 100.039°F
#1.b.
def NBseconde (h, m, s):
    h=h*3600
    m=m*60
    sec=h+m+s
    return sec

def sec1 (h, m, s):
    if s<59:
        s=s+1
    elif s==59 and m!=59:
        m, s=m+1, 0
    elif s==59 and m==59 and h!=23:
        h, m, s=h+1, 0, 0
    else:
        h, m, s= 0, 0, 0
    print h, "h", m, "m et", s, "s"


def heuresuiv (h, m, s):
    s=s+1
    if s==60:
        s=0
        m=m+1
        if  m==60:
            m=0
            h=h+1
            if h==24:
                h=0
    w=str(h)+"h"+str(m)+"m"+str(s)+"s"
    return w


def ZetaS (n,s):
    somme=0
    p=1
    while p<=n:
        somme=somme+1./p**s
        p=p+1
    return somme

#3
def suite(n):
    u, i=-2, 0
    while i<n:
        u=(-5)*u+7
        i=i+1
    return u

#3.b.
def suiteb(n):
    u, p=2, 1
    while p<n:
        u=(u)**2/p
        p=p+1
    return u

#3.c
def suitec(n):
    u, p=-1, 1
    while p<n:
        u=u+(-1)**p/(2*p)
        p=p+1
    return u

#4 factorielle
def fact(n):
    res=n
    p=1
    if n!=0:
        while (n-p)!=0:
            res=res*(n-p)
            p=p+1
        return res
    else:
        return 1

#5 racine cubique de x donne y
#def calcul(x,y):


##########
## TP 4 ##
##########
#ex1: entier parfait

#1-
def sommeEntiers(l):
    i=0
    somme=0
    while i<len(l):
        somme=somme+l[i]
        i=i+1    
    return somme

#2-
def listeDiviseurs(n):
    x=1
    listediv=[]
    while x<=(n/2.):
        if n%x==0:
            listediv=listediv+[x]
        x=x+1
    return listediv

#3-
def entierParfait(n):
    i=0
    listediv=listeDiviseurs(n)
    add=sommeEntiers(listediv)
##    while i<len(listediv):
##        y=listediv[i]
##        add=add+y
##        i=i+1
    if add==n:
        return True
    return False

#4-
def listeEntiersParfaits(b):
    listeb=[]
    n=1
    while n<b:
        res=entierParfait(n)
        if res==True:
            listeb=listeb+[n]
        n=n+1
    return listeb
            
#ex2: Les ensembles
#a-
def appartient(element,ensemble):
    n=0
    x=element
    while n<len(ensemble):
        if x==ensemble[n]:
            return True
        n=n+1
    return False

#b-
def inclusion(ensemble1,ensemble2):
    i=0
    x=ensemble1[i]
    while i<len(ensemble1):
        res=appartient(x,ensemble2)
        if res==False:
            return False
        else:
            i=i+1
    return True
       
 
##########
## TP 5 ##
##########         

from turtle import *

def triangl1(d):
    for i in range(3):
        forward(d)
        left(120)
    forward(d)
##triangl1(100)
##triangl1(50)

def triangl2(d):
    for i in range (3):
        forward(d)
        right(120)
    forward(d)
##triangl2(100)

def carre1(d):
    for i in range(4):
        forward(d)
        left(90)
    forward(d)
##carre1(50)

##ligne de n carré étant de a coté
def lignedecarres(a,n):
    for i in range (n):
        carre1(a) 
        up()
        forward(a/4)
        down()
##lignedecarres(50,10)

def rayons(n,d):
    for i in range (n):
        forward(d)
        backward(d)
        right(360/n)
##rayons(18,50)


def polynome(a,n):
    for i in range(n):
        forward(a)
        right(360/n)
##polynome(50,8)


from random import *

## test de fonction random

l=[w for w in range (0,9)]
print "la liste ", l
shuffle (l)
print "la liste mélangé ", l
x=choice (l)
print "on choisis un entier de la seq :", x
print "on estrait une liste de l, on obtient l' :", sample(l,5)

##la liste  [0, 1, 2, 3, 4, 5, 6, 7, 8]
##la liste mélangé  [0, 1, 4, 2, 8, 7, 5, 3, 6]
##on choisis un entier de la seq : 2
##on estrait une liste de l, on obtient l' : [8, 3, 4, 1, 0]
##
##la liste  [0, 1, 2, 3, 4, 5, 6, 7, 8]
##la liste mélangé  [5, 0, 8, 7, 2, 4, 6, 3, 1]
##on choisis un entier de la seq : 5
##on estrait une liste de l, on obtient l' : [0, 4, 7, 3, 6]


#jeu du chiffre misterieux : fonctionnel ! =)
from random import *
def jouer():
    n=0
    c=0
    x=randint(0,101)
    while n!=-1:
        n, c=input ("entrer un entier ou -1 pour stopper : "), c+1
        if n==-1:
            print "il falait trouver", x
            fin=-1
        elif n<0 or n>100:
            print "on cherche un entier entre 1 et 100"
        elif n<x:
            print n, "est trop petit"
        elif n==x:
            print "bravo c'est gagné en", c, "coups"
            n=-1
        else:
            print n, "est trop grand"


##########
## TP 6 ##
##########  

def carre(x):
    return x*x

def applique(f,liste):
    Lres=[]
    for x in liste:
        Lres=Lres+[f(x)]
    return Lres

#print applique(carre,[3,5,9])

def som_applique(f,liste):
    l=applique(f,liste)
    som=0
    for i in range (len(l)):
        som=som+l[i]
    return som

#print som_applique(carre,[3,5,9])

from random import *
def pfc():
    a=input("vous voulez jouer jusqu'a quel score? (maxi 10)")
    score_ordi=0
    score_vous=0
    liste=["p","f","c"]
    ordi_gagne=[["p","f"],["c","p"], ["f","c"]]
    while score_ordi<a and score_vous<a:
        b=raw_input("que voulez-vous jouer? taper p pour pierre, f pour feuille, c pour ciseau, stop pour quitter : ")
        d=choice(liste)
        if b=="stop":
            return "abandon du joueur"
        elif b==d:
            print "match nul"
        elif [b,d] in ordi_gagne:
            score_ordi+=1
            score_vous-=1
            print "l'ordi joue", d
            print"les scores: ordi ", score_ordi, "vous", score_vous
        else:
            score_ordi-=1
            score_vous+=1
            print "l'ordi joue", d
            print"les scores: ordi ", score_ordi, "vous", score_vous
    return ("fin du jeu. Les scores sont : "+str(score_ordi)+" a "+str(score_vous))

##########
## TP 7 ## Tkinter
##########  

from Tkinter import*

#Definition des fonctions
def quitter():
    fen.quit()
    fen.destroy()

def effacer():
    #effacer un Entry
    EFrancs.delete("0",END)
    EEuros.delete("0",END)
    #efface Text
    TFrancs.delete("0.0",END)
    TEuros.delete("0.0",END)

def ConvEuros():
    f=EFrancs.get()
    euro=eval(f)/6.55957
    TEuros.insert(END,str(euro))
def ConvFrancs():
    f=EEuros.get()
    franc=eval(f)*6.55957
    TFrancs.insert(END,str(franc))


#définition la fen
fen=Tk()
#définir les widgets

LTitre=Label(fen,text="Converssion Francs Euros",font=("courrier","14","bold"))
EFrancs=Entry(fen)
EEuros=Entry(fen)
LFrancs1=Label(fen,text="Francs")
LFrancs2=Label(fen,text="Francs")
LEuros1=Label(fen,text="Euros")
LEuros2=Label(fen,text="Euros")
Legal1=Label(fen,text="=")
Legal2=Label(fen,text="=")
TFrancs=Text(fen,height=1,width=20)
TEuros=Text(fen,height=1,width=20)
Beff=Button(fen,text="Remise a zero",command=effacer)
BQ=Button(fen,text="Quitter",command=quitter)
BConvEuros=Button(fen,text="Conversion en Euros",command=ConvEuros)
BConvFrancs=Button(fen,text="Conversion en Francs",command=ConvFrancs)

LTitre.grid(row=0,column=0,columnspan=6)
EFrancs.grid(row=1,column=0)
LFrancs1.grid(row=1,column=1)
BConvEuros.grid(row=1,column=2)
Legal1.grid(row=1,column=3)
TEuros.grid(row=1,column=4)
LEuros1.grid(row=1,column=5)
EEuros.grid(row=2,column=0)
LEuros2.grid(row=2,column=1)
BConvFrancs.grid(row=2,column=2)
Legal2.grid(row=2,column=3)
TFrancs.grid(row=2,column=4)
LFrancs2.grid(row=2,column=5)
Beff.grid(row=3,column=0)
BQ.grid(row=3,column=5)

fen.mainloop()

## jeu des images avec TKinter

# -*- coding: utf-8 -*-
from Tkinter import *
from random import *

def quitter():
    fen.quit()
    fen.destroy()

def affiche():
    global numero
    Can.delete(ALL)
    numero=randint(0,2)
    c=Can.create_image(200,200,image=Lesphotos[numero])
    B1.grid(row=1,column=1)
    B2.grid(row=2,column=1)
    B3.grid(row=3,column=1)

def vrai():
    Tmsg.delete("0.0",END)
    Tmsg.grid(row=4,column=2)
    Tmsg.configure(bg="green")
    Tmsg.insert(END,"BRAVO")
    

def faux():
    Tmsg.delete("0.0",END)
    Tmsg.grid(row=4,column=2)
    Tmsg.configure(bg="red")
    Tmsg.insert(END,"NON")
    
def chat():
    if numero==0:
        vrai()
    else:
        faux()
def chien():
    if numero==1:
        vrai()
    else:
        faux()
def ane():
    if numero==2:
        vrai()
    else:
        faux()
        
fen=Tk()
numero=0
photo1=PhotoImage(file="chat.gif")
photo2=PhotoImage(file="chien.gif")
photo3=PhotoImage(file="ane.gif")
Lesphotos=[photo1,photo2,photo3]
photonom=["chat","chien","ane"]

Can=Canvas(fen,height=400,width=400,bg="grey")
BQuestion=Button(fen,text="question",command=affiche)
B1=Button(fen,text="chat",command=chat)
B2=Button(fen,text="chien",command=chien)
B3=Button(fen,text="ane",command=ane)
BQ=Button(fen,text="quitter",command=quitter)
Tmsg=Text(fen,height=1,width=10)
#position
BQuestion.grid(row=0,column=1)
Can.grid(row=1,column=0,rowspan=4)
BQ.grid(row=5,column=1)

fen.mainloop()


## convertisseur franc / euros, avec Tkinter

from Tkinter import*

#Definition des fonctions
def quitter():
    fen.quit()
    fen.destroy()

def effacer():
    #effacer un Entry
    EFrancs.delete("0",END)
    EEuros.delete("0",END)
    #efface Text
    TFrancs.delete("0.0",END)
    TEuros.delete("0.0",END)

def ConvEuros():
    f=EFrancs.get()
    euro=eval(f)/6.55957
    TEuros.insert(END,str(euro))
def ConvFrancs():
    f=EEuros.get()
    franc=eval(f)*6.55957
    TFrancs.insert(END,str(franc))


#définition la fen
fen=Tk()
#définir les widgets

LTitre=Label(fen,text="Converssion Francs Euros",font=("courrier","14","bold"))
EFrancs=Entry(fen)
EEuros=Entry(fen)
LFrancs1=Label(fen,text="Francs")
LFrancs2=Label(fen,text="Francs")
LEuros1=Label(fen,text="Euros")
LEuros2=Label(fen,text="Euros")
Legal1=Label(fen,text="=")
Legal2=Label(fen,text="=")
TFrancs=Text(fen,height=1,width=20)
TEuros=Text(fen,height=1,width=20)
Beff=Button(fen,text="Remise a zero",command=effacer)
BQ=Button(fen,text="Quitter",command=quitter)
BConvEuros=Button(fen,text="Conversion en Euros",command=ConvEuros)
BConvFrancs=Button(fen,text="Conversion en Francs",command=ConvFrancs)
#defini la grille 
LTitre.grid(row=0,column=0,columnspan=6)
EFrancs.grid(row=1,column=0)
LFrancs1.grid(row=1,column=1)
BConvEuros.grid(row=1,column=2)
Legal1.grid(row=1,column=3)
TEuros.grid(row=1,column=4)
LEuros1.grid(row=1,column=5)
EEuros.grid(row=2,column=0)
LEuros2.grid(row=2,column=1)
BConvFrancs.grid(row=2,column=2)
Legal2.grid(row=2,column=3)
TFrancs.grid(row=2,column=4)
LFrancs2.grid(row=2,column=5)
Beff.grid(row=3,column=0)
BQ.grid(row=3,column=5)

fen.mainloop()


##########
## TP 8 ##
##########  

##a.1
from Tkinter import *
from random import *

def initTas (k):
    Lres=[k]
    Lres=[k]+[0]*(k-1)
    return Lres

##a.2
def falaise(tas):
    Lres=[]
    for i in range(len(tas)-1):
        if tas[i]>=tas[i+1]+2:
            Lres=Lres+[i]
    return Lres

##a.3
def etape(tas):
    Listefalaise=falaise(tas)
    if Listefalaise==[]:
        return False
    else:
        i=choice(Listefalaise)
        tas[i]=tas[i]-1
        tas[i+1]=tas[i+1]+1
        return True

##b.   
##tas=[15,3,12,6,14,14,8,9,6,11,8,1,12,9,7]

def grille():
    for i in range(nb+1):
        can.create_line(x0+c*i, y0,x0+c*i,y0 + nb*c)
        can.create_line(x0, y0+c*i,x0+nb*c ,y0+c*i)

nb= 15 # nombre de cases par ligne (grille carree)
c=40 # dimension d'une case supposée carrée
x0,y0=30,600 #coordonnées du point en haut à gauche

def New():
    global tas
    Can.delete(ALL)
    tas=[randint(1,15) for i in range(15)]
    Dessine(tas)
    
def unEtape():
    Can.delete(ALL)
    etape(tas)
    Dessine(tas)


def Simu():
    while etape(tas):
        Can.delete(ALL)
        Dessine(tas)
        Can.after(500)
        Can.update()

def Quitter():
    fen.quit()
    fen.destroy()

def DessineGrain(i,j):
    Can.create_rectangle(x0+c*i, y0-c*(j+1),x0+c*(i+1),y0-c*j,fill="Yellow")

def DessineCol(i,ci): ##i=numéro colonne, ci=nombre de grains
    for j in range(ci):
        DessineGrain(i,j)

def Dessine(tas): ##Dessine toutes les colonnes
    for i in range(len (tas)):
        DessineCol(i,tas[i])
    
 
fen=Tk()
Can=Canvas(fen, height=700, width=700, bg="Green")
BN=Button(fen, text="Nouvelle Partie",command=New)
BEtape=Button(fen, text="Etape",command=unEtape)
BSimu=Button(fen, text="Sumilation",command=Simu)
BQuit=Button(fen, text="Quitter",command=Quitter)

Can.grid(row=0,column=0,rowspan=5)
BN.grid(row=0,column=1)
BEtape.grid(row=1,column=1)
BSimu.grid(row=2,column=1)
BQuit.grid(row=4,column=1)


fen.mainloop()

## code fruits 
##TP8 ajac

from Tkinter import *
from random import *

mot="ABRICOT"
grillemot=[['Y', 'G', 'N', 'T', 'R', 'A', 'K', 'Q'], ['E', 'V', 'K', 'A', 'F', 'A', 'L', 'Q'], ['B', 'I', 'S', 'U', 'E', 'R',
'X', 'E'], ['R', 'Z', 'E', 'O', 'A', 'B', 'Z', 'O'], ['P', 'K', 'L', 'W', 'X', 'L', 'Y', 'Y'], ['H', 'W', 'L', 'V', 'T', 'O',
'W', 'G'], ['B', 'I', 'O', 'R', 'Z', 'X', 'Q', 'C'], ['K', 'L', 'Y', 'J', 'B', 'T', 'N', 'O']]
alpha=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
listemot=["ABRICOT","POMME","POIRE","ORANGE","CERISE","FRAISE","FRAMBOISE","KIWI","KUMQUAT","MYRTILLE","ANANAS"]

nb= 8 # nombre de cases par ligne (grille carree)
c=30 # dimension d'une case supposée carrée
x0,y0=30,600 #coordonnées du point en haut à gauche


def Jouer():
    Tmot.delete("0", END)
    Treponse.delete("0.0", END)
    global mot
    mot=choice(listemot)
    Tmot.delete("0.0",END)
    Tmot.insert(END, mot)
    grille() ##affiche la grille...

def correspond (x,y):
    return (y-y0)/c,(x-x0)/c


def ecrire(event):
    pos=correspond(event.x,event.y)
    i,j=pos[0],pos[1]
    if i in range (nb) and j in range (nb):
        Tmot.insert(END,grillemot[i][j])
    

def Valider ():
    print "valider"

def Quitter ():
    fen.quit()
    fen.destroy()

def grille():
    for i in range(nb+1):
        can.create_line(x0+c*i, y0,x0+c*i,y0 + nb*c)
        can.create_line(x0, y0+c*i,x0+nb*c ,y0+c*i)


fen=Tk()
Can=Canvas(fen, height=700, width=700, bg="white")

BJouer=Button(fen, text="Jouer",command=Jouer)
Lconsigne=Label(fen, text="Reconstitue ce mot")
TLemot=Text(fen,width=15, height=1)
Lmot=Label(fen, text="ton mot")
Emot=Entry(fen)
BValider=Button(fen, text="Valider", command=Valider)
Treponse=Text(fen,width=15, height=1)
BQuitter=Button(fen, text="Quitter", command=Quitter)


Can.grid(row=0,column=0,rowspan=8)
BJouer.grid(row=0,column=1)
Lconsigne.grid(row=1,column=1)
Tmot.grid(row=2,column=1)
Lmot.grid(row=3,column=1)
Emot.grid(row=4,column=1)
BValider.grid(row=5,column=1)
Treponse.grid(row=6,column=1)
BQuitter.grid(row=7,column=1)

Can.bind ("<Button-1>", ecrire)

fen.mainloop()


##########
## TP 9 ##
########## 

## ex 1 .
## 1.a
d={'lea': (2, 45, 176, 89), 'louise': (2, 45, 156, 78), 'pierre': (1, 32,
187, 67), 'luc': (1, 45, 176, 87), 'anne': (2, 55, 155, 45), 'marie': (2,
67, 167, 56), 'lise': (2, 34, 178, 57)}

def age (d,prenom):
    if d.has_key(prenom):
        return d[prenom][1]
    else:
        return 0

##1.b
def plus_taille(d,nb):
    cp=0
    for x in d.keys():
        if d[x][2]>nb:
            cp+=1
    return cp


##2.Moyenne
def moyenne_taille(d):
    somm=0
    for x in d.keys():
        somm+=d[x][2]
    return somm/float(len(d))

##3. la plus grande du dico
def leplusgrand(d):
    T=0
    l=()
    for x in d.keys():
        if d[x][2]>T:
            l=(x,d[x][2])
            T=d[x][2]
    return l


##4.a Probleme de poinds : IMC = poids/taille²
def test_poids(t):
    v,w,x,y=t
    IMC=float(y)/(float(x)/100.)**2
    if IMC>25:
        return True
    else:
        return False

##4.b
def nb_surpoids(d):
    cp=0
    for p in d.keys():
        if test_poids(d[p])==True:
            cp+=1
    return cp


##4.c
def qui_surpoids(d):
    Lres=[]
    for p in d.keys():
        if test_poids(d[p])==True:
            Lres+=[p]
    return Lres

## ex 2 : dico FRC / ANG
from random import *
from Tkinter import *

#definition du dictionnaire
mois={"janvier":"January","février":"February","mars":"March","avril":"April","mai":"May","juin":"June","juillet":"July","aout":"August","septembre":"September","octobre":"October","novembre":"November","decembre":"December"}
jour={"lundi":"Monday","mardi":"Tuesday","mercredi":"Wednesday","jeudi":"Thursday","Vendredi":"Friday","samedi":"Saturday","dimanche":"Sunday"}
question={"où":"where","quand":"when","comment":"how much","combien":"how many"}
temps={"temps":"weather","chaud":"warm","nuageux":"cloudy","venté":"windy","pluvieux":"raining","ensoleillé":"sunny","très chaud":"hot","neige":"snow","pluie":"rain","nuage":"cloud","soleil":"sun","vent":"wind","glace":"ice"}
element={"neige":"snow","pluie":"rain","nuage":"cloud","soleil":"sun","vent":"wind","glace":"ice","arc-en-ciel":"rainbow","ciel":"sky"}
saison={"été":"summer","automne":"autumn","hiver":"winter","printemps":"spring"}
adjectif={"facile":"easy","difficile":"difficult","vrai":"true","faux":"false","debut":"start","fin":"end"}
maison={"chateau":"castle","niche":"kennel","cabane en bois":"log cabin","habiter":"live","sombre":"dark","habits":"clothes","école":"school","maison":"house","dehors":"outside","parler":"speak","regarder":"whatch"}
action={"skier":"ski","nager":"swim","marcher":"walk","jouer au tennis":"play tennis","renifler":"sniff","tousser":"cough","vouloir":"want"}
noel={"noel":"christmas","carte postal":"postcard","dinde":"turkey","repas":"dinner","arbre":"tree","cadeau":"present","chaussure":"shoe"}
direction={"droite":"right","gauche":"left","haut":"up","bas":"down"}

dic={}
dic.update(mois)
dic.update(jour)
dic.update(saison)
dic.update(element)
dic.update(temps)
dic.update(question)
dic.update(adjectif)
dic.update(maison)
dic.update(action)
dic.update(noel)
dic.update(direction)


##les fonctions:
def quitter():
    fen.quit()
    fen.destroy()

def effacer():
    #efface Entry
    EMot.delete("0",END)
    #efface Text
    TNbp.delete("0.0",END)
    TNbq.delete("0",END)

def New():
    print "rien"

    
##la fenetre...

fen=Tk()

LTitre=Label(fen,text="Apprentissage de vocabulaire anglais",font=("courrier","14","bold"))
LNbq=Label(fen,text="Nombre de Questions")
LNbp=Label(fen,text="Nombre de points")
TNbq=Text(fen,height=1,width=20)
TNbp=Text(fen,height=1,width=20)
EMot=Entry(fen)

BNew=Button(fen,text="nouvelle question",command=New)
BQ=Button(fen,text="Quitter",command=quitter)
BZero=Button(fen,text="Remise a zero",command=effacer)


LTitre.grid(row=0,column=0,columnspan=3)
LNbq.grid(row=1,column=1)
LNbp.grid(row=2,column=1)
TNbq.grid(row=1,column=2)
TNbp.grid(row=2,column=2)
EMot.grid(row=3,column=0)

BNew.grid(row=4,column=2)
BQ.grid(row=5,column=2)
BZero.grid(row=6,column=2)

fen.mainloop()

###########
## TP 10 ##
###########

## TD 10 : les fichiers et dico

## Premiere partie
##1/
def buts (fic):
    L=open(fic,"r")
    c=0
    for ligne in L:
        L1=ligne.split()
        c=c+int(L1[-2])+int(L1[-1])
    return c
          
## 2/
def matchnul (fic):
    L=open(fic,"r")
    c=0
    for ligne in L:
        L1=ligne.split()
        if L1[-2]==L1[-1]:
            c+=1
    return c

## 3/ a/
def monequipe (equipe,fic):
    L=open(fic,"r")
    for ligne in L:
        L1=ligne.split()
        if equipe==L1[0] or equipe==L1[1]:
            return ligne
        
## 3/ b/
lesjournees=["J1.txt","J2.txt","J3.txt"]
def affichage (equipe, lesjournees):
    for J in lesjournees:
        res=monequipe(equipe,J)
        print J,res

## Deuxieme partie
##partie A
ligue1= ['Bordeaux', 'Marseille', 'Lille', 'Lyon', 'Lorient',
'Nantes', 'Auxerre', 'Monaco', 'Valenciennes', 'Montpellier',
'Toulouse', 'Sochaux', 'Boulogne', 'Nancy', 'Paris', 'Nice']

def cree_dico(ligue1):
    dico={}
    for x in ligue1:
        dico[x]=0
    return dico

## 2/
def aumoins(dico,p):
    lres=[]
    for x in dico:
        if dico[x]>=p:
            lres+=[x]
    return lres

## 3/
MonDico={'Lorient': 0, 'Sochaux': 0, 'Lyon': 0, 'Auxerre': 0,
'Toulouse': 0, 'Montpellier': 0, 'Lille': 0, 'Paris': 0, 'Valenciennes':
0, 'Boulogne': 0, 'Nice': 0, 'Nancy': 0, 'Monaco': 0, 'Bordeaux': 0,
'Marseille': 0, 'Nantes': 0}

def prem (dico):
    lePlus=0
    #lePlus=max(dico.values())   ... donne directement le max des valeurs
    for x in dico:
        if dico[x]>Plus:
            lePlus=dico[x]
    L=aumoins(dico,lePlus)
    return L

##Parie B
def ajoute (dicoResultats, fichier_journee):
    f=open(fichier_journee,"r")
    for ligne in f:
        L=ligne.split()
        if int(L[-1])<int(L[-2]):
            dicoResultats[L[0]]+=3
        elif int(L[-1])>int(L[-2]):
            dicoResultats[L[1]]+=3
        elif int(L[-1])==int(L[-2]):
            dicoResultats[L[1]]+=1
            dicoResultats[L[0]]+=1
    f.close()
    return dicoResultats

###########
## TP 12 ##
###########

def multi(p,k):
    p1=[]
    for x in p:
        x=x*k
        p1+=[x]
    return p1

def valeur (p,a):
    res=0
    for i in range (len(p)):
        res+=p[i]*(a**i)
    return res

def deriv (p):
    Lres=[]
    if (len(p))<1:
        return Lres
    else:
        for i in range (1,len(p)):
            Lres+=[p[i]*i]
        return Lres
    
##>>> deriv([1,0,2,1,-2])
##[0, 4, 3, -8]
##>>> deriv([1])
##[]

def som2(p,q):
    Lres=[]
    for i in range (len(p)):
        Lres+=[p[i]+q[i]]
    while Lres[-1]==0:
        Lres=Lres[:-2]
    return Lres
##
##def fois(pol,n):
##    Lres
##        

###############
## dev perso ##
###############

# code pour compter les heures de conduite
a=input("entrer le nombre d'heure?")
b=input("entrer le nombre de minute?")
min=b/60
heure=min+a
minute=b-min*60
print "Tu as travaillé : ", heure, "heures et", minute, "minutes. Felicitation =D"

#############
## TP Note ##
#############

## Mathilde et Betty 
from Tkinter import *

fen=Tk()

nb= 10      # nombre de cases par ligne (grille carree)
c=35        # dimension d'une case supposee carree
x0,y0=20,20 #coordonnées du point en haut à gauche

couleur="black" # couleur par defaut

can=Canvas(fen,height=500,width=500,bg="white")

##les fonctions...

def dessine_grille():
    for i in range(nb+1):
        can.create_line(x0+c*i, y0,x0+c*i,y0 + nb*c)
        can.create_line(x0, y0+c*i,x0+nb*c ,y0+c*i)


def cree_mat():
    mat=[]
    for i in range(nb):
        col = []
        for j in range(nb):
            col.append(0)
        mat.append(col)
    return mat

matrice=cree_mat()


def sauvegarder(): ## sauvegarder le fichier
    ## mise en place des nouveaux widgets
    BCharger.grid_forget()
    BSauvegarde.grid(row=2,column=999)
    Lsauvegarde.grid(row=3,column=999)
    ENomsauve.grid(row=4,column=999)
    ##lancement de l'ecriture
    fichier=open('C:\\test.txt',"w")
    for ligne in matrice:
        for valeur in ligne:
            fichier.write(str(valeur)+" ")
        fichier.write('\n')
    fichier.close()
    ENomsauve.bind("<Return>",ecriture)  

    
def ecriture(f): ## reecriture du ficher qui s'appelle - a -
    ENomsauve.grid_forget()
    Lsauvegarde.grid_forget()
    BCharger.grid(row=3,column=999)
    a=ENomsauve.get()
    f=str("C:\\"+a+".txt")
    f1=open(f,"w")
    f2=open('C:\\test.txt',"r")
    for ligne in f2:
        f1.write(str(ligne),)
    f1.close()
    f2.close()
    

def lire():  ## recuperer le fichier a charger et mise en place des nouveaux widgets
    BSauvegarde.grid_forget()
    Lcharge.grid(row=3,column=999)
    ENomcharge.grid(row=4,column=999)
    BCharger.grid(row=2,column=999)
    
    ENomcharge.bind("<Return>",affiche)

    
def affiche(f): ## affiche un dessin deja existant
    Lcharge.grid_forget()
    ENomcharge.grid_forget()
    BSauvegarde.grid(row=3,column=999)
    r=ENomcharge.get()     # recuperer le nom du fichier a ouvrir
    f=str("C:\\"+r+".txt")
    f1=open(f,"r")
    i=0
    for ligne in f1:
        liste=ligne.split()
        j=0
        for j in range (len(liste)):
            if liste[j]=='0':
                couleur="white"
                can.create_rectangle(x0 +c*j,y0+c*i,x0 +c*(j+1),y0+c*(i+1),fill=couleur)
                j+=1
            elif liste[j]=='green':
                couleur="green"
                can.create_rectangle(x0 +c*j,y0+c*i,x0 +c*(j+1),y0+c*(i+1),fill=couleur)
                j+=1
            elif liste[j]=='black' :
                couleur="black"
                can.create_rectangle(x0 +c*j,y0+c*i,x0 +c*(j+1),y0+c*(i+1),fill=couleur)
                j+=1
            elif liste[j]=='red':
                couleur="red"
                can.create_rectangle(x0 +c*j,y0+c*i,x0 +c*(j+1),y0+c*(i+1),fill=couleur)
                j+=1
            elif liste[j]=='blue':
                couleur="blue"
                can.create_rectangle(x0 +c*j,y0+c*i,x0 +c*(j+1),y0+c*(i+1),fill=couleur)
                j+=1
        i+=1
    f1.close()
       

def gommer():
    global couleur
    couleur="white"

def correspond(x,y):
    return [(y-y0)/c,(x-x0)/c]

def vert():
    global couleur
    couleur="green"

def rouge():
    global couleur
    couleur="red"
    
def noir():
    global couleur
    couleur="black"
    
def bleu():
    global couleur
    couleur="blue"

def donne_position(event): ## trouve les coordonnees et colore la grille
    global couleur
    global matrice
    [i,j]=correspond(event.x,event.y)
    if i in range(nb) and j in range (nb):
        can.create_rectangle(x0 +c*j,y0+c*i,x0 +c*(j+1),y0+c*(i+1),fill=couleur)
        if couleur=="white":
            matrice[i][j]=0
        else:
            matrice[i][j]=couleur
        
        
def quitter ():
    fen.quit()
    fen.destroy()

## LES FONCTIONS DE LA PARTIE 2

def jouer():
    BSauvegarde.grid_forget()
    BCharger.grid_forget()
    BNouvelleGrille.grid_forget()
    LFic.grid(row=1,column=999)
    EJouer.grid(row=2,column=999)

    EJouer.bind("<Return>",jeu)

def jeu(f): ## on affiche la moitie du fichier
    dessine_grille()
    a=EJouer.get()
    f=str("C:\\"+a+".txt")
    f1=open(f,"r")
    
    i=0
    for ligne in f1:
        liste=ligne.split()
        j=0
        for j in range (5):
            if liste[j]=='0':
                couleur="white"
                can.create_rectangle(x0 +c*j,y0+c*i,x0 +c*(j+1),y0+c*(i+1),fill=couleur)
                matrice[i][j]=0
            elif liste[j]=='green':
                couleur="green"
                can.create_rectangle(x0 +c*j,y0+c*i,x0 +c*(j+1),y0+c*(i+1),fill=couleur)
                matrice[i][j]=couleur
            elif liste[j]=='black' :
                couleur="black"
                can.create_rectangle(x0 +c*j,y0+c*i,x0 +c*(j+1),y0+c*(i+1),fill=couleur)
                matrice[i][j]=couleur
            elif liste[j]=='red':
                couleur="red"
                can.create_rectangle(x0 +c*j,y0+c*i,x0 +c*(j+1),y0+c*(i+1),fill=couleur)
                matrice[i][j]=couleur
            elif liste[j]=='blue':
                couleur="blue"
                can.create_rectangle(x0 +c*j,y0+c*i,x0 +c*(j+1),y0+c*(i+1),fill=couleur)
                matrice[i][j]=couleur
        i+=1
    f1.close()
    LFic.grid_forget()
    EJouer.grid_forget()
    BValide.grid(row=1,column=999)


def valide(): ## test la symetrie
    global matrice
    BValide.grid_forget()
    BNouvelleGrille.grid(row=1,column=999)    
    i=0
    for ligne in matrice:
        k=(-1)
        for j in range (0,5):
            if matrice[i][j]!=matrice[i][k]:
                LDesErreurs.grid(row=2,column=999)
            k=k-1
        if i<9:
            i+=1
    LBravo.grid(row=2,column=999)

## Fonctions questions supplémentaires

def axe ():
    can.create_line(x0+c*5, y0, x0+c*5, y0+10*c, fill="cyan", width=3)    
    

## l'interface, les widgets
    
LTitre=Label(fen,text="Tp note Mathilde & Betty",font=("courrier","14","bold"),fg="blue")
BNouvelleGrille=Button(fen,text="Nouvelle grille",font=("courrier","14","bold"),command=dessine_grille)
BSauvegarde=Button(fen,text="Sauvegarde",font=("courrier","14","bold"),command=sauvegarder)
BCharger=Button(fen,text="Charger",font=("courrier","14","bold"),command=lire)
BQuitter=Button(fen,text="Quitter",font=("courrier","10","bold"),command=quitter)
BGomme=Button(fen,text="Gomme",command=gommer)
BVert=Button(fen,bg="green",command=vert)
BRouge=Button(fen,bg="red",command=rouge)
BNoir=Button(fen,bg="black",command=noir)
BBleu=Button(fen,bg="blue",command=bleu)

ENomsauve=Entry(fen)
ENomcharge=Entry(fen)
Lsauvegarde=Label(fen,text="Nom du fichier de sauvegarde")
Lcharge=Label(fen,text="Nom du fichier a charger")

LTitre.grid(row=0,column=0,columnspan=1000)
can.grid(row=1,column=0,rowspan=500,columnspan=999)
BNouvelleGrille.grid(row=1,column=999)
BSauvegarde.grid(row=2,column=999)
BCharger.grid(row=3,column=999)
BQuitter.grid(row=504,column=999)
BGomme.grid(row=502,column=0)
BVert.grid(row=501,column=500)
BRouge.grid(row=502,column=500)
BNoir.grid(row=503,column=500)
BBleu.grid(row=504,column=500)

## partie deux, les nouveaux widgets

BJouer=Button(fen,text="Jouer",font=("courrier","18","bold"),command=jouer)
LFic=Label(fen,text="fichier pour jouer?")
EJouer=Entry(fen)
BValide=Button(fen,text="Valide",font=("courrier","18","bold"),command=valide)
LBravo=Label(fen,text="BRAVO",font=("courrier","18","bold"),bg="white")
LDesErreurs=Label(fen,text="DES ERREURS",font=("courrier","18","bold"),bg="white")

BJouer.grid(row=503,column=999)

## Partie questions supplémentaires
BAxe=Button(fen,text="axe",command=axe)
BAxe.grid(row=502,column=1)


can.bind("<Button-1>",donne_position)

fen.mainloop()

################
##            ##
##   FIN      ##
## Licence L1 ##
##            ##
################

################
##            ##
##   DEBUT    ##
## Licence L2 ##
##            ##
################

## POO Python : programmation orientée objet.

##########
## TP 1 ## POO
##########

from string import ascii_letters
from random import shuffle

## 1/
def creerCode():
    dico={}
    L1=list(ascii_letters)
    L2=L1[:]         ## important sinon L1 et L2 on les memes adresses
    shuffle(L2)
    i=0
    for el in L1:
        dico[el]=L2[i]
        i+=1
    return dico
 
        
## 2/
def coder(code,ficEntree,ficSortie):
    fe=open(ficEntree,"r")
    en=fe.read()
    fe.close()
    coden=''
    for x in en:
        if x in code:
            y=code[x]
        else:
            y=x
        coden+=y
    
    fs=open(ficSortie,"w")
    fs.write(coden)
    fs.close()

## 3/ on connait le code = on connait le dico
def decoder(code,f1,f2): ##f1 ficher crypte et f2 fichier obtenu apres.

## creer un dico inverse et  re utiliser le fonction code.
    f1=open(f1,"r")
    f2=open(f2,"w")
    for ligne in f1:
        mots=ligne.split()
        for x in mot:
            for cle in code:
                if x==code[cle]:
                    f2.write(cle)
        f2.write(" ")
    f1.close()
    f2.close()

## 4/
from string import zfill

def creerCodeBis():
    dico={}
    L1=list(ascii_letters)
    Lcle=L1[(len(L1)/2):]
##    for cle in Lcle:
##        dico[cle]=
##    
    

##########
## TP 2 ## POO  
##########
from math import *

##quest1
def code(val,nbBits):
    res=''
    for i in range (nbBits):
        (val,r)=divmod(val,2)
        res=str(r)+res
    return res

##quest2
def longueur(k):
    if k>1:
        y=ceil(log(k,2))
        return int(y)
    elif k==1:
        return 1
    
##quest3
def codeFacteur(num,rang,c):
    nb=longueur(num)
    b=code(rang,nb)
    res=b+c
    return res

##quest4
def compression(s):
    dic={'':0}
    fac=''
    rang=1
    for x in s:
        fac=fac+x
        if not fac in dic:
            dic[fac]=rang
            rang+=1
            fac=''
    return dic

##########
## TP   ## POO tortue  
##########

# -*- coding:utf-8 -*-
from math import *

from lindenmayer import *
import sys
if sys.version_info[0]==3:
    from tkinter import *
else:
    from Tkinter import *

class Tortue(object):
    can=None # le canevas est défini comme attribut de classe
    def __init__(self):
        self.ori=0   # l'orientation en degré
        self.posx=float(Tortue.can.cget('width'))/2
        self.posy=float(Tortue.can.cget('height'))/2
        self.trace=True
        self.color='blue'
        
    def positionner(self,x,y):
        self.posx=x
        self.posy=y

    def tourneGauche(self,valeur):
        self.ori+=valeur

    def tourneDroite(self,valeur):
        self.ori-=valeur

    def avance(self,valeur):
        X=self.posx+cos(self.ori*pi/180)*valeur
        Y=self.posy-sin(self.ori*pi/180)*valeur
        Tortue.can.create_line(self.posx,self.posy,X,Y,fill=self.color)
        self.posx=X
        self.posy=Y
       
    def recule(self,valeur):
        self.avance(-valeur)

    def leveCrayon(self):
        self.trace=False        

    def baisseCrayon(self):
        self.trace=True
 
    def couleur(self,color):
        self.color=color

    def dessineMot(self,mot,lg,ang):
        L=[]
        for car in mot:
            if car=="f":
                self.avance(lg)
            if car=="+":
                self.tourneGauche(ang)
            if car=="-":
                self.tourneDroite(ang)
            if car=="[":
                a=self.posx
                b=self.posy
                L.append((a,b))
            if car=="]":
                self.positionner(L[-1][0],L[-1][1])
                L.pop()
            

if '__main__'==__name__:
    
    fen=Tk()
    Tortue.can=Canvas(fen,width=800,height=800,bg='black')
    Tortue.can.grid()
    t=Tortue()

##question6
    A=LSysteme('x',{'x':'f[+x]f[-x]+x','f':'ff'})
    m=A.genere(5)
    t.dessineMot(m,10,20)

    fen.mainloop()

# ------------- Quelques systèmes
# dragon. 'fx',{'f':'','x':'-fx++fy-','y':'+fx--fy+'}  angle=45
# flocon. 'fl',{'f':'','l':'fl-fr--fr+fl++flfl+fr-','r':'+fl-frfr--fr-fl++fl+fr'} angle=60
# avec mémoire. 'x',{'x':'f[+x]f[-x]+x','f':'ff'} angle=20


##########
## TP   ## POO lindenmayer  
##########

# -*- coding:utf-8 -*-
class LSysteme(object):
    def __init__(self,axiom,regles):
        self.axiom=axiom
        self.dico=regles
        self.reset()

    def reset(self):
        self.mot=self.axiom
        self.generation=0

    def getMot(self):
        return self.mot

    def etape(self):
        self.generation+=1
        motsuiv=''
        for car in self.mot:
            motsuiv+=self.dico.get(car,car)
        self.mot=motsuiv

    def genere(self,n=1):
        self.reset()
        for i in range(n):
            self.etape()
        return self.mot

if __name__=='__main__':
    l=LSysteme('a',{'a':'ba','b':'a'})

    print(l.getMot())
    for i in range(5):
        l.etape()
        print(l.getMot())

## question2 test1
axiome="fx"
regles={"f":"","x":"-fx++fy","y":"+fy--fy+"}
def test1():
    A=LSysteme(axiome,regles)
    for i in range (1,4):
        print (A.genere(i))
             

##########
## TP   ## POO interfimage  
##########

# -*- coding:utf-8 -*-

## LA PARTIE INTERFACE
from traitementImage import *
import sys
if sys.version_info[0]==3:
    from tkinter import *
else:
    from Tkinter import *


class Appli(Tk):
    dec=30
    " la classe Appli dérive de la classe Tk definie dans le module Tkinter"
    def __init__(self):
        # la classe dérivée appelle l'initialisateur de la classe mère
        Tk.__init__(self)
        self.configure(bg='#ffffb2')
        self.title("Image")
        self.cote=10
        self.can=Canvas(self,height=760,width=760,bg='#aabbcc')
        self.can.grid(rowspan=4,column=0)
        
        ctrOperation=Frame(self,bg='#f0f0b0')
        ctrOperation.grid(row=1,column=1)
        Label(ctrOperation,text='Opérations',bg='#ffffb2').grid(row=0,padx=30,pady=10)
        Button(ctrOperation,text='Négatif',command=self.clicNeg).grid(row=1,pady=10)
        Button(ctrOperation,text='Lissage',command=self.clicLissage).grid(row=2,pady=10)
        
        Button(self,text='Image aléatoire',command=self.clicNouveau).grid(row=2,column=1)
        Button(self,text='Quitter',width=10,command=self.destroy).grid(row=5,column=1,pady=20)

        self.clicNouveau()

    def carre(self,i,j):
        cotdec=self.cote+Appli.dec
        val=self.image.getPixel(i,j)
        valhex=hex(val)[2:]
        if len(valhex)==1:valhex='0'+valhex
        coul='#'+valhex*3
        self.can.create_rectangle(self.cote*i+Appli.dec,self.cote*j+Appli.dec,self.cote*i+cotdec,self.cote*j+cotdec, fill=coul) 

    def affiche(self):
        self.can.delete('ALL')
        for i in range(self.image.nbLig):
            for j in range(self.image.nbCol):
                self.carre(i,j)

    def clicNouveau(self):
        self.image=Ima(20,20)
        self.cote=(min(int(self.can.cget('height')),int(self.can.cget('width')))-2*Appli.dec)/max(self.image.nbLig,self.image.nbCol)
        self.affiche()
        
    def clicLissage(self):
        self.image.lissage()
        self.affiche()
        
    def clicNeg(self):
        self.image.negatif()
        self.affiche()


if __name__ == '__main__':        
    app=Appli()
    app.mainloop()
    

##########
## TP   ## POO frequ  
##########

freq={'A': 8, 'C': 3, 'B': 1, 'E': 13, 'D': 4, 'G': 1, 'F': 1, 'I': 7, 'H': 1, 'K': 1, 'J': 1, 'M': 3, 'L': 6, 'O': 5, 'N': 7, 'Q': 1, 'P': 3, 'S': 8, 'R': 7, 'U': 6, 'T': 7, 'W': 1, 'V': 2, 'Y': 1, 'X': 1, 'Z': 1}

##########
## TP   ## POO traitementimage  
##########

# -*- coding:utf-8 -*-

from random import randrange

class Ima(object):
    def __init__(self,*args):
        if len(args)==1 and type(args[0])==list:
            self.tab = args[0]
            self.nbLig=len(self.tab)
            self.nbCol=len(self.tab[0])
        elif len(args)==2:         
            self.creerImAlea(args[0],args[1])
        self.info = {}

    def creerImAlea(self,nbLig,nbCol):
       self.nbLig=int(nbLig)
       self.nbCol=int(nbCol)
       self.tab=[[randrange(256) for j in range(nbCol)] for i in range(nbLig)]

    def __repr__(self):
        return str(self.tab)+'\n'

##1/
    def getPixel(self,i,j):
        return self.tab[i][j]
##2/
    def setPixel(self,i,j,val):
        self.tab[i][j]=val
##3/
    def negatif(self):
        for i in range (self.nbLig):
            for j in range (self.nbCol):
                x=self.getPixel(i,j)
                self.setPixel(i,j,(255-x))
##4/
    def lissage(self):
        tamp=[[self.tab[i][j]  for j in range(self.nbCol)] for i in range(self.nbLig)]
        for i in range (1,self.nbLig-1):
            for j in range (1,self.nbCol-1):
                v1=tamp[i-1][j-1]
                v2=tamp[i-1][j]
                v3=tamp[i-1][j+1]
                v4=tamp[i][j-1]
                v5=tamp[i][j+1]
                v6=tamp[i+1][j-1]
                v7=tamp[i+1][j]
                v8=tamp[i+1][j+1]
                v=tamp[i][j]
                moy=(v1+v2+v3+v4+v5+v6+v7+v8+v)/9
                self.tab[i][j]=moy               

##5/
    def histogramme(self):
        self.histo=[0]*256
        for i in range (self.nbLig):
            for j in range (self.nbCol):
                rang=self.tab[i][j]
                self.histo[rang]+=1

##6
    def mini(self):
        for i in range (len(self.histo)):
            if self.histo[i]>0:
                return i

##7/
    def maxi(self):
        m=(self.nbLig)*(self.nbCol)
        for i in range (len(self.histo)):
            if self.histo[i]<m:
                return i
        
##8/
    def contraste(self):
        vmin=self.mini()
        vmax=self.maxi()
        for i in range (self.nbLig):
            for j in range (self.nbCol):
                v=self.tab[i][j]
                self.setPixel(i,j,((255*(v-vmin))/(vmax-vmin)))

   
        

if __name__ == '__main__':
    im=Ima([[16*i+j for j in range(16)] for i in range(16)])
    print(im)
    im.negatif()
    print(im)
    im=Ima(8,5)
    print(im)
    im.lissage()
    print(im)


##########
## TP   ## POO decorateur  
##########

# -*- coding:utf-8 -*-

class Test(object):
    def __init__(self):
        self.nb=0
        self.dico={}

    def trace(self, func):
        def wrapper(*args):
            res=func(*args)            
            print('execution de',func.__name__ ,func.__doc__,args,res)
            return res
        return wrapper

    def compte(self, func):
        def wrapper(*args):
            self.nb+=1
            return func(*args)
        return wrapper


    def comptedic(self, func):
        def wrapper(*args):
            if args in self.dico:
                self.dico[args]+=1
            else:
                self.dico[args]=1
            return func(*args)
        return wrapper

    def enumere(self,fonc):
        def wrapper(*args):
            d=self.dico
            res=sum(d.values())
            return func(*args)
        return wrapper


## memorisation . question 3
class Memorisation(object):

    def __init__(self):
        self.dic={}
        
    def cache(self,f):
        def fmodifiee(*args):
            if args not in self.dic:
                self.dic[args]=f(*args)
            return self.dic[args]
        return fmodifiee

            

        

if __name__=='__main__':

    test1 = Test()

    @test1.trace
    def blabla(n):
        " fn jouet "
        return 'bla'*n

    print(blabla(4))

    memo=Memorisation()

@test1.compte
@test1.comptedic
@memo.cache
def fiboNaif(n):
##     " la fonction de Fibonacci"
    if n<2:
        return n
    return fiboNaif(n-1)+fiboNaif(n-2)

@test1.compte
@test1.comptedic
@memo.cache
def binoNaif(n,p):
##     "la fonction binomiale"
    if p in (0,n):
        return 1
    return binoNaif(n-1,p)+binoNaif(n-1,p-1)

print fiboNaif(7)
print test1.nb,test1.dico,
test1.__init__()
print binoNaif(10,5)
print test1.nb,test1.dico

##verification :
##13
##41 {(0,): 8, (1,): 13, (2,): 8, (3,): 5, (4,): 3, (5,): 2, (6,): 1, (7,): 1}
##252
##503 {(7, 3): 3, (3, 0): 15, (5, 4): 5, (2, 1): 70, (6, 2): 4, (9, 4): 1, (5, 1): 5, (8, 5): 1, (7, 2): 1, (4, 0): 5, (5, 5): 1, (4, 4): 5, (6, 3): 6, (5, 0): 1, (2, 2): 35, (3, 3): 15, (4, 1): 15, (1, 1): 70, (6, 4): 4, (3, 2): 35, (8, 3): 1, (7, 5): 1, (4, 2): 20, (1, 0): 70, (6, 5): 1, (5, 3): 10, (10, 5): 1, (6, 1): 1, (3, 1): 35, (7, 4): 3, (2, 0): 35, (4, 3): 15, (9, 5): 1, (5, 2): 10, (8, 4): 2}
##>>> d={(0,): 8, (1,): 13, (2,): 8, (3,): 5, (4,): 3, (5,): 2, (6,): 1, (7,): 1}
##>>> sum(d.values())
##41


## Exceptions
## question 5

class NegativeNumberError(ArithmeticError):

    def __init__(self,arg=None):
        if arg==None:
           arg="erreur, nb negatif"
        ArithmeticError.__init__ (self,arg)  

def racinecarre(n):
    if n<0:
        raise NegativeNumberError()
    return n**.5

def demande():
    x= input("Entrer un nombre positif ? ")
    return racinecarre(x)
        


##########
## TP   ## POO exam  
##########

# -*- coding:utf-8  -*-
"""
Méthodes statiques. Personnalisation de la création des instances
Le sujet suivant est une méthode particulière : __new__,
qui est appelée au moment de la création de l'instance d'une classe.
Elle appartient à la catégorie des méthodes statiques qui n'ont pas
d'instance "recepteur" : obj.__new__(...), puisque son appel a lieu
quand l'instance en question n'est pas encore allouée dans la mémoire.
Donc, pas de self ! C'est la classe elle-même qui est l'argument
implicite, et par convention on l'appelle cls. """

import sys
if sys.version_info[0]==3:
    from tkinter import *
else:
    from Tkinter import *

class ValColorError(Exception): pass

class CouleurRVB(dict):
    def __init__(self,r,v,b,nom="pas de nom"):
        if r<0 or v<0 or b<0 or r>255 or v>255 or b>255:
            raise ValColorError("une valeur de couleur n'est pas valide")
        dict.__init__(self,{'r':r,'v':v,'b':b})
        self.nom=nom

    def code(self):
        res='#'
        for cle in ['r','v','b']:
            if self[cle]<16:res+='0'
            res+=hex(self[cle])[2:]
        return res

    def intensite(self):
        return max(self.values())

    def __repr__(self):
        fen=Tk()
        fen.title('couleur rvb :'+str(self['r'])+','+str(self['v'])+','+str(self['b']))
        Label(fen,text=self.nom,width=20,height=10,bg=self.code()).grid()
        fen.mainloop()
        return self.code()

    def __add__(self,autre):
        if isinstance(autre,CouleurRVB):
            r=self['r']+autre['r']
            v=self['v']+autre['v']
            b=self['b']+autre['b']
            i=(self.intensite()+autre.intensite())//2
            maxi=max(r,v,b)
            return CouleurRVB((r*i)//maxi,(v*i)//maxi,(b*i)//maxi)

class CouCouRVB(tuple):
    def __init__(self,r,v,b):
        if 0<=r and r<256 and 0<=v and v<256 and 0<=b and b<256:
            tuple.__init__(self,(r,v,b))
        else:
            raise ValColorError("une valeur de couleur n'est pas valide")
        
class CouTupleRVB(tuple):
    def __new__(cls,r,v,b):
        if 0<=r and r<256 and 0<=v and v<256 and 0<=b and b<256:
            # return tuple.__new__(cls,(r,v,b))  # ! return
            return tuple.__new__(CouTupleRVB,(r,v,b))  # ! return
        else:
            raise ValColorError("une valeur de couleur n'est pas valide")

    def code(self):
        res='#'
        for val in self:
            if val<16:res+='0'
            res+=hex(val)[2:]
        return res
        
if __name__=="__main__":
    c1=CouleurRVB(16,20,100)
    c2=CouleurRVB(255,200,0)
    c3=c1+c2
    # print (c1, c1.intensite());print (c2);print (c3)

    
    d=CouTupleRVB(16,20,100)
    print (d, d.code())



################
##            ##
##   FIN      ##
## Licence L2 ##
##            ##
################

################
##            ##
##   DEBUT    ##
## Licence L3 ##
##            ##
################

## conception logiciel ## 

##########
## TP   ## POO compte
##########

class Compte(object):

    def __init__(self,solde,numerodeCompte):
        self.__solde=solde
        self.__num=numerodeCompte

    def debit(self,montant):
        if montant<self.__solde:
            self.__solde-=montant
            return self.__solde
        return False

    def credit(self,montant):
        if montant>0:
            self.__solde+=montant
            return self.__solde
        return False

    def getsolde(self):
        return self.__solde
    
    def getnum(self):
        return self.__num

    def __str__(self):
        res="solde : "+str(self.__solde)+" \n"
        res+="Numero : "+str(self.__num)+" \n"
        return res
        


class ComptePersonnel(Compte):

    def __init__(self,solde,numerodeCompte,limit):
        Compte.__init__(self,solde,numerodeCompte)
        self.__limit=limit

    def getlimit(self):
        return self.__limit
    def setlimit(self,val):
        self.limit=val

    def __str__(self):
        res=Compte.__str__(self)
        res+="limite : "+str(self.__limit)
        return res

    def afficheInfos(self):
        return(self.getsolde(),self.getnum(),self.__limit)

    def debit(self,montant):
        if montant<self.__limit and montant<self.getsolde():
            Compte.debit(self,montant)
            return True
        return False



class CompteEpargne(Compte):

    def __init__(self,solde,numerodeCompte,taux):
        Compte.__init__(self,solde,numerodeCompte)
        self.__taux=taux

    def appliqueTaux(self):
        montant=(self.getsolde())*(self.__taux)
        Compte.credit(self,montant)
    
    def afficheInfos(self):
        return(self.getsolde(),self.getnum(),self.__taux)

    def setTaux(self,t):
        self.__taux=t

    def __str__(self):
        res=Compte.__str__(self)
        res+="taux : "+str(self.__taux)
        return res
##from Tkinter import *
##
##class Fen(Tk):
##    
##    def __init__(self,cp,ce*args,**kw):
##        Compte=Label(fen,text="Mes Comptes")
##        Compte.grid(row=0,column=0,columnspan=3)
##        bcp=Button(fen,text="CP",command=CP)
##        bcp.grid(row=2,column=0)
##        bce=Button(fen,text="CE",command=CE)
##        bce.grid(row=2,column=1)
##        bq=Button(fen,text="Quitter",command=quitter)
##        bq.grid(row=2,column=2)
##        
##
##    def quitter():
##        fen.quit()
##        fen.destroy()
##         
##    def CP():pass
##    def CE():pass
##
##



if __name__ == "__main__" :

    c=Compte(1000,21001703)
    print c
    print c.debit(500)
    print c.credit(200)

    cp=ComptePersonnel(1000,21001703,100)
    print cp.afficheInfos()
    cp.debit(50)
    print cp.afficheInfos()
    print cp
    
    ce=CompteEpargne(1000,21001703,0.05)
    print ce.afficheInfos()
    ce.appliqueTaux()
    print ce.afficheInfos()
    print ce

##    Fen(cp,ce).mainloop()


##########
## TP 1 ## Carre magic
##########

## ex 1
## 1/
def Deg(x):
    return (9./5)*x+32
## retourne la T en Fahrenheit

def Fah(x):
    return (x-32)*5./9
## retourne la T en Degrè

## 2/
## a/
def compte(h,m,s):
    return s+m*60+h*60*60

## b/
def heuresuiv(h,m,s):
    if s!=59 :
        if m!=59:
            return str(h)+" h "+str(m)+" m "+str(s+1)+" s"
    elif m!=59:
        return str(h)+" h "+str(m+1)+" m 0s"
    elif h!=23:
        return str(h+1)+" h 0m 0s"
    else:
        return "0h 0m 0s"

## ex 2
def fact(n):
    if n==0:return 1
    else:
        s=1
        while n!=1:
            s=s*n
            n-=1       ## n=n-1
        return s

## ex3
##1/
def sommeEntiers(l):
    s=0
    for i in range (len(l)):
        s+=l[i] ## s=s+l[i]
    return s
        
##2/
def listeDiviseurs(n):
    List=[]
    x=1
    while x<n:
        if n%x==0:
            List+=[x]
        x+=1
    return List
    
##3/
def entierParfait(n):
    list=listeDiviseurs(n)
    return sommeEntiers(list)==n

##4/
def ListeEntiersParfaits(b):
    res=[]
    x=1
    while x<b:
        if entierParfait(x):
            res+=[x]
        x+=1
    return res

## Ex4
        
##1/
def somme(l):
    s=0
    for i in range (len(l)):
        s+=l[i]
    return s

##2/
def sommeligne(tab,i):
    return somme(tab[i])

##3/
def sommecol(tab,j):
    res=0
    for i in range (len(tab)):
        res+=tab[i][j]
    return res
        
##4/
def sommediag(tab):
    res=0
    j=0
    for i in range (len(tab)) :
        res+=tab[i][j]
        j+=1
    return res
    
##5/
def sommeantidiag(tab):
    res=0
    n=len(tab[0])-1
    for i in range (len(tab)) :
        res+=tab[i][n]
        n-=1
    return res
    
##6/
def test(tab):
    somd=sommediag(tab)
    somad=sommeantidiag(tab)
    llig=[]
    lcol=[]
    for i in range(len(tab)):
        llig+=[sommeligne(tab,i)]
    for k in range (len(llig)-1):
        if llig[k]!=llig[k+1]:
            return False
    L1=somme(llig)/(len(tab))
    for j in range (len(tab)):
        lcol+=[sommecol(tab,j)]
    for k in range (len(lcol)-1):
        if lcol[k]!=lcol[k+1]:
            return False
    L2=somme(lcol)/(len(tab))
    return somd==somad==L1==L2
    
        
        

## Test des programme :

if __name__=="__main__":
    tm=[[8,1,6],[3,5,7],[4,9,2]]
    print Deg(100)
    print Fah(32)
    print compte(1,1,0)
    print heuresuiv(23,59,59)
    print heuresuiv(21,59,59)
    print heuresuiv(12,52,59)
    print heuresuiv(14,34,23)
    print fact(0)
    print fact(1)
    print fact(3)
    print sommeEntiers([1,2,3,5,6,10,15])
    print listeDiviseurs(30)
    print entierParfait(6)
    print entierParfait(16)
    print ListeEntiersParfaits(1000)
    print somme ([6,7,2,3,1])
    print sommeligne(tm,0)
    print sommeligne(tm,1)
    print sommecol(tm,1)
    print sommecol(tm,2)
    print sommediag(tm)
    print sommeantidiag(tm)
    print test(tm)
    

##########
## TP   ## Tkinter
##########

from Tkinter import *

fen=Tk()

def quitter():
    fen.quit()
    fen.destroy()

def executer():
    resu=a.get()
    res=eval(resu)
    r2=Label(fen,text=res)
    r2.grid(row=1,column=1)

a=Entry(fen, width=10)
a.grid(row=0,column=0)

ok=Button(fen, text="Ok",command=executer)
ok.grid(row=0,column=1)

r=Label(fen,text="resultat :")
r.grid(row=1,column=0)

b=Button(fen,text="Quitter",command=quitter)
b.grid(row=2,column=1)

fen.mainloop()

##########
## TP   ## calculatrice
##########

from Tkinter import *

fen=Tk()

def quitter():
    fen.quit()
    fen.destroy()

def executer():
    r2.configure(text=eval(a.get()))
    

a=Entry(fen, width=10)
a.grid(row=0,column=0)

ok=Button(fen, text="Ok",bg="green",fg="red",command=executer)
ok.grid(row=0,column=1)

r=Label(fen,text="resultat :",fg="orange")
r.grid(row=1,column=0)

r2=Label(fen,text="")
r2.grid(row=1,column=1)

b=Button(fen,text="Quitter",fg="purple",bg="pink",command=quitter)
b.grid(row=2,column=1)

fen.mainloop()

## calculatrice plus ##

## TP3 calculatrice

from Tkinter import *
from math import *

fen=Tk()

def executer():
    lr2.configure(text=eval(ea.get()))

def calc(event):
    lr2.configure(text=eval(event.widget.get()))


def eff():
    ea.delete("0",END)
    lr2.configure(text="")


def sinus():
    saisi="sin("+ea.get()+")"
    ea.delete("0",END)
    ea.insert("0",saisi)
    lr2.configure(text=eval(ea.get()))

def cosinus():
    saisi="cos("+ea.get()+")"
    ea.delete("0",END)
    ea.insert("0",saisi)
    lr2.configure(text=eval(ea.get()))

def tang():
    saisi="tan("+ea.get()+")"
    ea.delete("0",END)
    ea.insert("0",saisi)
    lr2.configure(text=eval(ea.get()))

def ln():
    saisi="log("+ea.get()+")"
    ea.delete("0",END)
    ea.insert("0",saisi)
    lr2.configure(text=eval(ea.get()))

def quitter():
    fen.quit()
    fen.destroy()



titre=Label(fen,text="Calculatrice")
ea=Entry(fen, width=10)

lr=Label(fen,text="resultat = ",fg="brown")
lr2=Label(fen,text="")

bexe=Button(fen, text="EXE",bg="green",fg="red",command=executer)
beff=Button(fen, text="EFF",fg="red",command=eff)
Button(fen, text="SIN",fg="red",command=sinus).grid(row=3,column=2)
Button(fen, text="COS",fg="red",command=cosinus).grid(row=4,column=2)
Button(fen, text="TAN",fg="red",command=tang).grid(row=5,column=2)
Button(fen, text="LN",fg="red",command=ln).grid(row=6,column=2)
bquitt=Button(fen,text="Q",fg="purple",bg="pink",command=quitter)



titre.grid(row=0,column=1)
ea.grid(row=1,column=1)
lr.grid(row=2,column=0)
lr2.grid(row=2,column=1)
bexe.grid(row=3,column=0)
beff.grid(row=4,column=0)
bquitt.grid(row=6,column=0)

ea.bind("<Return>",calc)
## capte l'evenement "Entree" avec le clavier et utilise le handler clac

fen.mainloop()



##########
## TP   ## Pendu
##########

from random import *

def pendu():
    pv=10
    ##mot1=raw_input("Choisissez un mot : ")
    ##mot=mot1.lower()
    Lmot=["ordinateur","logiciel","portable","musique","judo","sport","cinema"]
    mot=Lmot[randrange(len(Lmot))]
##    f=open("~/Desktop/L3/conception logiciel/liste.txt",'r')
##
##    ##/users/lmass3/e_num_etu/Desktop/L3/conception logiciel
##    cont=0
##    for ligne in f:
##        cont+=1
##    mot=f[randrange(cont)]
    rep="_"*len(mot)
    print " Il y a "+str(len(mot))+" lettres"
    while rep!=mot:
        L=raw_input(" Entrez une lettre : ")
        res=[L!=l for l in mot]
        if  all(res):        
            pv-=1
            print " Plus que "+str(pv)+" essais"
            if pv==0: return "Game over"
        else:
            for i in range(len(res)):
                if not res[i]:
                    rep=rep[:i]+mot[i]+rep[i+1:]
        print rep
##    f.close()
    return "Felicitation =) "


##########
## TP   ## Nombre mysterieux
##########

from Tkinter import *
from random import *

fen=Tk()
x=0
c=0
def jouer():
    global x
    global c
    c+=1
    y=int(EVotrenombre.get())
    if y==(-1):
        global x
        reponse.insert (END, "la reponse etait "+str(x)+" \n")
    elif y<0 or y>100:
        reponse.insert (END, "on cherche un entier entre 1 et 100 \n")
    elif y<x:
        reponse.insert (END, str(y)+ " est trop petit \n")
    elif y==x:
        reponse.insert (END, str(y)+ " bravo c'est gagne en "+ str(c)+ " coups \n")
        Can.grid(row=1,column=0)
        Can.create_image(200,200,image=monIm)
    else:
        reponse.insert(END,str(y)+ " est trop grand \n")
    EVotrenombre.delete("0",END)

def nouvellepartie():
    global x
    reponse.delete("0.0",END)
    EVotrenombre.delete("0",END)
    x=randint(0,101)

def quitter():
    fen.quit()
    fen.destroy()


monIm=PhotoImage(file="/users/lmass3/e_num_etu/Desktop/L3/conception logiciel/bravo.gif")
LTitre=Label(fen,text="Jeu du nombre misterieux : deviner un entier compris entre 1 et 100",fg="purple")
LVotrenombre=Label(fen,text=" entrez votre nombre ",fg="blue")
EVotrenombre=Entry(fen)
BOk=Button(fen,text="OK",command=jouer)
BNouvellepartie=Button(fen,text="Nouvelle Partie",command=nouvellepartie)
BQ=Button(fen,text="quitter",command=quitter)
reponse=Text(fen) ##height=50,width=50
Can=Canvas(fen,height=400,width=400,bg="grey")

LTitre.grid(row=0,column=0,columnspan=3)
LVotrenombre.grid(row=1,column=0)
EVotrenombre.grid(row=1,column=1)
BOk.grid(row=1,column=2)
BNouvellepartie.grid(row=3,column=2)
BQ.grid(row=4,column=2)
reponse.grid(row=2,column=0,columnspan=3)

fen.mainloop()


##########
## TP   ## Jeu du mot
##########

# -*- coding: utf-8 -*-

from Tkinter import *
from random import *

fen=Tk()

mot="ABRICOT"
LisMot=["ABRICOT","POMME","POIRE","FRAISE","BANANE","KIWI","PECHE"]
grillemot=[['Y', 'G', 'N', 'T', 'R', 'A', 'K', 'Q'], ['E', 'V', 'K', 'A', 'F', 'A', 'L', 'Q'], ['B', 'I', 'S', 'U', 'E', 'R',
'X', 'E'], ['R', 'Z', 'E', 'O', 'A', 'B', 'Z', 'O'], ['P', 'K', 'L', 'W', 'X', 'L', 'Y', 'Y'], ['H', 'W', 'L', 'V', 'T', 'O',
'W', 'G'], ['B', 'I', 'O', 'R', 'Z', 'X', 'Q', 'C'], ['K', 'L', 'Y', 'J', 'B', 'T', 'N', 'O']]


def jouer():
    mot=choice(LisMot)
    Elemot.insert("0",mot)
    nb= 8 # nombre de cases par ligne (grille carree)
    c=40 # dimension d'une case supposée carrée
    x0,y0=30,30 #coordonnées du point en haut à gauche
    for i in range(nb+1):
        Can.create_line(x0+c*i, y0,x0+c*i,y0 + nb*c)
        Can.create_line(x0, y0+c*i,x0+nb*c ,y0+c*i)
    for L in grillemot:
        for i in range(len(L)):           
            Can.create_text (x0+20+i*c,y0+20,text=L[i],font=("helvetica",15,"bold"))
        y0+=c


def ecrire (event):
    ## (event.x, event.y) donne les coordonnnées du clic
    ##can.itemconfigure(...)
    saisi=Erep.get()
    l=Can.itemcget(Can.find_closest(event.x,event.y), "text")
    Erep.delete("0",END)
    Erep.insert("0",saisi+l)
    ## can.find_closest(event.x,event.y) ---> retourne l'item du canvas le plus pres du clic

    

def valider():
    saisi=Erep.get()
    lemot=Elemot.get()
    if saisi==lemot:
        Lbravo.pack(side=TOP)
    else:
        Lfaux.pack(side=TOP)
        

def quitter():
    fen.quit()
    fen.destroy()

Can=Canvas(fen,height=400,width=400,bg="white")
Bjouer=Button(fen,text="Jouer",command=jouer)
Lreconstitue=Label(fen,text="Reconstitue ce mot")
Elemot=Entry(fen,bg="grey")
Ltonmot=Label(fen,text="Ton mot")
Erep=Entry(fen,bg="grey")
Bvalider=Button(fen,text="Valider",command=valider)
BQ=Button(fen,text="Quitter",command=quitter)
Lbravo=Label(fen,text="BRAVO",fg="green")
Lfaux=Label(fen,text="Faux",fg="red")

Can.pack(side=LEFT)
Bjouer.pack(side=TOP)
Lreconstitue.pack(side=TOP)
Elemot.pack(side=TOP)
Ltonmot.pack(side=TOP)
Erep.pack(side=TOP)
Bvalider.pack(side=TOP)
BQ.pack(side=BOTTOM)



Can.bind("<Button-1>",ecrire)


##Can.grid(row=0,column=0,rowspan=6)
##Bjouer.grid(row=0,column=1)
##Lreconstitue.grid(row=1,column=1)
##Elemot.grid(row=2,column=1)
##Ltonmot.grid(row=3,column=1)
##Erep.grid(row=4,column=1)
##Bvalider.grid(row=5,column=1)
##BQ.grid(row=6,column=1)

fen.mainloop()


##########
## TP   ## Jeu du Snake
##########

## Jeu du Snake
from Tkinter import *

fen=Tk()

snake=[]
go=True
cpt=0

def jouer():
    global snake
    global go
    Bjouer.configure(text="Pause",command=pause)
    x,y=30,30
    t=20
    for i  in range (6):
        snake+=[can.create_oval(x+t*i,y,x+t+t*i,y+t)]
    while go:
        print "coucou"
        L=can.coords(snake[-1])
        fen.update()
        if L[2]<400:
            
            print L
            ##can.create_oval(L[2],L[1],L[2]+20,L[3])
            can.coords(snake[0],L[2],L[1],L[2]+20,L[3])
            snake.append(snake[0])
            snake.remove(snake[0])
            

def pause():
    global go
    Bjouer.configure(text="Jouer",command=jouer)
    go=False

def droite(event):
    global snake
    global cpt
    global X
    cpt+=1
    L=can.coords(snake[-1])
    if L[2]<500:
        if cpt%4==0:
            ##can.create_oval(L[2],L[1],L[2]+20,L[3])
            can.coords(snake[0],L[2],L[1],L[2]+20,L[3])
            snake.append(snake[0])
            snake.remove(snake[0])
            can.update()
        elif cpt%4==1:
            ##can.create_oval(L[0],L[3],L[2],L[3]+20)
            can.coords(snake[0],L[0],L[3],L[2],L[3]+20)
            snake.append(snake[0])
            snake.remove(snake[0])
            can.update()
        elif cpt%4==2:
            ##can.create_oval(L[0]-20,L[1],L[0],L[3])
            can.coords(snake[0],L[0]-20,L[1],L[0],L[3])
            snake.append(snake[0])
            snake.remove(snake[0])
            can.update()
        elif cpt%4==3:
            ##can.create_oval(L[0],L[1]-20,L[2],L[1])
            can.coords(snake[0],L[0],L[1]-20,L[2],L[1])
            snake.append(snake[0])
            snake.remove(snake[0])
            can.update()
                


##        can.move(snake[0],6*20,0)
##        snake.append(snake[0])
##        snake.remove(snake[0])
##        can.update()


def gauche(event):
    global snake
    global cpt
    global X
    cpt-=1
    while X==0:
                
        L=can.coords(snake[-1])
        if L[2]<500:
            if cpt%4==0:
                ##can.create_oval(L[2],L[1],L[2]+20,L[3])
                can.coords(snake[0],L[2],L[1],L[2]+20,L[3])
                snake.append(snake[0])
                snake.remove(snake[0])
                can.update()
            elif cpt%4==1:
                ##can.create_oval(L[0],L[3],L[2],L[3]+20)
                can.coords(snake[0],L[0],L[3],L[2],L[3]+20)
                snake.append(snake[0])
                snake.remove(snake[0])
                can.update()
            elif cpt%4==2:
                ##can.create_oval(L[0]-20,L[1],L[0],L[3])
                can.coords(snake[0],L[0]-20,L[1],L[0],L[3])
                snake.append(snake[0])
                snake.remove(snake[0])
                can.update()
            elif cpt%4==3:
                ##can.create_oval(L[0],L[1]-20,L[2],L[1])
                can.coords(snake[0],L[0],L[1]-20,L[2],L[1])
                snake.append(snake[0])
                snake.remove(snake[0])
                can.update()
                



##        can.move(snake[-1],(-6)*20,0)
##        snake=[snake[-1]]+snake
##        snake=snake[:-1]
##        can.update()


def quitter():
    fen.quit()
    fen.destroy()


can=Canvas(fen,height=400,width=400,bg="white")
Bjouer=Button(fen,text="Jouer",command=jouer)
BQ=Button(fen,text="Quitter",command=quitter)

can.grid(row=0,column=0,rowspan=2)
Bjouer.grid(row=0,column=1)
BQ.grid(row=1,column=1)

can.bind("<Button-1>",gauche)
can.bind("<Button-3>",droite)


fen.mainloop()

##########
## TP   ## Oct
##########

from Tkinter import *

fen=Tk()

def ecrire():
    can.delete(ALL)
    x=can.winfo_width()/2
    y=can.winfo_height()/2
    can.create_text(x,y,text=eEntre.get())


def quitter():
    fen.quit()
    fen.destroy()


varv= IntVar()
varh= IntVar()
def blocage():
    fen.resizable(not varv.get(),not varh.get())
    
eEntre=Entry(fen,bg="grey")
eEntre.grid(row=0,column=0,sticky=EW)
Button(fen,text="Clicker",command=ecrire).grid(row=0,column=1,sticky=EW)
can=Canvas(fen,bg="white")
can.grid(row=1,column=0,columnspan=2,sticky=NSEW)
Button(fen,text="Quitter",command=quitter).grid(row=2,column=1,rowspan=2,sticky=EW)


ch = Checkbutton(fen, text="blocage horizontal", variable=varv,command=blocage,anchor=W)
cv = Checkbutton(fen, text="blocage vertical", variable=varh,command=blocage,anchor=W)
ch.grid(row=2,column=0,sticky=EW)
cv.grid(row=3,column=0,sticky=EW)

#fen.grid_columnconfigure(0,weight=1) 
fen.grid_columnconfigure(1,weight=1)
fen.grid_rowconfigure(1,weight=1)


eEntre.focus_set()

fen.mainloop()


###############################
##                           ##
##   Tp Bataille Navale      ##
##                           ##
###############################

## Jeu Bataille Navale
## version 6.2 : LE JOUEUR CHOISIT LE PLACEMENT DES SES BATEAUX
## + test son choix est correct = pas de superpositions
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
    ## réinitialisation de toute les données
    Eport.delete("0",END)
    Ecrois.delete("0",END)
    Econtr.delete("0",END)
    Etorp.delete("0",END)
    Esous.delete("0",END)
    Lreste1.configure(text="vous avez 5 navires")
    Lreste2.configure(text="5 navires a couler")
    Nmoi=5
    Nordi=5


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
    global mat1
    cpt1=0 ## initialisation du compteur pour le test de superposition
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
        
    ## Test de superposition
    ## efface tout si les navires sont superposés
    for el in mat1:
        cpt1+=sum(el)
    if cpt1!=55:
        cpt1=0
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
        Lpb.configure(text="Il y a un probleme de placement", fg="red")
        
    else:
        Lpb.configure(text="")
        Lpartie.configure(text="C'EST PARTIE ! ", fg="red")
        Nordi=5
        Nmoi=5
                    




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
Lpartie=Label(fen,text="")
Lpb=Label(fen,text="")
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
Lpartie.grid(row=21,column=1,columnspan=8)
Lpb.grid(row=21,column=11,columnspan=10)
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



################
##            ##
##   Suite    ##
## Licence L3 ##
##            ##
################

## TP Optimisation / Combinatoire ## 

#### TP 1 ##############################################

## ex1 :

##132%45 = 42 ## donne le reste de l   division euclidienne
##132/45 = 2 ## donne la parie entiere
##132./45 = 2.933333333333333
x=8
y=5
z= x*y ## = 40
w= x/y ## = 1


## ex2 :

## a)
x=8
y=5
z= x*y ## = 40
w= x/y ## = 1

## b)
x,y,z,w
## 8 5 40 1

## ex3 :

##a)
x=8.0
y=5.0
print x*y
print x/y
## par rapport a l'ex precedent les reponses sont des chiffres a virgule

##b)
a=5
b=5.
print type(a)
print type(b)
##<type 'int'>
##<type 'float'>

## ex4 :
##a)
x=8
y=5
z= x*y ## = 40
w= x/y ## = 1
print x,y,z,w
##b)
print "la valeur est ",a

## ex : 

def absolu(x):
    return abs(x)
absolu(4)
absolu(-3)
absolu(0)

def fact(n):
    res=1
    for i in range (n):
        res=res*(n-i)
    return res
print fact(3)
print fact(7)
## coef binomial : C(7,3)
c=fact(7)/((fact(7-3))*fact(3))
print c ## 35

def factw(n):
    cpt=n
    res=1
    while cpt>1:
        res=res*cpt
        cpt-=1
    return res
print factw(4)
print factw(7)
c2=factw(7)/((factw(7-3))*factw(3))
print c2

def triliste(l):
    lres=[l[0]]
    for i in range(1,(len(l))):
        j=0
        while  j<(len(lres)) and l[i]>lres[j] :
            j+=1
        lres.insert(j,l[i])
    return lres
L=[5,6,9,1]
print L
L2=triliste(L)
print L2

def trimodif(l):
    for i in range(1,len(l)):
        j=0
        tmp=l.pop(i)
        while j<i and l[j]<tmp :
            j+=1
        l.insert(j,tmp)
L1=[3,7,1,5,8]
L3=[5,6,9,1,125,21356,21544,0]
print L1
trimodif(L1)
print L1

def tribulle(L):
    n=len(L)
    for i in range (1,n):
        for j in range (1,n-i+1):
            if L[j-1]>L[j]:
                temp=L[j-1]
                L[j-1]=L[j]
                L[j]=temp
L1=[3,7,1,5,8]
tribulle(L1)        

#### TP 2 ##############################################
# graph alea Parcours Graphe

from random import *
L=['a','b','c','d']

def GrapheOrientAlea(L):
    dic={}
    for i in L:
        dic[i]=[]
        for j in L:
            if i!=j and randint(0,1)==1 :
                ##dic[i]+=[j]
                dic[i].append(j)
    return dic
d=GrapheOrientAlea(L)
## genere un graphe alea orienté 

def GNOA (L):
    res=dict()
    for a in L:
         res[a]=list()
    for i in range (len(L)-1):
        for j in range (i+1,len(L)):
            if randint(0,1)==1:
                res[L[i]].append(L[j])
                res[L[j]].append(L[i])
                res[L[i]].sort()
                res[L[j]].sort()
    return res
d2=GNOA(L)
## genere un graphe alea non orienté


G={'A':['B'],'B':['C','D'],'C':['A'],'D':['A','C'],'E':['F','G'],'F':['B'],'G':['D','F']}
s='E'
etat=dict()
for i in G.keys():
    etat[i]=0
##etat={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0}

## recherche en profondeur dans graphe
def RechProf(G,s,etat):
    sommet=[s]
    etat[s]=1
    for el in G[s]:
        if etat[el]==0:
            etat[el]=1
            sommet+=RechProf(G,el,etat)
    return sommet
res=RechProf(G,s,etat)

## recherche en largueur dans un graphe
def RechLarg(G,s,etat):
    lsom=[s]
    sres=[]
    etat[s]=1
    while lsom!=[]:
        t=lsom.pop(0)
        sres+=[t]
        for i in G[t]:
            if etat[i]==0:
                etat[i]=1
                lsom.append(i)
    return sres
G={'A':['B'],'B':['C','D'],'C':['A'],'D':['A','C'],'E':['F','G'],'F':['B'],'G':['D','F']}
s='E'
etat=dict()
for i in G.keys():
    etat[i]=0
res2=RechLarg(G,s,etat)



####################################################
# Execution 
####################################################

if __name__ == "__main__":

    #graphe oriente aleatoire
    L=['a','b','c','d','e','f','g','h']
    G=GraphOrientAlea(L)

    print G

    #graphe non oriente aleatoire
    L=['a','b','c','d','e','f','g','h']
    G=GraphNonOrientAlea(L)

    print G


    G={'A':['B'],
       'B':['C','D'],
       'C':['A'],
       'D':['A','C'],
       'E':['F','G'],
       'F':['B'],
       'G':['D','F']}
    
    # on trie la liste des sommets
    l_somm=G.keys()
    l_somm.sort()
    
    # on met tous les sommet dans un état non visité 
    etat={}
    for s in l_somm:
        etat[s]=0
        
    # parcours en profondeur 
    # à partir du premier sommet
    print "parcours en profondeur"
    print "à partir du premier sommet"
    for s in l_somm:
        if etat[s]==0:
            print RechProf(G,s,etat)
        
    # on met tous les sommet dans un état non visité 
    etat={}
    for s in l_somm:
        etat[s]=0
            
        
    # parcours en largeur 
    # à partir du premier sommet 
    print "parcours en largeur"
    print "à partir du premier sommet"
    for s in l_somm:
        if etat[s]==0:
            print RechLarg(G,s,etat)
                    
    # autre exemple
    G={1:[2,6],
       2:[],
       3:[1,4],
       4:[3,6],
       5:[3,4],
       6:[5],
       7:[1,5,10],
       8:[7,9],
       9:[8],
       10:[9,11,12],
       11:[13],
       12:[5],
       13:[10,12]}

    l_somm=G.keys()
    l_somm.sort()
    
    etat={}
    for s in l_somm:
        etat[s]=0

    print "parcours en profondeur"
    print "à partir du premier sommet"
    for s in l_somm:
        if etat[s]==0:
            print RechProf(G,s,etat)


    etat={}
    for s in l_somm:
        etat[s]=0

    print "parcours en largeur"
    print "à partir du premier sommet"
    for s in l_somm:
        if etat[s]==0:
            print RechLarg(G,s,etat)


#### TP 3 ##############################################

S=[0,1,2,3,4,5] ## liste des sommets
L=[[0,1,3],[0,3,1],[0,5,5],[1,2,1],[1,5,1],[2,3,2],[3,1,3],[4,3,3],[5,4,2],[5,3,2]]
## liste des arretes : [depart,arrivée,distance]
def creerListeAdjacenceValuee(S,L):
    G={}
    Gdist={}
    for x in S:
        G[x]=[]
        Gdist[x]=[]
        for y in L:
            if x==y[0]:
                G[x].append(y[1])
                Gdist[x].append(y[2])


## Algo Djkstra : renvoie le dictionnaire des plus courtes distances de s0 vers les autres sommets
G={0: [1, 3, 5], 1: [2, 5], 2: [3], 3: [1], 4: [3], 5: [4, 3]}
Gdist={0: [3, 1, 5], 1: [1, 1], 2: [2], 3: [3], 4: [3], 5: [2, 2]}
s0=0

def Dijkstra(G,Gdist,s0):
    dic={}
    T=[] ## liste des sommets visités
    inf=999
    Gk=G.keys()
    i=0
    for x in Gk:
        if x==s0:
            dic[x]=0
        elif x in G[s0]:
            dic[x]=Gdist[s0][i]
            i+=1
        else:
            dic[x]=inf
    T+=[s0]
    Gk.remove(s0)
    print dic
    ## dic est initialisé

    while len(Gk)>0:
    
        y=inf
        for x in Gk:
            y=min(dic[x],y)
            if y==dic[x]:
                z=x
        T+=[z]
        Gk.remove(z)
        print T
        
        ## mise a jour de dic avec z (dernier element ajouté a T):
        for x in G[z]:
            if dic[x]>dic[z]+Gdist[z][G[z].index(x)]:
                dic[x]=dic[z]+Gdist[z][G[z].index(x)]
        print dic
    return dic

##dic=Dijkstra(G,Gdist,s0)
##print dic

## Algo de dikstra complet !
## calcule aussi le tableau père

def Algo(G,Gdist,s0):
    dic={}
    pere={}
    T=[] ## liste des sommets visités
    inf=999
    Gk=G.keys()
    i=0
    for x in Gk:
        if x==s0:
            dic[x]=0
            pere[x]=-1
        elif x in G[s0]:
            dic[x]=Gdist[s0][i]
            pere[x]=s0
            i+=1
        else:
            dic[x]=inf
            pere[x]=-1
    T+=[s0]
    Gk.remove(s0)
    ## dic est initialisé
    while len(Gk)>0:
    
        y=inf
        for x in Gk:
            y=min(dic[x],y)
            if y==dic[x]:
                z=x
        T+=[z]
        Gk.remove(z)
        
        ## mise a jour de dic avec z (dernier element ajouté a T:
        for x in G[z]:
            if dic[x]>dic[z]+Gdist[z][G[z].index(x)]:
                dic[x]=dic[z]+Gdist[z][G[z].index(x)]
                pere[x]=z
    res=[dic,pere]
    return res

res=Algo(G,Gdist,s0)
## print res

def reconstituerchemin(pere,x):
    L=[x]
    while pere[x]!=-1:
        L=[pere[x]]+L
        x=pere[x]
    return L

pere=res[1]
x=4
l=reconstituerchemin(pere,x)
##print pere
##print l



####################################################
# Execution 
####################################################

if __name__ == "__main__":

## 1er exemple
    l_sommet=range(1,6)
    l_arrete=[[1,2,100],
              [1,3,30],
              [1,5,10],
              [3,2,60],
              [3,4,20],
              [4,2,10],
              [5,4,50]]
    
    G_Gdist=creerListeAdjacenceValuee(l_sommet,l_arrete)
    print G_Gdist
    
    G=G_Gdist[0]
    Gdist=G_Gdist[1]
    
    print  Dijkstra(G,Gdist,1)
    
    l_dist_pere=DijkstraPere(G,Gdist,1)
    print l_dist_pere[0]
    print l_dist_pere[1]
    
    print reconstituerChemin(l_dist_pere[1],2)

## 2nd exemple
    l_sommet=range(6)
    l_arrete=[[0,1,3],[0,3,1],[0,5,5],
              [1,2,1],[1,5,1],
              [2,3,2],
              [3,1,3],
              [4,3,3],
              [5,3,2],[5,4,2]]
    
    G_Gdist=creerListeAdjacenceValuee(l_sommet,l_arrete)
    print G_Gdist
    
    G=G_Gdist[0]
    Gdist=G_Gdist[1]
    
    print  Dijkstra(G,Gdist,0)
    
    l_dist_pere=DijkstraPere(G,Gdist,0)
    print l_dist_pere[0]
    print l_dist_pere[1]
    
    print  reconstituerChemin(l_dist_pere[1],2)

          
## 3eme exemple
    l_sommet=range(4)
    l_arrete=[[0,2,1],
              [1,0,1],[1,3,3],
              [2,1,2],[2,3,4],
              [3,1,5]]
    
    G_Gdist=creerListeAdjacenceValuee(l_sommet,l_arrete)
    print G_Gdist
    
    G=G_Gdist[0]
    Gdist=G_Gdist[1]
    
    print  Dijkstra(G,Gdist,0)
    
    l_dist_pere=DijkstraPere(G,Gdist,0)
    print l_dist_pere[0]
    print l_dist_pere[1]
    
    print reconstituerChemin(l_dist_pere[1],2)


#### TP 4 ##############################################

##liste des peres correspondant aux composantes connexes !
dica={1:[2,6,9],2:[6,10],3:[11],4:[5,7,12],5:[8,13],6:[9,10],7:[8,12],8:[13],9:[10],12:[13]}
G={1:[2,6,9],2:[1,6,10],3:[11],4:[5,7,12],5:[4,8,13],6:[1,2,9,10],7:[4,8,12],8:[5,7,13],9:[1,6,10],10:[2,6,9],12:[4,7,13],11:[3],13:[5,8,12]}

pere={}
for i in range (1,14):
    pere[i]=-1
##print pere

def fusionrecherche(pere,dica):
    for k in pere:
        if k in dica:
            l=dica[k]
            for el in l:
                if pere[k]!=-1:
                    pere[el]=pere[k]
                else:
                    pere[el]=k
    return pere
##fusionrecherche(pere,dica)
##print pere

def lista(G): ## version avec les doublons dans les aretes
    L=[]
    for s in G :
        n=len(G[s])
        for i in range (n):
            if [G[s][i],s] not in L:
                L+=[[s,G[s][i]]]
    return L

def racine(pere,s):
    k=s
    while pere[k]!=-1:
        k=pere[k]
    return k

def composanteconnexe(G):
    dicpere={}
    for i in G.keys():
        dicpere[i]=-1
    for s in lista(G):
        if racine(dicpere,s[0])!=racine(dicpere,s[1]):
            dicpere[racine(dicpere,s[1])]=racine(dicpere,s[0])
    return dicpere


# -*- coding:iso-8859-1 -*-

def ListeArretes(G):
    lk=G.keys()
    lk.sort()

    la=list()

    for x in lk:
        for y in G[x]:
            if y>x:
                la.append([x,y])
    return la

def Racine(pere,s):
    res=s
    while pere[res]!=-1:
        res=pere[res]
    return res

# la meme en recursive
def Racine_r(pere,s):
 if pere[s]==-1:
     return s
 return Racine_r(pere,pere[s])

def ComposanteConnexe(G):
    # liste des arretes
    la=ListeArretes(G)

    # initialisation du dictionnaire pere
    pere=dict()
    for s in G.keys():
        pere[s]=-1

    # boucle principale
    for a in la:
        r_x=Racine(pere,a[0])
        r_y=Racine(pere,a[1])
        if r_x!=r_y:
            pere[r_y]=r_x
    
    return pere
    


####################################################
# Execution 
####################################################

if __name__ == "__main__":

## 1er exemple
    G1={1:[2,6],2:[1,6,7],3:[4,8],4:[3,5,8],5:[4],
       6:[1,2],7:[2],8:[3,4],9:[10],10:[9]}
    
    print  ListeArretes(G1)


    pere={1:-1,2:1,3:-1,4:3,5:4,6:1,7:1,8:3,9:-1,10:9}

    for i in range(1,11):
        print "s=",i," Racine(pere,s)=",Racine(pere,i)
        print "s=",i," Racine_r(pere,s)=",Racine_r(pere,i)

    print ComposanteConnexe(G1)
        
## 2eme exemple
    G2={1:[2,6,9],2:[1,6,10],3:[11],4:[5,7,12],5:[4,8,13],
        6:[1,2,9,10],7:[4,8,12],8:[5,7,13],9:[1,6,10],10:[2,6,9],
        11:[3],12:[4,7,13],13:[5,8,12]}
    
    print ListeArretes(G2)

    print ComposanteConnexe(G2)


#### TP noté ##############################################

G1={0:[5],1:[0,5],2:[1,4],3:[2],4:[1,3],5:[2,4]}

def GrapheInverse(G): ## fct qui donne le dic des predecesseurs
    ginv={}
    for cle in G:
        ginv[cle]=[]
    for cle in G:
        for val in G[cle]:
            ginv[val]+=[cle]
    return ginv
gi1=GrapheInverse(G1)

def TestEulerien(G,Ginv):
    for cle in G:
        if len(G[cle])!=len(Ginv[cle]):
            return False
    return True

## squelette vers un sommet donnée (sommet d'arrivée)
## parcours en profondeur a partir de s dans Ginv
## == Chaine Eulerienne

s=3
etat=dict()
for i in G1.keys():
    etat[i]=0
    
def RechProf(G,s,etat):
    sommet=[s]
    etat[s]=1
    for el in G[s]:
        if etat[el]==0:
            etat[el]=1
            sommet+=RechProf(G,el,etat)
    return sommet

##res1=RechProf(gi1,s,etat)
##print res1

arete=[]
def RechProfmodif(G,s,etat,arete):
    etat[s]=1
    for el in G[s]:
        if etat[el]==0:
            arete.append([s,el])
            etat[el]=1
            RechProfmodif(G,el,etat,arete)
    return arete
## are1=RechProfmodif(gi1,s,etat,arete)
## [[3, 4], [4, 2], [2, 5], [5, 0], [0, 1]]

def squelette(G,aretes,u):
    ginv=GrapheInverse(G)
    dic={}
    for el in arete:
        dic[el[1]]=el[0]
    return dic

G1={0:[5],1:[0,5],2:[1,4],3:[2],4:[1,3],5:[2,4]}	
##Gsquel1=squelette(G1,are1,3)
## {0: 5, 1: 0, 2: 4, 4: 3, 5: 2}

def RearrangementAretes(G,Gsquel):
	for s in Gsquel:
		if G[s]>1:
			G[s].append(G[s][0])
			G[s].remove(G[s][0])
	return G
##G11=RearrangementAretes(G1,Gsquel1)

def CycleEulerien(G,u):
    # Initialisation
    l_somm=G.keys()
    l_somm.sort()
    # on met tous les sommet dans un état non visité 
    parcouru=dict()
    for s in l_somm:
        parcouru[s]=[0]*len(G[s])
    
    #la liste resultat
    resultat=list()
    
    # Construction du cycle 
    s=u
    cont=True
    while cont:
        m=len(G[s])
        j=0
        flag=True
        while flag and j<m:
            if parcouru[s][j]==0:
                parcouru[s][j]=1
                t=G[s][j]
                resultat.append([s,t])
                s=t                
                flag=False
            else:
                j=j+1
        if flag:
            cont=False
            if s==u:
                return resultat
            else:
                print "Erreur : impossible de trouver un cycle eulerien"

res=CycleEulerien(G1,s)
print res
## [[3, 2], [2, 1], [1, 0], [0, 5], [5, 2], [2, 4], [4, 1], [1, 5], [5, 4], [4, 3]]


#############
## TP note ##
#############
# -*- coding:iso-8859-1 -*-

# Structures discretes : TP note 20112012

# Definitions

# Exercice 1

def GrapheInverse(G):
     # Intialisation
    ginv=dict()
    l_som=G.keys()
    l_som.sort()
    for i in l_som:
        ginv[i]=list()
    # Construction des listes d'adjacence opposees
    for i in l_som:
        for j in G[i]:
            ginv[j].append(i)
    return ginv


def TestEulerien(G,Ginv):
    for s in G.keys():
        if len(G[s]) != len(Ginv[s]):
            return False
    return True

# Exercice 2

def ParcoursProfondeur(G,s,etat,aretes):
    etat[s]=1
    for t in G[s]:
        if etat[t]==0:
            aretes.append([s,t])
            ParcoursProfondeur(G,t,etat,aretes)

def Squelette(G,aretes,u):
    squel=dict()
    l_som=G.keys()
    l_som.sort()
    for i in l_som:
        squel[i]=list()
    for a in aretes:
        squel[a[1]].append(a[0])
    return squel




# Exercice 3

def RearrangementAretes(G,Gsquel):
    l_som=G.keys()
    l_som.sort()
    for s in l_som:
        t=Gsquel[s]
        if t != []:
            G[s].remove(t[0])
            G[s].append(t[0])



# Exercice 4

def CycleEulerien(G,u):
    # Initialisation
    l_somm=G.keys()
    l_somm.sort()
    # on met tous les sommet dans un état non visité 
    parcouru=dict()
    for s in l_somm:
        parcouru[s]=[0]*len(G[s])
    
    #la liste resultat
    resultat=list()
    
    # Construction du cycle 
    s=u
    cont=True
    while cont:
        m=len(G[s])
        j=0
        flag=True
        while flag and j<m:
            if parcouru[s][j]==0:
                parcouru[s][j]=1
                t=G[s][j]
                resultat.append([s,t])
                s=t                
                flag=False
            else:
                j=j+1
        if flag:
            cont=False
            if s==u:
                return resultat
            else:
                print "Erreur : impossible de trouver un cycle eulerien"

                
# Programme principal


# Exercice 1
# un exemple avec le graphe G1

G1={0:[5],1:[0,5],2:[1,4],3:[2],4:[1,3],5:[2,4]}

G1inv=GrapheInverse(G1)

print "Exercice 1"
print "G1 : ", G1
print "Graphe inverse"
print "G1inv : ", G1inv
print "Test de condition d'existence de cycle Eulerien"
print "Resultat du test : ", TestEulerien(G1,G1inv)

G2={0:[1,4],
    1:[4],
    2:[0,3],
    3:[0,6],
    4:[3,7],
    5:[2],
    6:[2,5],
    7:[6]}

G2inv=GrapheInverse(G2)

print "G2 : ", G2
print "Graphe inverse"
print "G2inv : ", G2inv
print "Test de condition d'existence de cycle eulerien"
print "Resultat du test : ", TestEulerien(G2,G2inv)
 

# Exercice 2

# un exemple avec le graphe G1
# on trie la liste des sommets
l_somm=G1.keys()
l_somm.sort()

# on met tous les sommet dans un état non visité 
etat={}
for s in l_somm:
    etat[s]=0

#initialisation de arete
aretes=list()
#sommet de départ
u=3

print "Exercice 2"
print "Construction du squelette "
print "Sommet de depart :",u
ParcoursProfondeur(GrapheInverse(G1),u,etat,aretes)
print "Aretes du parcours du graphe inverse"
print aretes
print

print "Arbre de chemin rentrant vers le sommet :", u
Gsquel1=Squelette(G1,aretes,u)
print Gsquel1


# avec le graphe G2
# on trie la liste des sommets
l_somm=G2.keys()
l_somm.sort()

# on met tous les sommet dans un état non visité 
etat={}
for s in l_somm:
    etat[s]=0

#initialisation de arete
aretes=list()
#sommet de départ
u=3

print "Exercice 2"
print "Construction du squelette "
print "Sommet de depart :",u
ParcoursProfondeur(GrapheInverse(G2),u,etat,aretes)
print "Aretes du parcours du graphe inverse"
print aretes
print

print "Arbre de chemin rentrant ver le sommet :", u
Gsquel2=Squelette(G2,aretes,u)
print Gsquel2



# Exercice 3
# un exemple avec le graphe G1
print "Exercice 3"
print "Rearrangement des aretes"
print "Le graphe G1 avant rearrangement"
print G1
print "Le graphe G1 apres rearrangement"
RearrangementAretes(G1,Gsquel1)
print G1 


# avec le graphe G2
print "Exercice 3"
print "Rearrangement des aretes"
print "Le graphe G2 avant rearrangement"
print G2
print "Le graphe G1 apres rearrangement"
RearrangementAretes(G2,Gsquel2)
print G2 

# Exercice 4
# un exemple avec le graphe G1
print "Exercice 4"
print "Calcul d'un cycle eulerien"
cycle=CycleEulerien(G1,u)
print cycle

# avec le graphe G2
print "Exercice 4"
print "Calcul d'un cycle eulerien"
cycle=CycleEulerien(G2,u)
print cycle



################
##            ##
##   FIN      ##
## Licence L3 ##
##            ##
################

################
##            ##
##   DEBUT    ##
## Master M1  ## S1
##            ##
################

## POO Python 

## TP 1 ############################################
#### Lecture d'un fichier - image #### 
## Ex ## baleine.pgm ##
def dimension(img):
    fichier = open(img, "r")
    ligne=fichier.readline()
    ligne=fichier.readline()
    while ligne[0]=='#': ## la ligne est un commentaire
        ligne=fichier.readline() ## on passe a la ligne d'apres
    l=ligne.split() ## separe chaque mot en fct des espaces -> dans une liste
    print "la largueur de l'image "+str(img)+" est "+l[0]+" sa hauteur est "+l[1]
    fichier.close()
    
dimension('baleine.pgm')
## la largueur de l'image baleine.pgm est 430 sa hauteur est 305

#### Ecriture d'un fichier - image ####
def negatif(image):
    fichier= open(image,"r") ## ouverture du fichier image
    fichier2=open(image[:-4]+'neg.pgm','w')
    tamp=fichier.readline() ## parcours la ligne de P2 (saut de ligne)
    fichier2.write(tamp) ## ecriture de la ligne dans le fichier2
    tamp=fichier.readline() ## parcours la ligne de P2 (saut de ligne)
    while tamp[0] =='#': ## tant qu'il y a # au debut, on saute les lignes
        fichier2.write(tamp)
        tamp=fichier.readline()
    fichier2.write(tamp)
    tamp=fichier.readline()
    fichier2.write(tamp)
    tamp=fichier.readline()
    for ligne in fichier:
        val=int(ligne.split()[0])
        fichier2.write(str(255-val)+'\n') ## couleur inverse : 255 - valeur
    fichier.close()
    fichier2.close()

negatif('baleine.pgm')


## Ex 1

## 1)
def compte (ch,c):
    cpt=0
    for l in ch:
        if l==c:
            cpt+=1
    return cpt

## 2)
def miroir (ch):
    res=""
    for l in ch:
        res=l+res
    return res

ch="coucou"
c="c"
print compte(ch,c)
print miroir(ch)

## Ex 2

## 3)
def moyenne (listeNb):
    return sum(listeNb)/len(listeNb)

## 4)
def maxi (lis):
    return max(lis)

## 5)
def indexMax (lis):
    return lis.index(max(lis))

listeNb=[2,8,5]
print moyenne(listeNb)
print maxi(listeNb)
print indexMax(listeNb)

## Ex 3

europe = {'Estonie': ('Tallinn', 1.4), 'Portugal': ('Lisbonne', 10.1),
'Pologne': ('Varsovie', 38.6), 'Allemagne': ('Berlin', 82.4),
'Italie': ('Rome', 57.9), 'Lituanie': ('Vilnius', 3.6),
'Belgique': ('Bruxelles', 10.3), 'Lettonie': ('Riga', 2.3),
'Danemark': ('Copenhague', 5.4), 'Autriche': ('Vienne', 8.1)}

## 6) dico[cle][indice]
print europe['Lituanie'][0]
print europe['Lituanie'][1]
cap=[]
for e in europe:
    cap+=[europe[e][0]]
print cap
europe['France']=('Paris',66)
print europe

## 7)
def capitale(dico,pays):
    if pays in dico:
        return dico[pays][0]
    return "Ce pays n'est pas dans le dico"

print capitale(europe,'France')

## 8)
def popTotale(dico):
    cpt=0
    for pays in dico:
        cpt+=dico[pays][1]
    return cpt

print popTotale(europe)

## 9)
def fct9(dico,nb):
    lis=[]
    for p in dico:
        if dico[p][1]>nb:
            lis.append(p)
    return lis

print fct9(europe,30)

## 10)
def pluspetit(dico):
    res=europe.keys()[0]
    for p in dico:
        if dico[p][1]<dico[res][1]:
            res=p
    return res

print pluspetit(europe)
## min([el[1] for el in europe.values()])
## 1.4

## Ex 4 ## baleine.pgm

## 11)
def dimension(img):
    fichier = open(img, "r")
    ligne=fichier.readline()
    ligne=fichier.readline()
    while ligne[0]=='#':
        ligne=fichier.readline()
    l=ligne.split()
    print "la largueur de l'image "+str(img)+" est "+l[0]+" sa hauteur est "+l[1]       
    fichier.close()
    
dimension('baleine.pgm')
## la largueur de l'image baleine.pgm est 430 sa hauteur est 305

## 12)

def negatif(image):
    fichier= open(image,"r")#ouverture du fichier image
    fichier2=open(image[:-4]+'neg.pgm','w')
    tamp=fichier.readline()#parcours la ligne de P2 (saut de ligne)
    fichier2.write(tamp)
    tamp=fichier.readline()#parcours la ligne de P2 (saut de ligne)
    while tamp[0] =='#': #tant qu'il y a # au debut on les saute
        fichier2.write(tamp)
        tamp=fichier.readline()
    fichier2.write(tamp)
    tamp=fichier.readline()
    fichier2.write(tamp)
    tamp=fichier.readline()
    for ligne in fichier:
        val=int(ligne.split()[0])
        fichier2.write(str(255-val)+'\n')
    fichier.close()
    fichier2.close()

negatif('baleine.pgm')

## Ex 5 :
ch="les cours ont repris le 5, les cours redemarrent"

## 13.
from string import ascii_letters
def chaine(ch):
    l=ch.split()
    return l
print chaine(ch)

## 14.
def dico(ch):
    l=chaine(ch)
    d={}
    for el in l:
        if el in d:
            d[el]+=1
        else:
            d[el]=1
    return d
print dico(ch)

## 15.
def nplusfreq(ch,n):
    c=""
    for car in ch:
        if car in ascii_letters:
            c+=car.lower()
        else:
            car=" "
            c+=car
    d=dico(c)
    val=d.values()
    val.sort()
    nval=val[-n:] ## on prend les n derniere valeurs
    res={}
    for el in d:
        if d[el] in nval:
            res[el]=d[el]
    return res
print nplusfreq(ch,3)

## 16.

def motFrequents(f,n):
    fic= open(f,"r")
    lignes=fic.read()
    d=nplusfreq(lignes,n)
    fic.close()
    return d

print motFrequents('/usr/lib/python2.7/random.py',5)
print motFrequents('/usr/lib/python2.7/filecmp.py',5)

## TP2 ########################################################
## les Classes : 
class Compteur(object):
    def __init__(self,val=0): ## constructeur
        self.valeur=val
    def __repr__(self): ## permetera d'afficher une instance
        return str(self.valeur) 

## accesseur d'un atribut prive/brouille
def gatAge(self):
    return self.__age

## Ex 1 :
class Compteur(object):
    
    def __init__(self,val=0):
        self.valeur=val

    def __repr__(self):
        return str(self.valeur)

    def incremente(self):
        self.valeur+=1
    def decremente(self):
        self.valeur-=1

    def zero(self):
        return self.valeur==0

c=Compteur(5)
c.incremente()
c
c.zero()


## Ex 2 :
class Intervalle(object):

    def __init__(self,inf,sup):
        if inf<sup:
            self.inf=inf
            self.sup=sup
        else:
            self.inf=sup
            self.sup=inf
    
    def __repr__(self):
        return "["+str(self.inf)+","+str(self.sup)+"]"

    def milieu(self):
        "calcule le milieu d'un intervalle"
        return (self.sup+self.inf)/2.
    
    def longueur(self):
        "calcule la longueur d'un intervalle"
        return self.sup-self.inf

    def enveloppe(self,autre):
        """ retourne une instance de Intervalle
        correspondant au plus petit intervalle contenant
        self et autre
        """
        i=Intervalle(min(self.inf,autre.inf),max(self.sup,autre.sup))
        return i

    def rencontre(self,autre):
        "Precise si les intervalles s'intersectionnent"
        if self.inf<autre.inf:
            return self.sup>autre.inf
        return self.inf<autre.sup
    
    
i1=Intervalle(5,7)
i2=Intervalle(7,5)
print i1
print i2
i3=Intervalle(6,8)
print i3
print i3.milieu()
print i3.longueur()
print i1.enveloppe(i3)
print i1.rencontre(i3)

## Ex3 :
help(Intervalle)
dir(Intervalle) ## methods
i3.__dict__ ## le dico des attributs de i3

## Ex4 :
## attributs : can, coordonées x, y, l'orientation (deg), la couleur du crayon et si levé ou baissé.
## methodes : baisser ou lever le crayon, avancer, tourner, changer la couleur.
## cf tortue.py 




## TP3 Tortue #########################################################
from Tkinter import *      # la bibliotheque graphique 
class Tortue(object):
    can=None # la zone de dessin
    def __init__(self,color='white'):
        self.color=color
        self.reset()
    ## .... plein d'autre fonction
class Application(Tk): # la fenetre 
    def __init__(self):
        Tk.__init__(self)
        self.title('Caroline')
        # Creation de la zone de dessin et placement dans le fenetre
        Tortue.can=Canvas(self,width=600,height=600,bg='black')
        Tortue.can.grid()

if __name__=='__main__':
    app=Application()
    app.mainloop()
        

## TP3
## Ex1
class LSysteme(object):
    def __init__(self,axiome,regles):
        self.axiome=axiome
        self.regles=regles
        self.nbEtape=0
        self.mot=axiome

    def reset(self):
        self.nbEtape=0
        self.mot=self.axiome

    def etape(self):
        self.nbEtape+=1
        temp=''
        for car in self.mot:
            if car in self.regles:
                temp+=self.regles[car]
            else:
                temp+=car
        self.mot=temp

    def getMot(self):
        return self.mot

    def genere(self,n):
        self.reset()
        for i in range (n):
            self.etape()
        return self.mot


if __name__=='__main__':
    ## Question 2:
    ax=LSysteme('fx',{'f' : '', 'x' : '-fx++fy-', 'y' : '+fx--fy+'})
    print ax.genere(3)
    mot=ax.genere(2)


## TP4 ## image #####################################################
def filtre(self,predicat):
    return [el for el in self if predicat(el)] ## construction

## POO4
## ex1 :

class Lily (list):

    def miroir(self):
        res=[]
        for el in self:
            res=[el]+res
        return res

    def tous(self,predicat):
        
        for el in self:
            if not predicat(el):
                return False
        return True

    def filtre(self,predicat):
        return [el for el in self if predicat(el)]

    def index(self,value):
        i=0
        for el in self:
            if el == value  :
                return i
            i+=1
        return -1
        

##ls=Lily([7,3,15,0,3,8,2])
##print ls
##print ls.miroir()
##def pair(x):
##    return x%2==0
##print ls.tous(pair)
##print ls.filtre(pair)
##print ls.index(10)
##print list.index(ls,10) ## utilise la methode index de list

## ex2
# -*- coding:utf-8 -*-

class Image(object):
    def __init__(self,nomFic):
        ext=nomFic.split('.')[-1]
        if ext != 'pgm':
            raise UserWarning("mauvais format")
        source=open(nomFic,'r')
        source.readline()
        tamp=source.readline()
        while tamp[0]=='#':
            tamp=source.readline()
        tamp=tamp.split()
        self.larg=int(tamp[0])
        self.htr=int(tamp[1])

        self.tab=[[int(source.readline()[:-1]) for col in range(self.larg)] for lig in range(self.htr)]

        source.close()


    def getPixel(self,i,j):
        pix=self.tab[i][j]
        return pix

    def setPixel(self,i,j,val):
        self.tab[i][j]=val

    def negatif(self):
        for i in range (self.htr):
            for j in range (self.larg):
                self.tab[i][j]=255-self.tab[i][j]


    def symVertical(self):
        pass



if __name__ == '__main__':
    im=Image('baleine.pgm')
    print im.getPixel(0,0)
    print im.setPixel(1,3,5)
    im.negatif()


## TP5 #################################################################
## Compte
class Compte(object):
    nbComptes=0
    def __init__(self,nom):
        self.nom=nom
        self.num=Compte.nbComptes
        self.solde=0
        Compte.nbComptes+=1
class CompteDecAut(Compte): ## decouvert autorise ## ##  Heritage ## 
    def __init__(self,nom,montant):
        Compte.__init__(self,nom)
        self.m=montant

## TP5

## ex1

class Compte(object):
    nbComptes=0
    def __init__(self,nom):
        self.nom=nom
        self.num=Compte.nbComptes
        self.solde=0
        Compte.nbComptes+=1

    def __repr__(self):
        return str(self.nom, self.num, self.solde)

    def verser(self,som):
        self.solde+=som

    def retirer(self,som):
        if som<self.solde:
            self.solde-=som
        else:
            print 'le solde est insuffisant'

class CompteDecAut(Compte):

    def __init__(self,nom,montant):
        Compte.__init__(self,nom)
        self.m=montant

    def retirer(self,som):
        if som<self.solde+self.m:
            self.solde-=som
        else:
            print 'le solde est insuffisant'

class CompteRemunere(Compte):

    def __init__(self,nom,taux):
        Compte.__init__(self,nom)
        self.tx=taux

    def calculeInterets(self):
        i=self.solde*(self.tx/100.)
        self.solde+=i


## ex2

class ReseauSoc(dict):
    def estMembre(self,pers):
        return pers in self

    def nbConnaissance(self,pers):
        return len(self[pers])

    def amis(self,pers1,pers2):
        return (pers1 in self[pers2] and pers2 in self[pers1])

    def connaissancesCommunes(self,pers1,pers2):
        res=[]
        for p in self[pers1]:
            if p in self[pers2]:
                res.append(p)
        return res

    def popularite(self,pers):
        cpt=0
        for p in self:
            if pers in self[p]:
                cpt+=1
        return cpt

    def estCelebre(self,pers):
        return (self.popularite(pers)>len(self)/2.)

    def ajoute(self,pers1,pers2):
        self[pers1].append(pers2)

    
if __name__ == '__main__':
##    c=Compte('Paul')
##    c.affiche()
##    c2=Compte('Pierre')
##    c2.affiche()
##    c.verser(200)
##    c.retirer(100)
##    c2.retirer(10)
##    c.affiche()
##    c2.affiche()
##    c3=CompteDecAut('Joe',50)
##    c4=CompteRemunere('Boby',5)
##    c3.verser(20)
##    c3.retirer(30)
##    c3.affiche()
##    c4.verser(100)
##    c4.calculeInterets()
##    c4.affiche()
    Res=ReseauSoc({'a':['a','b'],'b':['a','c','d','e'],'c':['b'],'d':['b','e'],'e':['b','d']})
    print Res.estMembre('a')
    print Res.estMembre('f')
    print Res.nbConnaissance('b')
    print Res.amis('a','b')
    print Res.connaissancesCommunes('b','d')
    print Res.popularite('a')
    print Res.estCelebre('b')
    print Res.estCelebre('c')
    Res.ajoute('a','d')
    print Res
    print Res.amis('a','d')
    

## TP6 : Interface : VUE MACHINE / VUE CHAINE #############################
## traitements : piece dessine/modele

# -*- coding: utf-8 -*-
## TP6


from random import *
from math import *

##################### PIECE
class Piece(object):
    "classe pour creer une piece"
    def __init__(self,can):
        self.can=can
        self.generer()
        self.dessinePiece()

    def generer(self):
        raise NotImplementedError

    def __eq__(self,autre):
        " on redefinit la methode qui teste l'egalité "
        if self.trait!=autre.trait:
            return False
        for i in range(4):
            if not (self.trou[i]>1 and autre.trou[i]>1) or not(self.trou[i]<1 and autre.trou[i]<1):
                return False
        pair=True
        pairautre=True
        for i in range(4):
            if self.trou[i]%2!=0:
                pair=False
                break
        for i in range(4):
            if autre.trou[i]%2!=0:
                pairautre=False
                break
        return pair==pairautre
                

    def dessinePiece(self):
        "dessin de la pièce sur le canevas"
        t=16
        ray=3*t
        xc,yc=4*t,4*t
        ang=pi/8
        sommets=[]
        milSommets=[]
        for i in range(1,16,2):
            sommets.append(xc+ray*cos(i*ang))
            sommets.append(yc+ray*sin(i*ang))
            milSommets.append(xc+ray*(cos(i*ang)+cos((i-2)*ang))/2)
            milSommets.append(yc+ray*(sin(i*ang)+sin((i-2)*ang))/2)

        self.can.create_polygon(sommets,fill='blue')
        for i in range(4):
            if  self.trait[i]>0:
                self.can.create_line(milSommets[2*i],milSommets[2*i+1],milSommets[2*i+8],milSommets[2*i+9],width=4*self.trait[i]-1)

        r=7
        for i in range(4):
            if self.trou[i]%2==1:
                self.can.create_oval(xc-r,yc-r,xc+r,yc+r,fill='red')
                break
        for i in range(4):
            if self.trou[i]>1:
                xd,yd,xf,yf=milSommets[2*i],milSommets[2*i+1],milSommets[2*i+8],milSommets[2*i+9]
                x,y=xd+(xf-xd)/6,yd+(yf-yd)/6
                self.can.create_oval(x-r,y-r,x+r,y+r,fill='red')
                x,y=xd+5*(xf-xd)/6,yd+5*(yf-yd)/6
                self.can.create_oval(x-r,y-r,x+r,y+r,fill='red')
                
class PieceModele(Piece):
    " Piece modele est une piece aleatoire "
    def generer(self):
        self.trou=[randint(0,3) for i in range(4)] ## randrange(4)
        self.trait=[randrange(4) for i in range(4)]

class PieceUsine(Piece):
    " Piece usine est construite par l'utilsateur "
    def generer(self):
        self.trou=[0,0,0,0]
        self.trait=[0,0,0,0]

    def trouer(self,nb):
        if self.trou[0]==0 and nb==0:
            self.trou[0]+=nb
        elif self.trou[0]!=nb:
            self.trou[0]=3
            
    def tracer(self,epaisseur):
        self.trait[0]=max(self.trait[0],epaisseur)

    def tourner(self,angle):
        self.trait=self.trait[-angle:]+self.trait[:-angle]
        self.trou=self.trou[-angle:]+self.trou[:-angle]

####################exo 2 MACHINE
class Machine (object):
    def __init__(self,conf=0):
        self.conf=conf

    def setConf(self,val):
        self.conf=val

    def usiner(self,piece):
        raise NotImplementedError

class MPassive(Machine):
    def usiner(self,piece):
        pass
            
class MTrou(Machine):
    def usiner(self,piece):
        piece.trouer(self.conf)

class MTrait(Machine):
    def usiner(self,piece):
        piece.tracer(self.conf)

class MRoue(Machine):
    def usiner(self,piece):
        piece.tourner(self.conf)
 
#####################exo 3 CHAINE DE MONTAGE

class Chaine (list): #liste de machines

    def __init__(self,nb=12): ##permet d'initialiser par defaut le nombre de machine=12 -> au + 4 MTRou, 4 MTrait et 3 MRoue
       list.__init__(self,[MPassive(0) for i in range(nb)])

    def setMach(self,i,typeM=3,conf=0): ##permet d'instancier la i-eme machine selon un type et une configuration desires --> type 3 = mpassive
        if typeM==3:
            self[i]=MPassive(conf)
        elif typeM==2:
            self[i]=MRoue(conf)
        elif typeM==1:
            self[i]=MTrait(conf)
        elif typeM==0:
            self[i]=MTrou(conf)
            
    def setConf(self,i,conf):
        self[i].setConf(conf)
        
    def usiner(self,piece): ## permet d'unsiner une piece donnee
        for machine in self:
            machine.usiner(piece)

    def raz(self): ## permet de reinitialiser la chaine avec des machines de la classe MPassive
        for i in range(len(self)):
            self.setMach(i)
        
#####################EXO 4 INTERFACE GRAPHIQUE
            ## on passe
#####################EXO 5
## commanter le fichier avec la commande epydoc.


if __name__== '__main__':
    from Tkinter import *
    fen=Tk()
    can1=Canvas(fen,bg='light yellow')
    can1.grid()
    m=PieceModele(can1)
    can2=Canvas(fen,bg='light yellow')
    can2.grid()
    p=PieceUsine(can2)
    p.trouer(2)
    p.tourner(1)   
    p.tracer(2)
    p.dessinePiece()
    can3=Canvas(fen,bg='light yellow')
    can3.grid()
    p3=PieceUsine(can3)
    ch=Chaine(4)
    ch.setMach(0,0,2)
    ch.setMach(1,0,1)
    ch.setMach(2,1,1)
    ch.setMach(3,2,1)
    ch.usiner(p3)

    p3.dessinePiece()
    fen.mainloop()
    

## TP7 :  #########################################################
# commenter les fichiers. faire une doc

## TP8 ###########################################################
## Redefinition des operateurs
class Horloge(object):

    def __init__(self,heure=0,minute=0,seconde=0):
        self.seconde=seconde%60
        minute=minute+(seconde-self.seconde)//60
        self.minute=minute%60
        self.heure=heure+(minute-self.minute)//60

    def __repr__(self):
        return str(self.heure)+'h'+str(self.minute)+'m'+str(self.seconde)+'s'

    def __add__(self,autre):
        h=self.heure+autre.heure
        m=self.minute+autre.minute
        s=self.seconde+autre.seconde
        res=Horloge(h,m,s)
        return res

    def __mul__(self,k): ## l'objet est a gauche
        h=k*self.heure
        m=k*self.minute
        s=k*self.seconde
        res=Horloge(h,m,s)
        return res
    __rmul__ = __mul__
    
## complexe : autre = a + i * b
d=float(autre.a**2+autre.b**2) ## la norme au carre
## julia.py : complexe


# -*- coding:utf-8  -*-
## TP8 Redefinition des opérateurs

## ## ex1 une classe Horloge
class Horloge(object):

    def __init__(self,heure=0,minute=0,seconde=0):
        self.seconde=seconde%60
        minute=minute+(seconde-self.seconde)//60
        self.minute=minute%60
        self.heure=heure+(minute-self.minute)//60

    def __repr__(self):
        return str(self.heure)+'h'+str(self.minute)+'m'+str(self.seconde)+'s'

    def __add__(self,autre):
        h=self.heure+autre.heure
        m=self.minute+autre.minute
        s=self.seconde+autre.seconde
        res=Horloge(h,m,s)
        return res

    def __sub__(self,autre):
        h=self.heure-autre.heure
        m=self.minute-autre.minute
        s=self.seconde-autre.seconde
        res=Horloge(h,m,s)
        return res

##    def __rmul__(self,k): ## l'objet est a droite de l'operateur
##        h=k*self.heure
##        m=k*self.minute
##        s=k*self.seconde
##        res=Horloge(h,m,s)
##        return res
    
    def __mul__(self,k): ## l'objet est a gauche
        h=k*self.heure
        m=k*self.minute
        s=k*self.seconde
        res=Horloge(h,m,s)
        return res
    __rmul__ = __mul__


## ## ex 2 : Une classe complexe

class Complexe(object):

    def __init__ (self,a,b):
        self.a=a
        self.b=b
        
    def __repr__(self):
        if self.b==0:
            return str(self.a)
        elif self.b==1:
            return str(self.a)+"+i"
        elif self.b==(-1):
            return str(self.a)+"-i"
        elif self.b>0:
            return str(self.a)+"+"+str(self.b)+"i"
        else:
            return str(self.a)+str(self.b)+"i"

    def __add__(self,autre):
    ## selon le type de autre
        if isinstance(autre,Complexe):
            a=self.a+autre.a
            b=self.b+autre.b
            return Complexe(a,b)
        else:
            return Complexe(self.a+autre,self.b)
    __radd__=__add__

    def __sub__(self,autre):
        if isinstance(autre,Complexe):
            a=self.a-autre.a
            b=self.b-autre.b
            return Complexe(a,b)
        else:
            return Complexe(self.a-autre,self.b)

    def __rsub__(self,autre):
        autre-self

    def __neg__(self):
        a=-self.a
        b=-self.b
        return Complexe(a,b)

    def __mul__(self,autre):
        if isinstance(autre,Complexe):
            a=self.a*autre.a-self.b*autre.b
            b=self.a*autre.b+self.b*autre.a
            return Complexe(a,b)
        else:
            return Complexe(self.a*autre,self.b*autre)
    __rmul__ = __mul__

    def __div__(self,autre):
        if isinstance(autre,Complexe):
            d=float(autre.a**2+autre.b**2) ## la norme au carre

            a=(self.a*autre.a+self.b*autre.b)/d
            b=(-self.a*autre.b+self.b*autre.a)/d
            return Complexe(a,b)
        else:
            return Complexe(self.a/float(autre),self.b/float(autre))

    def __rdiv__(self,autre): ## pour -1/c1
        if type(autre) is int:
            return Complexe(autre,0)/self



## ex 3  Ensemble de Julia
## julia.py
    
if __name__ == '__main__':
##    h=Horloge(1,35,47)
##    i=Horloge(1,-45,-30)
##    print h
##    print i
##    res=h+i
##    print res
##    res2=i-h
##    print res2
##    res3=5*i
##    print res3
##    res4=i*5
##    print res4
##
##    print Horloge(2,-120,0)
    
    c1=Complexe(-3,2)
    c2=Complexe(2,-1)
    print c1
    print c2
    print c1+c2
    print 1+c1+c2
    print -c1-c2-4
    print 3*c1*c2
    print c1/c2
    print -1/c1

    
## Julia.Py

# -*- coding:utf-8  -*-
from POO8 import Complexe
from numpy import ndarray
from matplotlib import pyplot,cm
from math import sqrt

class Julia(ndarray):
    """
    On se donne un parametre complexe c.
    Pour chaque point du plan z, z est dans l'ensemble de Julia    
    si la suite
           | z{0} = z
           | z{n+1} = z{n}*z{n} + c
    converge.        
    """
    def __new__(cls,c,minx=-1,maxx=1,miny=-1,maxy=1,zoom=200,maxIte=255):
        sizex,sizey=int(zoom*(maxx-minx)),int(zoom*(maxy-miny))
        self = ndarray.__new__(cls, (sizex,sizey),dtype=int)
        self.fill(0)
        self.maxIte=maxIte
        self.c=c
        self.zoom=zoom
        self.minx,self.miny=minx,miny
        self.tailx,self.taily=sizex,sizey       
        return self

    def calcule(self):        
        coin=Complexe(self.minx,self.miny)
        zoom=float(self.zoom)
        for i in range(self.tailx):
            for j in range(self.taily):
                z=Complexe(i,j)/zoom+coin
                self[i,j]=self.couleur(z)

    def couleur(self,z):
        zn=z
        i=0
        while i<self.maxIte:
            i+=1
            z=z*z+self.c
            norm=sqrt(float(z.a**2+z.b**2))
            if norm>2:
                return i
        return i

if __name__=='__main__':
    m=Julia(Complexe(.3,.5),zoom=150,maxIte=150)
    # m=Julia(Complexe(.285,.01),zoom=150,maxIte=150)
    # m=Julia(Complexe(.285,.0),zoom=150,maxIte=150)
    m.calcule()
    pyplot.axis("off")    
    pyplot.imshow(m, cmap=cm.spectral) #cm.jet, cm.prism, cm.hot
    pyplot.show()



## TP9 ########################################################""
## __iter__ et next
class Miroir (object):

    def __init__(self,liste):
        self.liste=liste
        self.index=len(liste)

    def __iter__(self):
        return self

    def next(self):
        if self.index==0:
            raise StopIteration
        self.index-=1
        return self.liste[self.index]

m=Miroir([1,2,3,4])
##for el in m:
##    print (el)

## POO 9

## exercice 2 :

class Miroir (object):

    def __init__(self,liste):
        self.liste=liste
        self.index=len(liste)

    def __iter__(self):
        return self

    def next(self):
        if self.index==0:
            raise StopIteration
        self.index-=1
        return self.liste[self.index]

m=Miroir([1,2,3,4])
##for el in m:
##    print (el)
##>>> 
##4
##3
##2
##1
##>>>
m=Miroir([1,2,3,4])
##print(next(m))
##print(next(m))
##>>>
##4
##3
##>>> 

## exercice 3 :

class Circulaire(Miroir):
    
    def __init__(self,liste):
        Miroir.__init__(self,liste)
        
    def __iter__(self):
        return self

    def next(self):
        if self.index==0:
            self.index=len(self.liste)
        self.index-=1
        return self.liste[self.index]
m2=Circulaire([0,1,2])
##for el in m2:
##    print (el)
## Fonctionne, a l'infini !

## exercice 4 :
from random import *
class Aleatoire(object):

    def __init__(self,liste):
        shuffle(liste)
        self.liste=liste
        self.index=-1

    def __iter__(self):
        return self

    def next(self):
        if self.index==len(self.liste)-1:
            raise StopIteration
        self.index+=1
        return self.liste[self.index]

m3=Aleatoire([7,8,9,10,11,12])
##for el in m3:
##    print (el)

## exercice 5 :

class IterAlea(object):
    def __init__(self,n):
        self.n=n
        self.index=0

    def __iter__(self):
        return self

    def next(self):
        if self.index<self.n:
            self.index+=1
            x=random()
            y=random()
            boo=x*x+y*y<=1
            return (x,y,boo)

    def MonteCarlo(self):
        p=0.
        for i in range (self.n):
            if (next(self))[2]:
                p+=1
        return 4*p/self.n

s=IterAlea(100000)
print s.MonteCarlo()
## 3.14

## exercice 5 :

class Sequenceur(object):
    def __init__(self,it1,it2):
        self.it1=it1
        self.it2=it2
        self.tour=1

    def __iter__(self):
        return self

    def next(self):
        if self.tour==1:
            try:
                return next(self.it1)
            except StopIteration:
                self.tour=2
                return next(self.it2) ## evite de retourner un None au milieu des deux iterateurs
        else:
            return next(self.it2)
            
##>>> s=Sequenceur(iter(range(5)),iter('azerty'))
##>>> for el in s : print el 



## TP 10 Generateur ##################################################
def fonctionGenerateur(fn,n):
    for i in range(n):
        yield fn(i)

def mafn(x):return x+3

for el in fonctionGenerateur(mafn,7):
    print (el)
print

## ou ##
it=fonctionGenerateur(mafn,2)
print(next(it)) ## 3
print(next(it)) ## 4
##print(next(it)) ## StopIteration

print(list(fonctionGenerateur(lambda x:x*x,6))) ## 6 iterations d'un lambda fonction
## [0, 1, 4, 9, 16, 25]

## Engendrer les mots de longueurs n compose des 'lettres' 0 et 1
def mot(n):
    if n==0:
        yield ""
    else:
        for el in mot(n-1):
            yield el+'0'
            yield el+'1'

it=mot(3)
for el in it:print el
## idem mais avec les lettres d'un certain alphabet
def motQ2(n,alphabet):
    if n==0:
        yield ""
    else:
        for el in motQ2(n-1,alphabet):
            for l in alphabet:
                yield el+l

it2=list(motQ2(2,['a','b','c']))
for el in it2:print el

print(list(it2))

## iterer plusieurs generateurs
def sequence(*args):
    for gege in args:
        for el in gege:
            yield el
print (list(sequence(xrange(4),xrange(5,-1,-1),xrange(0,4,2),xrange(5,-1,-2))))
##[0, 1, 2, 3, 5, 4, 3, 2, 1, 0, 0, 2, 5, 3, 1]

## generateur d'un jeu de 32 cartes
def gene(E,F):
    for e in E:
        for f in F:
            yield (e,f)
E=['coeur','pique','carreau','trefle']
F=['As','7','8','9','10','J','Q','K']
print(list(gene(E,F)))

def sousEns(E,k):
    if k==0:
        yield []
    elif k==len(E):
        yield E
    else:
        for el in sousEns(E[1:],k):
            yield el
        for el in sousEns(E[1:],k-1):
            yield [E[0]]+el
            
print (list(sousEns(['a','b','c','d'],2)))
## [['c', 'd'], ['b', 'd'], ['b', 'c'], ['a', 'd'], ['a', 'c'], ['a', 'b']]

Jeu=list(gene(E,F)) ## genere un jeu de 32 cartes
geneMains=sousEns(Jeu,5) ## generateur de toutes les mains
## M=next(geneMains) ## une main
## print (M)

## regarder s'il y a un carre
def fonct(M):
    dico={} ## le dico des hauteurs contenu dans une main
    for carte in M:
        if carte[1] in dico:
            dico[carte[1]]+=1
        else:
            dico[carte[1]]=1
    return dico

def carre(M):
    return 4 in fonct(M).values()
def brelan(M):
    return 3 in fonct(M).values()

## nbr de mains contenant :
## - exactement un carre :
print len(list(filtre(geneMains,carre)))
## 224
print len(list(filtre(sousEns(Jeu,5),brelan)))
## 12096

## TP 10 Generateur

def fonctionGenerateur(fn,n):
    for i in range(n):
        yield fn(i)

def mafn(x):return x+3

for el in fonctionGenerateur(mafn,7):
    print (el)
print

##3
##4
##5
##6
##7
##8
##9

it=fonctionGenerateur(mafn,2)
print(next(it)) ## 3
print(next(it)) ## 4
##print(next(it)) ## StopIteration

print(list(fonctionGenerateur(lambda x:x*x,6)))
## [0, 1, 4, 9, 16, 25]
print(tuple(fonctionGenerateur(lambda x:x*'bla',4)))
## ('', 'bla', 'blabla', 'blablabla')

## Exo 2 : Engendrer les mots de longueurs n
## question 1
def mot(n):
    if n==0:
        yield ""
    else:
        for el in mot(n-1):
            yield el+'0'
            yield el+'1'

it=mot(3)
for el in it:print el

##000
##001
##010
##011
##100
##101
##110
##111

## question 2
def motQ2(n,alphabet):
    if n==0:
        yield ""
    else:
        for el in motQ2(n-1,alphabet):
            for l in alphabet:
                yield el+l

it2=list(motQ2(2,['a','b','c']))
for el in it2:print el
##aa
##ab
##ac
##ba
##bb
##bc
##ca
##cb
##cc
print(list(it2))
## ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']


## Exo 3

def sequence(*args):
    for i in range(len(args)):
        for el in args[i]:
            yield el

print (list(sequence(xrange(4),xrange(5,-1,-1),xrange(0,4,2),xrange(5,-1,-2))))
##[0, 1, 2, 3, 5, 4, 3, 2, 1, 0, 0, 2, 5, 3, 1]

## ou directement : 
def sequence(*args):
    for gege in args:
        for el in gege:
            yield el
print (list(sequence(xrange(4),xrange(5,-1,-1),xrange(0,4,2),xrange(5,-1,-2))))

## Exo 4

def gene(E,F):
    for e in E:
        for f in F:
            yield (e,f)

E=['coeur','pique','carreau','trefle']
F=['As','7','8','9','10','J','Q','K']
print(list(gene(E,F)))

## [('rouge', '1'), ('rouge', '2'), ('rouge', '3'), ('rouge', '4'), ('rouge', '5'), ('noir', '1'), ('noir', '2'), ('noir', '3'), ('noir', '4'), ('noir', '5')]

## question 2
def sousEns(E,k):
    if k==0:
        yield []
    elif k==len(E):
        yield E
    else:
        for el in sousEns(E[1:],k):
            yield el
        for el in sousEns(E[1:],k-1):
            yield [E[0]]+el
            
print (list(sousEns(['a','b','c','d'],2)))
## [['c', 'd'], ['b', 'd'], ['b', 'c'], ['a', 'd'], ['a', 'c'], ['a', 'b']]

## question 3

def filtre(generateur,predicat):
    for el in generateur:
        if predicat(el):
            yield el

print (list(filtre(xrange(50),lambda x:x%6==0)))

## question 4
Jeu=list(gene(E,F)) ## genere un jeu de 32 cartes
geneMains=sousEns(Jeu,5) ## generateur de toutes les mains
##M=next(geneMains) ## une main
## print (M)

## regarder s'il y a un carre
def fonct(M):
    dico={} ## le dico des hauteurs
    for carte in M:
        if carte[1] in dico:
            dico[carte[1]]+=1
        else:
            dico[carte[1]]=1

    return dico
def carre(M):
    return 4 in fonct(M).values()

def brelan(M):
    return 3 in fonct(M).values()

## question 5

## nbr de mains contenant :
## - exactement un carre :

print len(list(filtre(geneMains,carre)))
## 224
print len(list(filtre(sousEns(Jeu,5),brelan)))
## 12096



## TP 11 ############################################################
## Methode speciales  : un dico initialiser par un tuple

class MultiEnsemble(dict):

    def __init__(self,*args):
        for el in args:
            if el in self:
                self[el]+=1
            else:
                self[el]=1

    def __repr__(self):
        res='{'
        for el in self:
            res+=(str(el)+',')*self[el]
        res=res[:-1]+'}'
        return res

    def __len__(self):
        return sum(self.values())

    def __getitem__(self,cle):
        return self.get(cle,0)

    def __setitem__(self,cle,val):
        if val>=1:
            dict.__setitem__(self,cle,val)
        elif cle in self:
            dict.__delitem__(self,cle)

    def __delitem__(self,cle):
        self[cle]-=1

    def __eq__(self,autre):
        if isinstance(autre,MultiEnsemble):
            return dict.__eq__(self,autre)
        return False

    def __neq__(self,autre):
        if isinstance(autre,MultiEnsemble):
            return dict.__neq__(self,autre)
        return True

    def copy(self):
        arg=()
        for el in self:
            for nb in range (self[el]):
                arg+=(el,)
        return MultiEnsemble(*arg)

def test():
    M=MultiEnsemble(2,7,5,2,2,5)
    print M
    print dict.__repr__(M)
    print len(M)
   
a=MultiEnsemble(2,7,5,2,2,5)
print a ## {2,2,2,5,5,7}
print len(a) ## 6

# test()
##{2,2,2,5,5,7}
##{2: 3, 5: 2, 7: 1}
##6

##getitem
print a[2] ## 3
print a[10] ## 0
## setitem
a[10]=5
print a ##{2,2,2,10,10,10,10,10,5,5,7}
a[2]=0
print a ##{10,10,10,10,10,5,5,7}
## delitem
a.__delitem__(10)
print a
M=MultiEnsemble(2,7,5,2,2,5)
print M==a ## False
print M!=a ## True
print M!=M ## False
print M.copy() ## {2,2,2,5,5,7}


## TP 11 Methode spéciales

class MultiEnsemble(dict):

    def __init__(self,*args):
        for el in args:
            if el in self:
                self[el]+=1
            else:
                self[el]=1

    def __repr__(self):
        res='{'
        for el in self:
            res+=(str(el)+',')*self[el]
        res=res[:-1]+'}'
        return res

    def __len__(self):
        return sum(self.values())

    def __getitem__(self,cle):
        return self.get(cle,0)

    def __setitem__(self,cle,val):
        if val>=1:
            dict.__setitem__(self,cle,val)
        elif cle in self:
            dict.__delitem__(self,cle)

    def __delitem__(self,cle):
        self[cle]-=1

    def __eq__(self,autre):
        if isinstance(autre,MultiEnsemble):
            return dict.__eq__(self,autre)
        return False

    def __neq__(self,autre):
        if isinstance(autre,MultiEnsemble):
            return dict.__neq__(self,autre)
        return True

    def copy(self):
        arg=()
        for el in self:
            for nb in range (self[el]):
                arg+=(el,)
        return MultiEnsemble(*arg)


def test():
    M=MultiEnsemble(2,7,5,2,2,5)
    print M
    print dict.__repr__(M)
    print len(M)


    
a=MultiEnsemble(2,7,5,2,2,5)
print a
## {2,2,2,5,5,7}
print len(a)
## 6

# test()
##{2,2,2,5,5,7}
##{2: 3, 5: 2, 7: 1}
##6

##getitem
print a[2]
## 3
print a[10]
## 0

## setitem
a[10]=5
print a
##{2,2,2,10,10,10,10,10,5,5,7}
a[2]=0
print a
##{10,10,10,10,10,5,5,7}

## delitem
a.__delitem__(10)
print a

M=MultiEnsemble(2,7,5,2,2,5)
print M==a ## False
print M!=a ## True
print M!=M ## False

print M.copy()
## {2,2,2,5,5,7}


## TP 12 codage couleur RVB ################################################

class CouleurRVB(dict):

    def __init__(self,intr,intv,intb):
        if 0<intr<255 and 0<intv<255 and 0<intb<255:
            self['r']=intr
            self['v']=intv
            self['b']=intb
        else :
            raise TypeError ("une valeur de couleur n'est pas valide")

    def code(self):
        res=""
        for cle in self:
            if self[cle]<16:
                res+="0"+hex(self[cle])[2:]
            else:
                res+=hex(self[cle])[2:]
        return res

    def intensite(self):
        return max(self.values())

    def __repr__(self):
        return self.code()
    ## + l'affichage d'une fenetre Tk inter

    def __add__(self,c2):
        r,v,b=self['r']+c2['r'],self['v']+c2['v'],self['b']+c2['b']
        i= (self.intensite()+c2.intensite())/2.
        r3,v3,b3=r*i/max(r,v,b),v*i/max(r,v,b),b*i/max(r,v,b)
        return CouleurRVB(r3,v3,b3)

coul=CouleurRVB(60,50,180)
print coul
print coul.code()
print coul.intensite()
coul2=CouleurRVB(66,180,18)
print coul+coul



## ## ## cours M1 S1 Python ## ## ##

## Tkinter helloworld
from Tkinter import *

fen=Tk()
text=Label(fen, text="bonjour", fg="red")
but=Button(fen, text="Quitter", command=fen.destroy)
text.pack()
but.pack()
fen.mainloop()

## attribut de classe
class Helloworld(object):
    tableau=[...] ## Helloword.tableau+=[...]
    def __init__(self...) ..

## Agregation
class Segment(object):
    def __init__(self,x1,y1,x2,y2):
        self.p1=Point(x1,y1)
        self.p2=Point(x2,y2)

class Polygone(list):
    def __init__(self,*args):
        list.__init__(self,args) ## recup le tuple pour creer la liste
        for p in self:
            if not isinstance(p,Point):
                raise Exception, "un polugone ne contient que des points"

## class abstraite : pas implementee
## polymorphisme : une methode peut etre appelee par plusieurs objets diff et ne fera pas le meme chose
## interface : class ou tte les methodes sont abstraites
## corps d'un methode abstraite ne contient que l'erreur :
raise NotImplementedError

class C(A):
    def surcharge(self,nb1,nb2=None):
        if not nb2:
            A.surcharge(self,nb1)
        else:
            print nb1+nb2

## manipuler des attributs
objet.__setattr__('propriete',val)
objet.__setattribute__('propriete')
objet.__delattr__('propriete')

## surcharche de l'indexation
liste[valeur] <=> liste.__getitem__(valeur)
liste[v1]=v2 <=> lsite.__setitem__(v1,v2)

def __contains__(self,val):
    self.sort() ## ou l=self[:] et l.sort () ## self n'est pas modife a la fin
    return self[0]<=val<=self[-1]

## expression d'un generateur
[i*i fir i in range(10)]
[el*2 for el in range(4)]

from math import sin,pi
def tablesinus(intervalle=range(300)):
    return ((x,sin(x*pi/180)) for x in range(300) if x in intervalle)
## generateur
for (angle,sinus) in tablesinus(range(20,40)):
    print "sinus de %s degres vaut %s" %(angle,sinus)


def reverse(seq):
    for index in range(len(seq)-1,-1,-1):
        yield seq[index]
for i in reverse("bonjour"): print i,

import itertools ## biblio d'iterateur
dir(itertools)

for el in itertools.cycle((i for i in range(10))):print el
## boucle infini

islice(iterable,a,b) ## n'itere l'element que entre a et b

class TraiteFic(object):
    def __init__(self,fic):
        self.nomfic=fic
    def lire(self,nbligne=None):
        if not nbligne:
            return (ligne.strip() for ligne in open(self.nomfic) if len(ligne.strip())>0 )
        else:
            return itertools.islice((ligne.strip() for ligne in open() if len(ligne.strip())>0),0,nbligne)
    def tailleligne(self):
        return (len(ligne.strip()) for ligne in self.lire())


################
##            ##
##   FIN      ##
## Master M1  ## S1
##            ##
################

################
##            ##
##   DEBUT    ##
## Master M2  ## S2
##            ##
################

## TP0 ## 

# le programme va aller chercher toutes les fonctions de la bibliothèque Tkinter
from Tkinter import *      # la bibliothèque graphique


class Appli(Tk):
    def __init__(self,*args,**kw): # pourra prendre autant d'arguments avec et sans valeur par defaut (tuple et dico)
        Tk.__init__(self,*args,**kw)# 1iere chose : appeller le constructeur de la classe mere
        Label(self,text="Hello world").pack() # un label texte, directement placé
        BoutQuit(self,width=20).pack()

# spécialiser le bouton quitter:
class BoutQuit(Button):
    def __init__(self,fen,**kw):
        Button.__init__(self,fen,text="quitter",command=self.quitter,**kw)
        self.f=fen # attribut d'instance f : on sauve la fenetre fen pour les fonctions de toute ma classe

    def quitter(self):
        self.f.quit()
        self.f.destroy()
 
if __name__=='__main__':
    Appli().mainloop()



## Projet ##
## EnqueteDeRue ##

## essai graphique 

##import numpy
##from pylab import *
##
##x = [0, 1, 3, 3, 3, 4, 5, 5, 8, 8, 8, 8, 9]
##h, b = numpy.histogram(x, bins=5)
#### h, b = numpy.histogram(x, bins=[0, 2, 5, 8, 10])
##print (h, b)
##h = 100*h/float(len(x))
##print (h, b)
##pylab.figure()
##pylab.bar(b, h, width=b[1]-b[0])
#### width = [b[i+1]-b[i] for i in range(len(b)-1)]
#### pylab.bar(b[:-1], h[:-1], width=width)
##pylab.ylabel("frequence [%]")
##pylab.show()
##
##
##
##
##import pylab
##x = [1, 3, 3, 3, 4, 5, 5, 8, 8, 8, 8, 9]
##pylab.hist(x, bins=5)
##pylab.show()



x = [0, 1, 3, 3, 3, 4, 5, 5, 8, 8, 8, 8, 9]
histogram(x)
##	Compute the histogram of a set of data.


## Ecran menu OK 


#### Structure des ecrans MENU ####

from tkinter import *


# la bibliothèque graphique

class Appli(Tk):
    
    def __init__(self,*args,**kw): # pourra prendre autant d'arguments avec et sans valeur par defaut (tuple et dico)
        Tk.__init__(self,*args,**kw)# 1iere chose : appeller le constructeur de la classe mere
        Can=Canvas(self,height=100,width=100,bg="white").grid(row=0,column=0,sticky=NW)
        #Can.insert(self,text="Menu principal")
        Label(self,text="Menu principal",font=('Verdana', 18, 'bold')).grid(row=0,column=1,padx=20, pady=20)
        Benq1=BoutENQ(self,height=5,width=5).grid(row=1,column=1,padx=20, pady=20)
        Benq2=BoutENQ(self,height=5,width=5).grid(row=2,column=1,padx=20, pady=20)
        BoutQuit(self,width=10).grid(row=3,column=2)
        self.geometry("400x500")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        

# spécialiser le bouton quitter:
class BoutQuit(Button):
    def __init__(self,fen,**kw):
        Button.__init__(self,fen,text="quitter",command=self.quitter,**kw)
        self.f=fen # attribut d'instance f : on sauve la fenetre fen pour les fonctions de toute ma classe

    def quitter(self):
        self.f.quit()
        self.f.destroy()
        #Message() ### Si on veut demander "Etes vous sur.. ?"

class BoutENQ(Button):
    def __init__(self,fen,**kw):
        Button.__init__(self,fen,text="enq",command=self.charger,**kw)
        self.f=fen # attribut d'instance f : on sauve la fenetre fen pour les fonctions de toute ma classe

    def charger(self):
        Enquete()
        
class Enquete(Toplevel):
    def __init__(self,nbQuestion=10,**kw):
        Toplevel.__init__(self,**kw)
        self.geometry("400x500")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.title("L'enquete est en cours...")
        BoutQuitMESSAGE(self).grid(row=0,column=0)


class BoutQuitMESSAGE(Button):
    def __init__(self,fen,**kw):
        Button.__init__(self,fen,text="quitter",command=self.message,**kw)
        self.f=fen
        
    def message(self):
        Message(self.f) ### Si on veut demander "Etes vous sur.. ?"

        
class Message(Toplevel):
    def __init__(self,fen,**kw):
        Toplevel.__init__(self,**kw)
        self.title("Message avant de quitter")
        self.geometry("400x500")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        Label(self,text="etes vous sur de vouloir quitter ? (Retour au Menu)",font=("Calibri",20)).grid(row=0,column=0)
        Button(self,text="Oui",command=lambda f1=self,f2=fen:(f1.destroy(),f2.destroy())).grid(row=1,column=0)
        Button(self,text="Non",command=self.destroy).grid(row=1,column=1)

                   
 
if __name__=='__main__':
    Appli().mainloop()


## toplevel ; fenetre dependant d'une autre


#### Application Jolie

#### Structure des ecrans MENU ####
import string
from Tkinter import *
from random import *

########################### Fenetre principale de notre application:
class Appli(Tk):
    
    def __init__(self,*args,**kw): # pourra prendre autant d'arguments avec et sans valeur par defaut (tuple et dico)
        Tk.__init__(self,*args,**kw)# 1iere chose : appeller le constructeur de la classe mere
        
        #Image et canevas:
        self.Can=Canvas(self,height=100,width=120,bg="white")
        self.Can.grid(row=0,column=0,sticky=NW)
        self.image = PhotoImage(file='im.gif')
        self.Can.create_image(50,60, image = self.image)

        #Label et bouton:
        Label(self,text="Menu principal",font=('Verdana', 18, 'bold'),bg="white").grid(row=0,column=1,padx=20, pady=20)
        Benq1=BoutENQ(self,height=5,width=10).grid(row=1,column=1,padx=20, pady=20)
        Benq2=BoutENQ(self,height=5,width=10).grid(row=2,column=1,padx=20, pady=20)
        BoutQuit(self,width=10).grid(row=3,column=2)
        self.geometry("400x500")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.configure(bg = "white")



#Specialiser le bouton quitter:
class BoutQuit(Button):
    def __init__(self,fen,**kw):
        Button.__init__(self,fen,text="Quitter",command=self.quitter,**kw)
        self.f=fen # attribut d'instance f : on sauve la fenetre fen pour les fonctions de toute ma classe

    def quitter(self):
        self.f.quit()
        self.f.destroy()

#Specialiser le bouton enquete:
class BoutENQ(Button):
    def __init__(self,fen,**kw):
        Button.__init__(self,fen,text="Enquete",command=self.charger,**kw)
        self.f=fen # attribut d'instance f : on sauve la fenetre fen pour les fonctions de toute ma classe

    def charger(self):
        NomEnq()
    
#Specialiser le bouton statistique:
class BoutSTAT(Button):
    def __init__(self,fen,**kw):
        Button.__init__(self,fen,text="Statistique",command=self.charger,**kw)
        self.f=fen

    def charger(self):
        Statistique()
        
#Specialiser le bouton questionnaire:
class BoutNomEnq(Button):
    def __init__(self,fen,**kw):
        Button.__init__(self,fen,text="Questionnaire",command=self.charger,**kw)
        self.f=fen # attribut d'instance f : on sauve la fenetre fen pour les fonctions de toute ma classe

    def charger(self):
        Enquete() #On charge la page du questionnaire de l'enquete


##################################### DEMARRE LA DEUXIEME FENETRE NOM ENQUETE AVEC POSSIBILITE DE RETOUR ET DE FERMER L'APPLICATION
class NomEnq(Toplevel):
    def __init__(self,nbQuestion=10,**kw):
        Toplevel.__init__(self,**kw)
        self.geometry("400x500")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.title("Que voulez-vous faire sur cette enquete ?")
        self.configure(bg = "white")

        #Image et canevas
        self.Can=Canvas(self,height=100,width=120,bg="white")
        self.Can.grid(row=0,column=0,sticky=NW)
        self.image = PhotoImage(file='im.gif')
        self.Can.create_image(50,60, image = self.image)
        
        Label(self,text="Menu Enquete",font=('Verdana', 18, 'bold'),bg="white").grid(row=0,column=1,padx=20, pady=20)
        Benq1=BoutNomEnq(self,height=5,width=10).grid(row=1,column=1,padx=20, pady=20) #Envoie l'enqueteur sur la page questionnaire (enquete)
        Benq2=BoutSTAT(self,height=5,width=10).grid(row=2,column=1,padx=20, pady=20) #ENvoie l'enqueteur sur la page des statistiques
        BoutQuitMENU(self,width=10).grid(row=3,column=0)
        BoutQuitAPP(self,width=10).grid(row=3,column=2)
        self.geometry("400x500")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.configure(bg = "white")


#Mise en place d'un bouton retour menu dans l'interface de l'enquete:
class BoutQuitMENU(Button):
    def __init__(self,fen,**kw):
        Button.__init__(self,fen,text="Retour",command=lambda f1=self,f2=fen:(f1.destroy(),f2.destroy()),**kw)


#Mise en place d'un bouton fermer application: ########## NE MARCHE PAS #######
class BoutQuitAPP(Button):
    def __init__(self,fen,**kw):
        Button.__init__(self,fen,text="Fermer application",command=lambda f1=self,f2=fen:(f1.destroy(),f2.destroy()),**kw)
        self.f=fen
        
       
################################## ICI COMMENCE LE CODE STAT A REFAIRE 
class Statistique(Toplevel):
    pass

################################## ICI COMMENCE LE CODE ENQUETE        
class Enquete(Toplevel):
    def __init__(self,nbQuestion=10,**kw):
        Toplevel.__init__(self,**kw)
        self.geometry("400x500")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.title("L'enquete est en cours...")
        self.configure(bg = "white")
        
        #Image du questionnaire:
        self.cQ=Canvas(self,width=100, height=120, background='white')
        self.cQ.grid(column=0,row=0,rowspan=2,sticky=NW)
        self.image = PhotoImage(file='im.gif')
        self.cQ.create_image(50,60, image = self.image)
        
        #Lecture du fichier des questions:
        self.Fichier = open('question.txt','r').read().split("\n")
        self.i=0
        self.j=0
        self.f=self.Fichier
        self.q=self.f[self.i]+"\n"+self.f[self.i+1]

        #Frame de la question:
        self.fQuest=Frame(self)
        self.fQuest.grid(column=1,row=0,sticky=N)
        self.fQuest.configure(bg = "white")

        #Frame de la reponse:
        self.fRep=Frame(self)
        self.fRep.grid(column=1,row=1,columnspan=1,padx=10, pady=10)
        self.fRep.configure(bg = "white")

        #Frame de liste des questions:
        self.fList=Frame(self)
        self.fList.grid(column=2,row=0,rowspan=3,padx=10, pady=5,sticky=E)
        self.fList.configure(bg = "white")

        #Frame du bouton suivant:
        self.fSuiv=Frame(self)
        self.fSuiv.grid(column=1,row=2,columnspan=1,padx=20, pady=20)
        self.fSuiv.configure(bg = "white")

        #Creation de la question et des reponses
        Question=Label(self.fQuest,text=self.q,fg="red",width=20, height=5,relief=RAISED).pack(side = TOP)
        # Label(fRep,text="Reponse",fg="red",relief=RAISED,width=20, height=15).pack(side = BOTTOM)

        #Lecture du fichier des réponses:
        self.lignes = open('rep.txt','r').readlines()
        ligne=self.lignes[self.j].split(";")
        self.frep=ligne
        print(self.frep)
        textvar=[]
        var=[]
        
        if (self.frep[0])=="C":
            for i in range(int(self.frep[1])):
                textvar+=[str(self.frep[2+i])]
                var+=[IntVar()]
                Checkbutton(self.fRep,text=textvar[i],variable=var[i],width=20, height=5).pack(side=TOP)
                
        if (self.frep[0])=="R":
            for i in range(int(self.frep[1])):
                textvar+=[str(self.frep[2+i])]
                var+=[IntVar()]
                Radiobutton(self.fRep,text=textvar[i],variable=var[i],width=20, height=5,value=i).pack(side=TOP)

        if (self.frep[0])=="S":
            reponse=StringVar()
            var+=[reponse]
            Champ=Entry(self.fRep,textvariable=reponse,bg="white")#,xview_scroll(20,UNITS))
            Champ.focus_set()
            Champ.pack(side=TOP,padx=5,pady=5)
 
        #Creation d'un bouton:
        BoutQuitMESSAGE(self).grid(row=3,column=2,padx=5, pady=5,sticky=SE)
        Button(self.fSuiv,text='Suivante',bg = "light blue",width=10, height=3,command=self.suivant).grid(column=2,row=0,padx=10, pady=10)


        #Liste des questions
        listQuest=["Q1","Q2","Q3","Q4","Q5","Q6","Q7","Q8","Q9","Q10"]
        m=0
        print (listQuest[1])
        for q in listQuest:
            m=m+1
            Button(self.fList,text=q,command=lambda l=q:self.question(l)).grid(column=3,row=m)


    def question(self,q):
        print (q)

    def suivant(self):
        #On dÃ©truit la frame actuelle:
        self.fQuest.destroy()
        self.fRep.destroy()
        #On remet la frame:
        self.fQuest=Frame(self)
        self.fQuest.grid(column=1,row=0,sticky=N)
        self.fQuest.configure(bg = "white")
        self.fRep=Frame(self)
        self.fRep.grid(column=1,row=1,columnspan=1,padx=10, pady=10)
        self.fRep.configure(bg = "white")
        #Mise Ã  jour des questions:
        self.i=self.i+2
        self.j=self.j+1
        n=int(self.i)
        m=int(self.j)
        if self.i < (len(self.Fichier)-1):
            print (n)
            print (m)
            self.f=self.Fichier
            self.q=self.f[n]+"\n"+self.f[n+1]
            self.Question=Label(self.fQuest,text=self.q,fg="red",width=27, height=5,relief=RAISED).pack(side = BOTTOM)

            # mise a jour des reponses :
            ligne=self.lignes[m].split(";")
            self.frep=ligne
            print(self.frep)
            textvar=[]
            var=[]
            if (self.frep[0])=="C":
                for i in range(int(self.frep[1])):
                    textvar+=[str(self.frep[2+i])]
                    var+=[IntVar()]
                    Checkbutton(self.fRep,text=textvar[i],variable=var[i],width=20, height=5).pack(side=TOP)
                    
            if (self.frep[0])=="R":
                for i in range(int(self.frep[1])):
                    textvar+=[str(self.frep[2+i])]
                    var+=[IntVar()]
                    Radiobutton(self.fRep,text=textvar[i],variable=var[i],width=20, height=5,value=i).pack(side=TOP)

            if (self.frep[0])=="S":
                reponse=StringVar()
                var+=[reponse]
                Champ=Entry(self.fRep,textvariable=reponse,bg="white")#,xview_scroll(20,UNITS))
                Champ.focus_set()
                Champ.pack(side=TOP,padx=5,pady=5)


        else:
            # Detruire les frames existantes::
            self.fSuiv.destroy()
            self.fRep.destroy()
            self.fList.destroy()

            #On recrÃ©e la frame fSuiv pour mettre un bouton enregistrer:
            self.fSuiv=Frame(self)
            self.fSuiv.grid(column=1,row=2,columnspan=1,padx=20, pady=20)
            self.fSuiv.configure(bg = "white")
            Button(self.fSuiv,text='Enregistrer',bg = "light blue",width=10, height=3,command=self.enr).grid(column=2,row=0,padx=10, pady=10)

            #On recrÃ©e la frame FRep pour mettre un texte de remerciement:
            self.fRep=Frame(self)
            self.fRep.grid(column=1,row=1,columnspan=1,padx=10, pady=10)
            self.fRep.configure(bg = "white")
            Label(self.fRep,text="Voulez vous enregistrer  \n vos rÃ©ponses. \n \n Merci d'avoir rÃ©pondu \n au questionnaire !",bg="white",fg="blue",relief=RAISED,width=20, height=15).pack(side = BOTTOM)
        
            print ("Fin du questionnaire")
      
    def enr(self):
        pass


class BoutQuitMESSAGE(Button):
    def __init__(self,fen,**kw):
        Button.__init__(self,fen,text="quitter",command=self.message,**kw)
        self.f=fen
        
    def message(self):
        Message(self.f) ### Si on veut demander "Etes vous sur.. ?"

######################## IL FAUT RECUPERER CETTE CLASSE CAR MODIFICATION
class Message(Toplevel):
    def __init__(self,fen,**kw):
        Toplevel.__init__(self,**kw)
        self.configure(bg="white")
        self.title("ATTENTION FERMETURE ENQUETE!")
        self.geometry("300x250")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        Label(self,text="Etes-vous sur \n de vouloir quitter ? \n (Retour au Menu) \n \n Vos reponses ne seront \n pas enregistrÃ©es.",bg="white",font=("arial",12)).grid(row=0,column=0,columnspan=2,sticky=NSEW)
        Button(self,text="Non",font="arial 12 bold",width=10,bg="light blue", height=2,command=self.destroy).grid(row=1,sticky=NSEW,column=0,padx=10,pady=10)
        Button(self,text="Oui",width=10, bg="light blue",height=2,command=lambda f1=self,f2=fen:(f1.destroy(),f2.destroy())).grid(row=1,sticky=NSEW,column=1,padx=10,pady=10)
        

class BoutEnregistrer(Button):
    def __init__(self,fen,**kw):
        Button.__init__(self,fen,text="Enregistrer",command=self.enregistrer,**kw)
        self.f=fen
        

 
if __name__=='__main__':
    Appli().mainloop()



## Appli fusion + radio 


## Application a lancer avec Python 3.4
import string
from tkinter import *
from random import *


########################### Fenetre principale de notre application:
class Appli(Tk):

    def __init__(self,*args,**kw): # pourra prendre autant d'arguments avec et sans valeur par defaut (tuple et dico)
        Tk.__init__(self,*args,**kw)# 1iere chose : appeller le constructeur de la classe mere

        #Image et canevas
        self.Can=Canvas(self,height=100,width=100,bg="white")
        self.Can.grid(row=0,column=0,sticky=NW)
        self.image = PhotoImage(file='im.gif')
        self.Can.create_image(50,60, image = self.image)
        #Label et bouton:
        Label(self,text="Menu principal",font=('Verdana', 18, 'bold'),bg="white").grid(row=0,column=1,padx=20, pady=20)
        Benq1=BoutENQ(self,height=5,width=10).grid(row=1,column=1,padx=20, pady=20)
        Benq2=BoutENQ(self,height=5,width=10).grid(row=2,column=1,padx=20, pady=20)
        BoutQuit(self,width=10).grid(row=3,column=2)
        self.geometry("400x500")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.configure(bg = "white")



# spécialiser le bouton quitter:
class BoutQuit(Button):
    def __init__(self,fen,**kw):
        Button.__init__(self,fen,text="quitter",command=self.quitter,**kw)
        self.f=fen # attribut d'instance f : on sauve la fenetre fen pour les fonctions de toute ma classe

    def quitter(self):
        self.f.quit()
        self.f.destroy()

#Specialiser le bouton enquete relatif a une enquete choisis:
class BoutENQ(Button):
    def __init__(self,fen,**kw):
        Button.__init__(self,fen,text="Enquete",command=self.charger,**kw)
        self.f=fen # attribut d'instance f : on sauve la fenetre fen pour les fonctions de toute ma classe

    def charger(self):
        NomEnq(self.f)
    
#Specialiser le bouton statistique:
class BoutSTAT(Button):
    def __init__(self,fen,**kw):
        Button.__init__(self,fen,text="Statistique",command=self.charger,**kw)
        self.f=fen

    def charger(self):
        Statistique()
        
#Specialiser le bouton questionnaire:
class BoutNomEnq(Button):
    def __init__(self,fen,**kw):
        Button.__init__(self,fen,text="Questionnaire",command=self.charger,**kw)
        self.f=fen # attribut d'instance f : on sauve la fenetre fen pour les fonctions de toute ma classe

    def charger(self):
        Enquete() #On charge la page du questionnaire de l'enquete



##################################### DEMARRE LA DEUXIEME FENETRE NOM ENQUETE AVEC POSSIBILITE DE RETOUR ET DE FERMER L'APPLICATION
class NomEnq(Toplevel):
    def __init__(self,fen,nbQuestion=10,**kw):
        Toplevel.__init__(self,fen,**kw)
        self.geometry("400x500")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.title("Que voulez-vous faire sur cette enquete ?")
        self.configure(bg = "white")

        #Image et canevas
        self.Can=Canvas(self,height=100,width=120,bg="white")
        self.Can.grid(row=0,column=0,sticky=NW)
        self.image = PhotoImage(file='im.gif')
        self.Can.create_image(50,60, image = self.image)
        
        Label(self,text="Menu Enquete",font=('Verdana', 18, 'bold'),bg="white").grid(row=0,column=1,padx=20, pady=20)
        Benq1=BoutNomEnq(self,height=5,width=10).grid(row=1,column=1,padx=20, pady=20) #Envoie l'enqueteur sur la page questionnaire (enquete)
        Benq2=BoutSTAT(self,height=5,width=10).grid(row=2,column=1,padx=20, pady=20) #ENvoie l'enqueteur sur la page des statistiques
        #Mise en place d'un bouton retour menu dans l'interface de l'enquete:
        Button(self,text="Retour",width=10,command=self.destroy).grid(row=3,column=0)
        ##############################################################################################################################
        #Mise en place d'un bouton fermer application:
        Button(self,text="Fermer application",width=10,command=lambda f1=self,f2=fen:(f1.destroy(),f2.destroy())).grid(row=3,column=2)

 
        self.geometry("400x500")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.configure(bg = "white")


################################## ICI COMMENCE LE CODE STAT A REFAIRE 
class Statistique(Toplevel):
    pass

################################## ICI COMMENCE LE CODE ENQUETE             
class Enquete(Toplevel):
    def __init__(self,nbQuestion=10,**kw):
        Toplevel.__init__(self,**kw)
        self.geometry("400x500")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.title("L'enquete est en cours...")
        self.configure(bg = "white")

        self.listerep=[]
        
        #Image du questionnaire:
        self.cQ=Canvas(self,width=100, height=120, background='white')
        self.cQ.grid(column=0,row=0,rowspan=2,sticky=NW)
        self.image = PhotoImage(file='im.gif')
        self.cQ.create_image(50,60, image = self.image)
        
        #Lecture du fichier:
        self.Fichier = open('question.txt','r',encoding="utf-8").read().split("\n")
        self.i=0
        self.j=0
        self.f=self.Fichier
        self.q=self.f[self.i]+"\n"+self.f[self.i+1]

        #Frame de la question:
        self.fQuest=Frame(self)
        self.fQuest.grid(column=1,row=0,sticky=N)
        self.fQuest.configure(bg = "white")

        #Frame de la réponse:
        self.fRep=Frame(self)
        self.fRep.grid(column=1,row=1,columnspan=1,padx=10, pady=10)
        self.fRep.configure(bg = "white")

        #Frame de liste des questions:
        self.fList=Frame(self)
        self.fList.grid(column=2,row=0,rowspan=3,padx=10, pady=5,sticky=E)
        self.fList.configure(bg = "white")

        #Frame du bouton suivant:
        self.fSuiv=Frame(self)
        self.fSuiv.grid(column=1,row=2,columnspan=1,padx=20, pady=20)
        self.fSuiv.configure(bg = "white")


        #Creation de la question et des reponses
        Question=Label(self.fQuest,text=self.q,fg="red",width=20, height=5,relief=RAISED).pack(side = TOP)
        # Label(fRep,text="Reponse",fg="red",relief=RAISED,width=20, height=15).pack(side = BOTTOM)
        #Lecture du fichier:
        self.lignes = open('rep.txt','r',encoding="utf-8").readlines()
        ligne=self.lignes[self.j].split(";")
        self.frep=ligne
        print(self.frep)
        textvar=[]
      
        if (self.frep[0])=="R":
            v=IntVar()
            for i in range(int(self.frep[1])):
                textvar+=[str(self.frep[2+i])]
                Radiobutton(self.fRep,text=textvar[i],variable=v,width=20, height=5,value=i).pack(side=TOP)

        if (self.frep[0])=="S":
            reponse=StringVar()
            self.Champ=Entry(self.fRep,textvariable=reponse,bg="white")#,xview_scroll(20,UNITS))
            self.Champ.focus_set()
            self.Champ.pack(side=TOP,padx=5,pady=5)

        #Création d'un bouton:
        BoutQuitMESSAGE(self).grid(row=3,column=2,padx=5, pady=5,sticky=SE)
        Button(self.fSuiv,text='Suivante',bg = "light blue",width=10, height=3,command=self.suivant).grid(column=2,row=0,padx=10, pady=10)


        #Liste des questions
        listQuest=["Q1","Q2","Q3","Q4","Q5","Q6","Q7","Q8","Q9","Q10"]
        m=0
        print (listQuest[1])
        for q in listQuest:
            m=m+1
            Button(self.fList,text=q,command=lambda l=q:self.question(l)).grid(column=3,row=m)


    def question(self,q):
        print (q)
        
    def quitter(self):
               self.quit()
               self.destroy()

    def suivant(self):
        ## Teste pour voir la reponse a la question 1 :
        if (self.frep[0])=="R":
            print("la valeur choisi est")
            print(v.get())
        if (self.frep[0])=="S":
            print("la saisi est ")
            print((self.Champ).get())
            
        #On détruit la frame actuelle:
        self.fQuest.destroy()
        self.fRep.destroy()
        #On remet la frame:
        self.fQuest=Frame(self)
        self.fQuest.grid(column=1,row=0,sticky=N)
        self.fQuest.configure(bg = "white")
        self.fRep=Frame(self)
        self.fRep.grid(column=1,row=1,columnspan=1,padx=10, pady=10)
        self.fRep.configure(bg = "white")
        #Mise à jour des questions:
        self.i=self.i+2
        self.j=self.j+1
        n=int(self.i)
        m=int(self.j)

        
        if self.i < (len(self.Fichier)-1):
            
##            print (n)
##            print (m)
            self.f=self.Fichier
            self.q=self.f[n]+"\n"+self.f[n+1]
            self.Question=Label(self.fQuest,text=self.q,fg="red",width=27, height=5,relief=RAISED).pack(side = BOTTOM)

            # mise a jour des reponses :
            ligne=self.lignes[m].split(";")
            self.frep=ligne
            print(self.frep)
            textvar=[]
                   
            if (self.frep[0])=="R":
                v=IntVar()
                for i in range(int(self.frep[1])):
                    textvar+=[str(self.frep[2+i])]
                    r=Radiobutton(self.fRep,text=textvar[i],variable=v,width=20, height=5,value=i).pack(side=TOP)
                print("la valeur selectionné est : ")
                print(v.get())
                # recuperer les reponses checked
                ###i=index((v.get())==1)
                ###self.listerep+=[textvar[i]]
                ##print(self.listerep)

            if (self.frep[0])=="S":
                reponse=StringVar()
                self.Champ=Entry(self.fRep,textvariable=reponse,bg="white")#,xview_scroll(20,UNITS))
                self.Champ.focus_set()
                self.Champ.pack(side=TOP,padx=5,pady=5)
##                self.listerep+=[Champ.get()]
##                print(self.listerep)


        else:
            # Detruire les frames existantes::
            self.fSuiv.destroy()
            self.fRep.destroy()
            self.fList.destroy()

            #On recrée la frame fSuiv pour mettre un bouton enregistrer:
            self.fSuiv=Frame(self)
            self.fSuiv.grid(column=1,row=2,columnspan=1,padx=20, pady=20)
            self.fSuiv.configure(bg = "white")
            Button(self.fSuiv,text='Enregistrer',bg = "light blue",width=10, height=3,command=self.enr).grid(column=2,row=0,padx=10, pady=10)

            #On recrée la frame FRep pour mettre un texte de remerciement:
            self.fRep=Frame(self)
            self.fRep.grid(column=1,row=1,columnspan=1,padx=10, pady=10)
            self.fRep.configure(bg = "white")
            Label(self.fRep,text="Voulez vous enregistrer  \n vos réponses. \n \n Merci d'avoir répondu \n au questionnaire !",bg="white",fg="blue",relief=RAISED,width=20, height=15).pack(side = BOTTOM)
        
            print ("Fin du questionnaire")
      
    def enr(self):
        pass


class BoutQuitMESSAGE(Button):
    def __init__(self,fen,**kw):
        Button.__init__(self,fen,text="quitter",command=self.message,**kw)
        self.f=fen
        
    def message(self):
        Message(self.f) ### Si on veut demander "Etes vous sur.. ?"

        
class Message(Toplevel):
    def __init__(self,fen,**kw):
        Toplevel.__init__(self,**kw)
        Toplevel.__init__(self,**kw)
        self.configure(bg="white")
        self.title("ATTENTION FERMETURE ENQUETE!")
        self.geometry("300x250")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        Label(self,text="Etes-vous sur \n de vouloir quitter ? \n (Retour au Menu) \n \n Vos reponses ne seront \n pas enregistrées.",bg="white",font=("arial",12)).grid(row=0,column=0,columnspan=2,sticky=NSEW)
        Button(self,text="Non",font="arial 12 bold",width=10,bg="light blue", height=2,command=self.destroy).grid(row=1,sticky=NSEW,column=0,padx=10,pady=10)
        Button(self,text="Oui",width=10, bg="light blue",height=2,command=lambda f1=self,f2=fen:(f1.destroy(),f2.destroy())).grid(row=1,sticky=NSEW,column=1,padx=10,pady=10)
        
       

 
if __name__=='__main__':
    Appli().mainloop()


## toplevel ; fenetre dependant d'une autre


## Appli enreistr 

#### Structure des ecrans MENU ####
import string
from Tkinter import *
from random import *

# la bibliothèque graphique

class Appli(Tk):
    
    def __init__(self,*args,**kw): # pourra prendre autant d'arguments avec et sans valeur par defaut (tuple et dico)
        Tk.__init__(self,*args,**kw)# 1iere chose : appeller le constructeur de la classe mere

        #Image et canevas
        self.Can=Canvas(self,height=120,width=120,bg="white")
        self.Can.grid(row=0,column=0,sticky=NW)
        self.image = PhotoImage(file='im.gif')
        self.Can.create_image(50,60, image = self.image)
        
        Label(self,text="Menu principal",font=('Verdana', 18, 'bold'),bg="white").grid(row=0,column=1,sticky=N,padx=5, pady=5)
        Benq1=BoutENQ(self,height=5,width=10).grid(row=1,column=1,padx=5, pady=5)
        Benq2=BoutENQ(self,height=5,width=10).grid(row=2,column=1,padx=5, pady=5)
        BoutQuit(self,width=10).grid(row=3,column=2)
        self.geometry("400x500")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.configure(bg = "white")



# spécialiser le bouton quitter:
class BoutQuit(Button):
    def __init__(self,fen,**kw):
        Button.__init__(self,fen,text="quitter",command=self.quitter,**kw)
        self.f=fen # attribut d'instance f : on sauve la fenetre fen pour les fonctions de toute ma classe

    def quitter(self):
        self.f.quit()
        self.f.destroy()
        #Message() ### Si on veut demander "Etes vous sur.. ?"

class BoutENQ(Button):
    def __init__(self,fen,**kw):
        Button.__init__(self,fen,text="Enquête",command=self.charger,**kw)
        self.f=fen # attribut d'instance f : on sauve la fenetre fen pour les fonctions de toute ma classe

    def charger(self):
        Enquete()
        
class Enquete(Toplevel):
    def __init__(self,nbQuestion=10,**kw):
        Toplevel.__init__(self,**kw)
        self.geometry("400x500")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.title("L'enquete est en cours...")
        self.configure(bg = "white")
        
        #Image du questionnaire:
        self.cQ=Canvas(self,width=100, height=120, background='white')
        self.cQ.grid(column=0,row=0,rowspan=2,sticky=NW)
        self.image = PhotoImage(file='im.gif')
        self.cQ.create_image(50,60, image = self.image)
        
        #Lecture du fichier:
        self.Fichier = open('question.txt','r').read().split("\n")
        self.i=0
        self.f=self.Fichier
        self.q=self.f[self.i]+"\n"+self.f[self.i+1]

        #Frame de la question:
        self.fQuest=Frame(self)
        self.fQuest.grid(column=1,row=0,sticky=N)
        self.fQuest.configure(bg = "white")

        #Frame de la réponse:
        self.fRep=Frame(self)
        self.fRep.grid(column=1,row=1,columnspan=1,padx=10, pady=10)
        self.fRep.configure(bg = "white")

        #Frame de liste des questions:
        self.fList=Frame(self)
        self.fList.grid(column=2,row=0,rowspan=3,padx=10, pady=5,sticky=E)
        self.fList.configure(bg = "white")

        #Frame du bouton suivant:
        self.fSuiv=Frame(self)
        self.fSuiv.grid(column=1,row=2,columnspan=1,padx=20, pady=20)
        self.fSuiv.configure(bg = "white")


        #label:
        #Creation de la question et des reponses
        Question=Label(self.fQuest,text=self.q,fg="red",width=20, height=5,relief=RAISED).pack(side = TOP)
        #Label(fRep,text="Reponse",fg="red",relief=RAISED,width=20, height=15).pack(side = BOTTOM)
        #Lecture du fichier:
        ligne = open('rep.txt','r').read().split(";")
        self.frep=ligne
        print(self.frep)
        textvar=[]
        var=[]
        
        if (self.frep[0])=="C":
            for i in range(int(self.frep[1])):
                textvar+=[str(self.frep[2+i])]
                var+=[IntVar()]
                Checkbutton(self.fRep,text=textvar[i],variable=var[i],width=20, height=5).pack(side=TOP)
                
        if (self.frep[0])=="R":
            for i in range(int(self.frep[1])):
                textvar+=[str(self.frep[2+i])]
                var+=[IntVar()]
                Radiobutton(self.fRep,text=textvar[i],variable=var[i],width=20, height=5,value=i).pack(side=TOP)

        if (self.frep[0])=="S":
            reponse=StringVar()
            var+=[reponse]
            Champ=Entry(self.fRep,textvariable=reponse,bg="white")#,xview_scroll(20,UNITS))
            Champ.focus_set()
            Champ.pack(side=TOP,padx=5,pady=5)
 
        #Création d'un bouton:
        BoutQuitMESSAGE(self).grid(row=3,column=2,padx=5, pady=5,sticky=SE)
        Button(self.fSuiv,text='Suivante',bg = "light blue",width=10, height=3,command=self.suivant).grid(column=2,row=0,padx=10, pady=10)


        #Liste des questions
        listQuest=["Q1","Q2","Q3","Q4","Q5","Q6","Q7","Q8","Q9","Q10"]
        m=0
        print (listQuest[1])
        for q in listQuest:
            m=m+1
            Button(self.fList,text=q,command=lambda l=q:self.question(l)).grid(column=3,row=m)


    def question(self,q):
        print (q)
        
    def quitter(self):
               self.quit()
               self.destroy()

    def suivant(self):
        #On détruit la frame actuelle:
        self.fQuest.destroy()
        #On remet la frame:
        self.fQuest=Frame(self)
        self.fQuest.grid(column=1,row=0,sticky=N)
        self.fQuest.configure(bg = "white")
        #Mise à jour des questions:
        self.i=self.i+2
        n=int(self.i)
        if self.i < (len(self.Fichier)-1):
            print (n)
            self.f=self.Fichier
            self.q=self.f[n]+"\n"+self.f[n+1]
            self.Question=Label(self.fQuest,text=self.q,fg="red",width=27, height=5,relief=RAISED).pack(side = BOTTOM)
        else:
            # Detruire les frames existantes::
            self.fSuiv.destroy()
            self.fRep.destroy()
            self.fList.destroy()

            #On recrée la frame fSuiv pour mettre un bouton enregistrer:
            self.fSuiv=Frame(self)
            self.fSuiv.grid(column=1,row=2,columnspan=1,padx=20, pady=20)
            self.fSuiv.configure(bg = "white")
            Button(self.fSuiv,text='Enregistrer',bg = "light blue",width=10, height=3,command=self.enr).grid(column=2,row=0,padx=10, pady=10)

            #On recrée la frame FRep pour mettre un texte de remerciement:
            self.fRep=Frame(self)
            self.fRep.grid(column=1,row=1,columnspan=1,padx=10, pady=10)
            self.fRep.configure(bg = "white")
            Label(self.fRep,text="Vos réponses ont bien \n été enregistrées. \n \n Merci d'avoir répondu \n au questionnaire !",bg="white",fg="blue",relief=RAISED,width=20, height=15).pack(side = BOTTOM)
        
            print ("Fin du questionnaire")

    def enr(self):
        pass
      



class BoutQuitMESSAGE(Button):
    def __init__(self,fen,**kw):
        Button.__init__(self,fen,text="quitter",command=self.message,**kw)
        self.f=fen
        
    def message(self):
        Message(self.f) ### Si on veut demander "Etes vous sur.. ?"

        
class Message(Toplevel):
    def __init__(self,fen,**kw):
        Toplevel.__init__(self,**kw)
        self.title("Message avant de quitter")
        self.geometry("400x500")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        Label(self,text="Etes-vous sur de vouloir quitter ? \n (Retour au Menu) \n Vos reponses ne seront pas enregistrées.",font=("Calibri",15)).grid(row=0,column=0)
        Button(self,text="Oui",width=20, height=7,command=lambda f1=self,f2=fen:(f1.destroy(),f2.destroy())).grid(row=1,column=0)
        Button(self,text="Non",width=20, height=7,command=self.destroy).grid(row=2,column=0)

class BoutEnregistrer(Button):
    def __init__(self,fen,**kw):
        Button.__init__(self,fen,text="Enregistrer",command=self.enregistrer,**kw)
        self.f=fen
        
    def message(self):
        Enregistrer(self.f) ### Si on veut demander "Etes vous sur.. ?"

  
 
if __name__=='__main__':
    Appli().mainloop()


## toplevel ; fenetre dependant d'une autre


## appli avec reponses

## Application a lancer avec Python 3.4
from Tkinter import *
from random import *

############################################ Fenetre principale de notre application: ##############################################################################
class Appli(Tk):

    def __init__(self,*args,**kw): # pourra prendre autant d'arguments avec et sans valeur par defaut (tuple et dico)
        Tk.__init__(self,*args,**kw)# 1iere chose : appeller le constructeur de la classe mere

        #Image et canevas
        self.Can=Canvas(self,height=120,width=100,bg="white")
        self.Can.grid(row=0,column=0,sticky=NW)
        self.image = PhotoImage(file='im.gif')
        self.Can.create_image(50,60, image = self.image)
        #Label et bouton:
        Label(self,text="Menu \nPrincipal",fg="blue",font=('Verdana', 22,'bold'),bg="white").grid(row=0,column=1,padx=5,pady=25,sticky=N)
        self.Benq1=BoutENQ1(self,height=3,width=15,font=('Verdana',10),bg="light blue").grid(row=1,column=1,padx=10, pady=40)
        self.Benq2=BoutENQ2(self,height=3,width=15,font=('Verdana',10),bg="light blue").grid(row=2,column=1,padx=10, pady=40)
        BoutQuit(self,width=13).grid(row=3,column=2,padx=10,pady=10)
        self.geometry("400x500")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.configure(bg = "white")



#Specialiser le bouton quitter:
class BoutQuit(Button):
    def __init__(self,fen,**kw):
        Button.__init__(self,fen,text="Fermeture \n Application",command=self.quitter,**kw)
        self.f=fen # attribut d'instance f : on sauve la fenetre fen pour les fonctions de toute ma classe

    def quitter(self):
        self.f.quit()
        self.f.destroy()

#Specialiser le bouton enquete relatif a une enquete choisis:
class BoutENQ1(Button):
    def __init__(self,fen,**kw):
        self.text="Enquete1"
        Button.__init__(self,fen,text=self.text,command=self.charger,**kw)
        self.f=fen # attribut d'instance f : on sauve la fenetre fen pour les fonctions de toute ma classe

    def charger(self):
        NomEnq(self.f)

class BoutENQ2(Button):
    def __init__(self,fen,**kw):
        self.text="Enquete2"
        Button.__init__(self,fen,text=self.text,command=self.charger,**kw)
        self.f=fen # attribut d'instance f : on sauve la fenetre fen pour les fonctions de toute ma classe

    def charger(self):
        NomEnq2(self.f)
        
#Specialiser le bouton statistique:
class BoutSTAT(Button):
    def __init__(self,fen,**kw):
        Button.__init__(self,fen,text="Statistique",command=self.charger,**kw)
        self.f=fen

    def charger(self):
        Statistique()
        
#Specialiser le bouton questionnaire:
class BoutNomEnq(Button):
    def __init__(self,fen,**kw):
        Button.__init__(self,fen,text="Questionnaire",command=self.charger,**kw)
        self.f=fen # attribut d'instance f : on sauve la fenetre fen pour les fonctions de toute ma classe

    def charger(self):
        Enquete() #On charge la page du questionnaire de l'enquete

class BoutNomEnq2(Button):
    def __init__(self,fen,**kw):
        Button.__init__(self,fen,text="Questionnaire",command=self.charger,**kw)
        self.f=fen # attribut d'instance f : on sauve la fenetre fen pour les fonctions de toute ma classe

    def charger(self):
        Enquete2() #On charge la page du questionnaire de l'enquete

##################################### DEMARRE LA DEUXIEME FENETRE NOM ENQUETE AVEC POSSIBILITE DE RETOUR ET DE FERMER L'APPLICATION ################################
class NomEnq(Toplevel):
    def __init__(self,fen,nbQuestion=10,**kw):
        Toplevel.__init__(self,fen,**kw)
        self.geometry("400x500")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.title("Que voulez-vous faire sur cette enquete ?")
        self.configure(bg = "white")

        #Image et canevas
        self.Can=Canvas(self,height=120,width=100,bg="white")
        self.Can.grid(row=0,column=0,sticky=NW)
        self.image = PhotoImage(file='im.gif')
        self.Can.create_image(50,60, image = self.image)
        
        Label(self,text="Menu \nEnquete",fg="blue",font=('Verdana', 22, 'bold'),bg="white").grid(row=0,column=1,padx=10, pady=15,sticky=N)
        Benq1=BoutNomEnq(self,height=3,width=15,font=('Verdana',10),bg="light blue").grid(row=1,column=1,padx=8,pady=35,sticky="NSEW") #Envoie l'enqueteur sur la page questionnaire (enquete)
        Benq2=BoutSTAT(self,height=3,width=15,font=('Verdana',10),bg="light blue").grid(row=2,column=1,padx=8,pady=35,sticky="NSEW") #ENvoie l'enqueteur sur la page des statistiques
        #Mise en place d'un bouton retour menu dans l'interface de l'enquete:
        Button(self,text="Retour",width=13,command=self.destroy).grid(row=3,column=0,padx=10,pady=10,sticky=SW)
        #Mise en place d'un bouton fermer application:
        Button(self,text="Fermer \nApplication",width=13,command=lambda f1=self,f2=fen:(f1.destroy(),f2.destroy())).grid(row=3,column=2,padx=10,pady=10)

class NomEnq2(Toplevel):
    def __init__(self,fen,nbQuestion=10,**kw):
        Toplevel.__init__(self,fen,**kw)
        self.geometry("400x500")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.title("Que voulez-vous faire sur cette enquete ?")
        self.configure(bg = "white")

        #Image et canevas
        self.Can=Canvas(self,height=120,width=100,bg="white")
        self.Can.grid(row=0,column=0,sticky=NW)
        self.image = PhotoImage(file='im.gif')
        self.Can.create_image(50,60, image = self.image)
        
        Label(self,text="Menu \nEnquete",fg="blue",font=('Verdana', 22, 'bold'),bg="white").grid(row=0,column=1,padx=10, pady=15,sticky=N)
        Benq1=BoutNomEnq2(self,height=3,width=15,font=('Verdana',10),bg="light blue").grid(row=1,column=1,padx=8,pady=35,sticky="NSEW") #Envoie l'enqueteur sur la page questionnaire (enquete)
        Benq2=BoutSTAT(self,height=3,width=15,font=('Verdana',10),bg="light blue").grid(row=2,column=1,padx=8,pady=35,sticky="NSEW") #ENvoie l'enqueteur sur la page des statistiques
        #Mise en place d'un bouton retour menu dans l'interface de l'enquete:
        Button(self,text="Retour",width=13,command=self.destroy).grid(row=3,column=0,padx=10,pady=10,sticky=SW)
        #Mise en place d'un bouton fermer application:
        Button(self,text="Fermer \nApplication",width=13,command=lambda f1=self,f2=fen:(f1.destroy(),f2.destroy())).grid(row=3,column=2,padx=10,pady=10)

################################## ICI COMMENCE LE CODE STAT A REFAIRE ###########################################################################################
class Statistique(Toplevel):
    pass

################################## ICI COMMENCE LE CODE ENQUETE ##################################################################################################
class Enquete(Toplevel):
    def __init__(self,nbQuestion=10,**kw):
        Toplevel.__init__(self,**kw)
        self.geometry("400x500")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.title("L'enquete est en cours...")
        self.configure(bg = "white")

        #Ecriture dans un fichier texte des reponses
        note="note.txt"
        self.fichier=open(note,'a') # a pour append
        self.listerep=""
        
        #Image du questionnaire:
        self.cQ=Canvas(self,width=100, height=120, background='white')
        self.cQ.grid(column=0,row=0,rowspan=2,padx=5, pady=5, sticky=NW)
        self.image = PhotoImage(file='im.gif')
        self.cQ.create_image(50,60, image = self.image)
        
        #Frame de la question:
        self.fQuest=Frame(self)
        self.fQuest.grid(column=1,row=0,padx=20,pady=10,sticky=N)
        self.fQuest.configure(bg = "white")

        #Lecture du fichier des questions:
        self.Fichier = open('question.txt','r').read().split("\n")
        self.i=0
        self.j=0
        self.f=self.Fichier
        self.q=self.f[self.i]+"\n"+self.f[self.i+1]

        #Frame de la reponse:
        self.fRep=Frame(self)
        self.fRep.grid(column=0,row=1,columnspan=2,padx=10,sticky=NSEW)
        self.fRep.configure(bg = "white")

        #Frame de liste des questions:
        self.fList=Frame(self)
        self.fList.grid(column=2,row=0,rowspan=3,padx=10,pady=5,sticky=E)
        self.fList.configure(bg = "white")

        #Frame du bouton suivant:
        self.fSuiv=Frame(self)
        self.fSuiv.grid(column=0,row=2,columnspan=2,padx=20,pady=20)
        self.fSuiv.configure(bg = "white")


        #Creation de la question:
        Question=Label(self.fQuest,text=self.q,fg="blue",width=25,height=5,relief=RAISED,bg="white").pack(side = TOP)

       
        #Lecture du fichier des réponses:
        self.lignes = open('rep.txt','r').readlines()
        ligne=self.lignes[self.j].split(";")
        self.frep=ligne
        print(self.frep)
        textvar=[]

      
        if (self.frep[0])=="R":
            self.v=IntVar()
            for i in range(int(self.frep[1])):
                textvar+=[str(self.frep[2+i])]
                Radiobutton(self.fRep,text=textvar[i],variable=self.v,width=20, height=5,value=i).pack(side=TOP)

        if (self.frep[0])=="S":
            reponse=StringVar()
            self.v=Entry(self.fRep,textvariable=reponse,bg="white")#,xview_scroll(20,UNITS))
            self.v.focus_set()
            self.v.pack(side=TOP,padx=5,pady=5)

        #CrÃ©ation d'un bouton:
        BoutQuitMESSAGE(self).grid(row=3,column=2,padx=5, pady=5,sticky=SE)
        Button(self.fSuiv,text='Suivante',bg = "light blue",width=10, height=3,command=self.suivant).grid(column=2,row=0,padx=10, pady=10)


        #Liste des questions:
        m=0
        n=(len(self.Fichier)/2)
        while m < n:
            m=m+1
            q=str(m)
            Button(self.fList,text=str("Q"+q),command=lambda l=q:self.question(l)).grid(column=3,row=m)


    def question(self,q):
        print (q)  
        #On supprime les frames:
        self.fQuest.destroy()
        self.fRep.destroy()
        #On remet la frame:
        self.fQuest=Frame(self)
        self.fQuest.grid(column=1,row=0,padx=20,pady=10,sticky=N)
        self.fQuest.configure(bg = "white")
        self.fRep=Frame(self)
        self.fRep.grid(column=1,row=1,columnspan=1,padx=10, pady=10)
        self.fRep.configure(bg = "white")
        self.f=self.Fichier
        #On affiche la question voulue:
        n=int((int(q)-1)*2)
        self.m=self.f[n]+"\n"+self.f[n+1]
        self.Question=Label(self.fQuest,text=self.m,fg="blue",width=25, height=5,relief=RAISED,bg="white").pack(side = BOTTOM)
        #Et donc les réponses possibles:
        ligne=self.lignes[int(q)-1].split(";")
        self.frep=ligne
        textvar=[]
        if (self.frep[0])=="R":
            self.v=IntVar()
            for i in range(int(self.frep[1])):
                textvar+=[str(self.frep[2+i])]
                Radiobutton(self.fRep,text=textvar[i],variable=self.v,width=20, height=5,value=i,bg="white").pack(side=TOP)
        if (self.frep[0])=="S":
            reponse=StringVar()
            self.v=Entry(self.fRep,textvariable=reponse,bg="white")
            self.v.focus_set()
            self.v.pack(side=TOP,padx=5,pady=5)

                
    def quitter(self):
               self.quit()
               self.destroy()

    def suivant(self):
        ## pour voir la reponse a la question precedente :
        print("la reponse : ")
        print(self.v.get())
        self.listerep+=str(self.v.get())+";"
            

        #On detruit la frame actuelle:
        self.fQuest.destroy()
        self.fRep.destroy()
        #On remet la frame:
        self.fQuest=Frame(self)
        self.fQuest.grid(column=1,row=0,padx=20,pady=10,sticky=N)
        self.fQuest.configure(bg = "white")
        self.fRep=Frame(self)
        self.fRep.grid(column=1,row=1,columnspan=1,padx=10, pady=10)
        self.fRep.configure(bg = "white")
        #Mise Ã  jour des questions:
        self.i=self.i+2
        self.j=self.j+1
        n=int(self.i)
        m=int(self.j)

        
        if self.i < (len(self.Fichier)-1):

            self.f=self.Fichier
            self.q=self.f[n]+"\n"+self.f[n+1]
            self.Question=Label(self.fQuest,text=self.q,fg="blue",width=25, height=5,relief=RAISED,bg="white").pack(side = BOTTOM)

            # mise a jour des reponses :
            ligne=self.lignes[m].split(";")
            self.frep=ligne
            print(self.frep)
            textvar=[]
                   
            if (self.frep[0])=="R":
                self.v=IntVar()
                for i in range(int(self.frep[1])):
                    textvar+=[str(self.frep[2+i])]
                    Radiobutton(self.fRep,text=textvar[i],variable=self.v,width=20, height=5,value=i,bg="white").pack(side=TOP)

            if (self.frep[0])=="S":
                reponse=StringVar()
                self.v=Entry(self.fRep,textvariable=reponse,bg="white")#,xview_scroll(20,UNITS))
                self.v.focus_set()
                self.v.pack(side=TOP,padx=5,pady=5)

        else:

            # Detruire les frames existantes::
            self.fSuiv.destroy()
            self.fRep.destroy()
            self.fList.destroy()

            #On recrÃ©e la frame fSuiv pour mettre un bouton enregistrer:
            self.fSuiv=Frame(self)
            self.fSuiv.grid(column=1,row=2,columnspan=1,padx=20, pady=20)
            self.fSuiv.configure(bg = "white")
            Button(self.fSuiv,text='Enregistrer',bg = "light blue",width=10, height=3,command=self.enr).grid(column=2,row=0,padx=10, pady=10)

            #On recrÃ©e la frame FRep pour mettre un texte de remerciement:
            self.fRep=Frame(self)
            self.fRep.grid(column=1,row=1,columnspan=1,padx=10, pady=10)
            self.fRep.configure(bg = "white")
            Label(self.fRep,text="Voulez vous enregistrer  \n vos reponses. \n \n Merci d'avoir repondu \n au questionnaire !",bg="white",fg="blue",relief=RAISED,width=20, height=15).pack(side = BOTTOM)
        
            print ("Fin du questionnaire")
      
    def enr(self):
        self.fichier.write(self.listerep+"\n") #ligne du fichier texte pour un individu
        self.fichier.close()
        self.destroy()


################################## ICI COMMENCE LE CODE ENQUETE2 ##################################################################################################
class Enquete2(Toplevel):
    def __init__(self,nbQuestion=10,**kw):
        Toplevel.__init__(self,**kw)
        self.geometry("400x500")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.title("L'enquete 2 est en cours...")
        self.configure(bg = "white")

        #Ecriture dans un fichier texte des reponses
        note="note2.txt"
        self.fichier=open(note,'a') # a pour append
        self.listerep=""
        
        #Image du questionnaire:
        self.cQ=Canvas(self,width=100, height=120, background='white')
        self.cQ.grid(column=0,row=0,rowspan=2,padx=5, pady=5, sticky=NW)
        self.image = PhotoImage(file='im.gif')
        self.cQ.create_image(50,60, image = self.image)
        
        #Frame de la question:
        self.fQuest=Frame(self)
        self.fQuest.grid(column=1,row=0,padx=20,pady=10,sticky=N)
        self.fQuest.configure(bg = "white")

        #Lecture du fichier des questions:
        self.Fichier = open('question2.txt','r').read().split("\n")
        self.i=0
        self.j=0
        self.f=self.Fichier
        self.q=self.f[self.i]+"\n"+self.f[self.i+1]

        #Frame de la reponse:
        self.fRep=Frame(self)
        self.fRep.grid(column=0,row=1,columnspan=2,padx=10,sticky=NSEW)
        self.fRep.configure(bg = "white")

        #Frame de liste des questions:
        self.fList=Frame(self)
        self.fList.grid(column=2,row=0,rowspan=3,padx=10,pady=5,sticky=E)
        self.fList.configure(bg = "white")

        #Frame du bouton suivant:
        self.fSuiv=Frame(self)
        self.fSuiv.grid(column=0,row=2,columnspan=2,padx=20,pady=20)
        self.fSuiv.configure(bg = "white")


        #Creation de la question:
        Question=Label(self.fQuest,text=self.q,fg="blue",width=25,height=5,relief=RAISED,bg="white").pack(side = TOP)

       
        #Lecture du fichier des réponses:
        self.lignes = open('rep2.txt','r').readlines()
        ligne=self.lignes[self.j].split(";")
        self.frep=ligne
        print(self.frep)
        textvar=[]

      
        if (self.frep[0])=="R":
            self.v=IntVar()
            for i in range(int(self.frep[1])):
                textvar+=[str(self.frep[2+i])]
                Radiobutton(self.fRep,text=textvar[i],variable=self.v,width=20, height=5,value=i).pack(side=TOP)

        if (self.frep[0])=="S":
            reponse=StringVar()
            self.v=Entry(self.fRep,textvariable=reponse,bg="white")#,xview_scroll(20,UNITS))
            self.v.focus_set()
            self.v.pack(side=TOP,padx=5,pady=5)

        #CrÃ©ation d'un bouton:
        BoutQuitMESSAGE(self).grid(row=3,column=2,padx=5, pady=5,sticky=SE)
        Button(self.fSuiv,text='Suivante',bg = "light blue",width=10, height=3,command=self.suivant).grid(column=2,row=0,padx=10, pady=10)


        #Liste des questions:
        m=0
        n=(len(self.Fichier)/2)
        while m < n:
            m=m+1
            q=str(m)
            Button(self.fList,text=str("Q"+q),command=lambda l=q:self.question(l)).grid(column=3,row=m)


    def question(self,q):
        print (q)
        #On supprime les frames:
        self.fQuest.destroy()
        self.fRep.destroy()
        #On remet la frame:
        self.fQuest=Frame(self)
        self.fQuest.grid(column=1,row=0,padx=20,pady=10,sticky=N)
        self.fQuest.configure(bg = "white")
        self.fRep=Frame(self)
        self.fRep.grid(column=1,row=1,columnspan=1,padx=10, pady=10)
        self.fRep.configure(bg = "white")
        self.f=self.Fichier
        #On affiche la question voulue:
        n=int((int(q)-1)*2)
        self.m=self.f[n]+"\n"+self.f[n+1]
        self.Question=Label(self.fQuest,text=self.m,fg="blue",width=25, height=5,relief=RAISED,bg="white").pack(side = BOTTOM)
        #Et donc les réponses possibles:
        ligne=self.lignes[int(q)-1].split(";")
        self.frep=ligne
        textvar=[]
        if (self.frep[0])=="R":
            self.v=IntVar()
            for i in range(int(self.frep[1])):
                textvar+=[str(self.frep[2+i])]
                Radiobutton(self.fRep,text=textvar[i],variable=self.v,width=20, height=5,value=i,bg="white").pack(side=TOP)
        if (self.frep[0])=="S":
            reponse=StringVar()
            self.v=Entry(self.fRep,textvariable=reponse,bg="white")
            self.v.focus_set()
            self.v.pack(side=TOP,padx=5,pady=5)
        
    def quitter(self):
               self.quit()
               self.destroy()

    def suivant(self):
        ## pour voir la reponse a la question precedente :
        print("la reponse : ")
        print(self.v.get())
        self.listerep+=str(self.v.get())+";"
            

        #On detruit la frame actuelle:
        self.fQuest.destroy()
        self.fRep.destroy()
        #On remet la frame:
        self.fQuest=Frame(self)
        self.fQuest.grid(column=1,row=0,padx=20,pady=10,sticky=N)
        self.fQuest.configure(bg = "white")
        self.fRep=Frame(self)
        self.fRep.grid(column=1,row=1,columnspan=1,padx=10, pady=10)
        self.fRep.configure(bg = "white")
        #Mise Ã  jour des questions:
        self.i=self.i+2
        self.j=self.j+1
        n=int(self.i)
        m=int(self.j)

        
        if self.i < (len(self.Fichier)-1):

            self.f=self.Fichier
            self.q=self.f[n]+"\n"+self.f[n+1]
            self.Question=Label(self.fQuest,text=self.q,fg="blue",width=25, height=5,relief=RAISED,bg="white").pack(side = BOTTOM)

            # mise a jour des reponses :
            ligne=self.lignes[m].split(";")
            self.frep=ligne
            print(self.frep)
            textvar=[]
                   
            if (self.frep[0])=="R":
                self.v=IntVar()
                for i in range(int(self.frep[1])):
                    textvar+=[str(self.frep[2+i])]
                    Radiobutton(self.fRep,text=textvar[i],variable=self.v,width=20, height=5,value=i,bg="white").pack(side=TOP)

            if (self.frep[0])=="S":
                reponse=StringVar()
                self.v=Entry(self.fRep,textvariable=reponse,bg="white")#,xview_scroll(20,UNITS))
                self.v.focus_set()
                self.v.pack(side=TOP,padx=5,pady=5)

        else:

            # Detruire les frames existantes::
            self.fSuiv.destroy()
            self.fRep.destroy()
            self.fList.destroy()

            #On recrÃ©e la frame fSuiv pour mettre un bouton enregistrer:
            self.fSuiv=Frame(self)
            self.fSuiv.grid(column=1,row=2,columnspan=1,padx=20, pady=20)
            self.fSuiv.configure(bg = "white")
            Button(self.fSuiv,text='Enregistrer',bg = "light blue",width=10, height=3,command=self.enr).grid(column=2,row=0,padx=10, pady=10)

            #On recrÃ©e la frame FRep pour mettre un texte de remerciement:
            self.fRep=Frame(self)
            self.fRep.grid(column=1,row=1,columnspan=1,padx=10, pady=10)
            self.fRep.configure(bg = "white")
            Label(self.fRep,text="Voulez vous enregistrer  \n vos reponses. \n \n Merci d'avoir repondu \n au questionnaire !",bg="white",fg="blue",relief=RAISED,width=20, height=15).pack(side = BOTTOM)
        
            print ("Fin du questionnaire")
      
    def enr(self):
        self.fichier.write(self.listerep+"\n") #ligne du fichier texte pour un individu
        self.fichier.close()
        self.destroy()

        
class BoutQuitMESSAGE(Button):
    def __init__(self,fen,**kw):
        Button.__init__(self,fen,text="quitter",command=self.message,**kw)
        self.f=fen
        
    def message(self):
        Message(self.f) ### Si on veut demander "Etes vous sur.. ?"

        
class Message(Toplevel):
    def __init__(self,fen,**kw):
        Toplevel.__init__(self,**kw)
        Toplevel.__init__(self,**kw)
        self.configure(bg="white")
        self.title("ATTENTION FERMETURE ENQUETE!")
        self.geometry("300x250")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        Label(self,text="Etes-vous sur \n de vouloir quitter ? \n (Retour au Menu) \n \n Vos reponses ne seront \n pas enregistrÃ©es.",bg="white",font=("arial",12)).grid(row=0,column=0,columnspan=2,sticky=NSEW)
        Button(self,text="Non",font="arial 12 bold",width=10,bg="light blue", height=2,command=self.destroy).grid(row=1,sticky=NSEW,column=0,padx=10,pady=10)
        Button(self,text="Oui",width=10, bg="light blue",height=2,command=lambda f1=self,f2=fen:(f1.destroy(),f2.destroy())).grid(row=1,sticky=NSEW,column=1,padx=10,pady=10)
              

 
if __name__=='__main__':
    Appli().mainloop()


## toplevel ; fenetre dependant d'une autre

################################
##                                  ##
##   TP systeme recommandation      ##
##                                  ##
################################

# -*- coding: utf-8 -*-
## systeme de recommandation

## ensemble temoin
G=[17,98,2,34,47]
# l'utilisateur devra ordonner cet ens
# puis donner ses 5 nombres favoris

## demander à l'utilisateur de classer l'echantillon
print("Classez cet echantillon de nombre 17,98,2,34,47  ")
c17 = int(input("classement de 17 : "))
c98 = int(input("classement de 98 : "))
c2 = int(input("classement de 2 : "))
c34 = int(input("classement de 34 : "))
c47 = int(input("classement de 47 : "))
classement=str(c17)+" "+str(c98)+" "+str(c2)+" "+str(c34)+" "+str(c47)+" "+"\n"
print "votre classement est : "
print classement


## demander ses 5 nombres favoris entre 0 et 100
print("Quels sont vos 5 nombres favoris entre 0 et 100  ")
p1 = int(input("le premier : "))
p2 = int(input("le deuxieme : "))
p3 = int(input("le troisieme : "))
p4 = int(input("le quatrieme : "))
p5 = int(input("le cinquieme : "))
favori=str(p1)+" "+str(p2)+" "+str(p3)+" "+str(p4)+" "+str(p5)+" "+"\n"
print "votre classement préféré est : "
print favori


## ecriture dans un fichier texte des notes
note="note.txt"
fichier=open(note,'a') # a pour append
fichier.write(classement) #1ere ligne du fichier texte pour un individu
fichier.close()

## ecriture dans un fichier texte des recommandations
rec="rec.txt"
fichier=open(rec,'a') # a pour append
fichier.write(favori) #2eme ligne du fichier texte pour le meme individu
fichier.close()

## pour calculer le score d'un individu
## on multiplie classement * (Mat_classement)= vect(score)
# on regarde le score max pour faire un recommandation soit les nombres préférés
# (la ligne correspondant dans la matrice)

## suite TP voir recommandation.py


# -*- coding: utf-8 -*-

## apres avoir lancé le script 3 fois pour avoir qqe lignes dans la matrice.

# on effectue l'etape ou on veut faire une  recommandation :

## demander à l'utilisateur de classer l'echantillon
print("Classez cet echantillon de nombre 17,98,2,34,47  ")
c17 = int(input("classement de 17 : "))
c98 = int(input("classement de 98 : "))
c2 = int(input("classement de 2 : "))
c34 = int(input("classement de 34 : "))
c47 = int(input("classement de 47 : "))
classement=str(c17)+" "+str(c98)+" "+str(c2)+" "+str(c34)+" "+str(c47)+"\n"
print "votre classement est : "
print classement

## on va parcourir le fichier pour calculer le score toutes les deux lignes
fichier = open('note.txt', 'r')

vect_score=[]
classement=classement.split()
print(classement)
        
#On lit chaque ligne du fichier
for ligne in fichier.readlines() :
    if len(ligne) != 0 :
    #On scinde la ligne
        donnee = ligne.split(" ")
        print(donnee)
        donnee=donnee[0:5]
        print(donnee)
        score=0
        for i in range(len(classement)):
            score+=int(classement[i])*int(donnee[i])
        vect_score+=[score]
print("les scores sont : ")
print(vect_score)


fichier.close()


# trouver l'index du score max
ind=vect_score.index(max(vect_score))
print(ind)

# index * 2 pour retrouver la recommandation
fichier = open('rec.txt', 'r')
for i in (range(ind)):
    ligne=fichier.readline()
print "la recommandation est : "
print ligne
fichier.close()


################
##            ##
##   FIN      ##
## Master M2  ## S2
##            ##
################



## Drag n drop ##

from Tkinter import *
class CanvasDnD(Canvas):
    
    def movable(self,*args):
        for o in args: ## pour parcourir les objets
            self.tag_bind(o,"<Button-1>",self.__drag)
            self.tag_bind(o,"<Button1-ButtonRelease>",self.__release)
        

    def unmovable(self,*args):
        for o in args: ## pour parcourir les objets
            self.tag_unbind(o,"<Button-1>")
            self.tag_unbind(o,"<Button1-ButtonRelease>")


    ## les handlers : les methodes qui réagissent
    
    def __drag(self,event):
        ## il faut sauver les objets et coords
        self.__o=CURRENT ## le dernier objet que a subit qqch = celui qu'on a clické
        ## si on voulait faire ça avec un widget : self.__w=event.widget
        self.__x=event.x
        self.__y=event.y
        ## pour prendre l'objet et capter ses mouvements on se sert ensuite de __drop
        self.bind("<Button1-Motion>",self.__drop)
        

    def __drop(self,event):
        ## pour capter les mouvements de la souris
        self.move(self.__o,event.x-self.__x,event.y-self.__y)
        self.__x=event.x
        self.__y=event.y
        
    
    def __release(self,event):
        self.unbind("<Button1-Motion>")

## Application
class fenApp(Tk):
    def __init__(self,*args,**argw):
        Tk.__init__(self,*args,**argw)
        self.can=CanvasDnD(self,width=500,height=500,bg="light grey")
        self.can.pack()
        Button(self,text="quitter",command=self.quitter).pack()
        self.can.movable(self.can.create_oval(240,240,260,260,fill="red"),self.can.create_oval(140,140,160,160,fill="white"))

    def quitter(self):
        self.quit()
        self.destroy()

if __name__=="__main__":
    fenApp().mainloop()
