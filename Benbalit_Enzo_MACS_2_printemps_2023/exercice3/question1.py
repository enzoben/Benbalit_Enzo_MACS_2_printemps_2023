import numpy as np

def espX(p,s):
    #cette fonction nous donne E[X*indicatrice(X<=s)]
    esp=0
    i=1
    while i<=s:
        esp=esp+i*p[i]
        i=i+1
    return esp

def espX2(p,s):
    #cette fonction nous donne E[X^2*indicatrice(X<=s)]
    esp=0
    i=1
    while i<=s:
        esp=esp+i*i*p[i]
        i=i+1
    return esp

def fg(p,s):
    #cette fonction nous donne la valeur de f(s) et g(s)
    esp=espX(p,s)
    f=100*esp-20*s
    g=100*np.sqrt(espX2(p,s)-esp*esp)
    return f,g

def Calcul_fg(p):
    #Cette fonction retourne des vecteurs de taille 5 
    #tq: F[i]=f(i) et G[i]=g(i)
    F=np.zeros(5)
    G=np.zeros(5)
    for s in range(5):
        F[s],G[s]=fg(p,s)
        
    return F,G