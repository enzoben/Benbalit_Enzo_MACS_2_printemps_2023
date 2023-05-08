import numpy as np
import question1 as q1

def fg(a,b,r,p,s):
    #cette fonction retourne la valeur de f(s) et g(s)
    #r : le prix de la location journaliere
    #a : les frais d'exploitation
    #b : les frais fixe
    esp=q1.espX(p,s)
    f=(r-a)*esp-b*s
    g=(r-a)*np.sqrt(q1.espX2(p,s)-esp*esp)
    return f,g

def Calcul_fg(p,a,b,r):
    #Cette fonction retourne des vecteurs de taille 5 
    #tq: F[i]=f(i) et G[i]=g(i)
    #r : le prix de la location journaliere
    #a : les frais d'exploitation
    #b : les frais fixe
    F=np.zeros(5)
    G=np.zeros(5)
    for s in range(5):
        F[s],G[s]=fg(a,b,r,p,s)
    return F,G
    