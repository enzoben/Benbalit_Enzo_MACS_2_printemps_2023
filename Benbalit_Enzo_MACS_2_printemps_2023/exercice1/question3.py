import numpy as np
import question2bc as q2bc

def int_trapeze(St,T):
    #calcul par la methode des trapezes l'approximation
    #de l'integrale de St dans [0,T]
    N2=np.size(St)
    h2=T/N2
    I=0
    for i in range(N2-1):
        I=I+(St[i]+St[i+1])
    I=I*(h2/2)
    return I

def XTseed_int(I,St,T,K,B,r):
    #calcul l'interieur de l'esperance 
    #si la condition du if n'est pas respecter alors Xt=0
    Xt=0
    if max((1/T)*I-K,0)!=0 and max(St)>B:
        Xt=np.exp(-r*T)*((1/T)*I-K)
    return Xt

def prixBarriereAsiatique(r,s,S0,K,B,N1,N2,T):
    #calcul du prix barriere de l'option asiatique pour un temps fixe
    #par la methode de monte-carlo
    piT=0 
    for i in range(N1):
        #a chaque etape on calcul un nouvel St et son integral approche par
        #la methode des trapezes, puis on calcule Xt
        St=q2bc.simulerSt(r,s,T,N2,S0)
        I=int_trapeze(St,T)
        Xt=XTseed_int(I,St,T,K,B,r)
        piT=piT+Xt
    piT=piT/N1
    return piT

def prixBarriereAsiatiqueMaturite(r,s,S0,K,B,N1,N2,T,N3):
    #a chaque etape on calcul \bar{\pi_{b_i}} independament des valeurs precedentes
    h=T/N3
    PB=np.zeros(N3)
    for i in range(N3):
        PB[i]=prixBarriereAsiatique(r,s,S0,K,B,N1,N2,(i+1)*h)
    return PB
