import numpy as np
import question2a as q2a

### QUESTION (b)
def simulerSt(r,s,T,n,S0):
    #on simule notre mouvement brownien W_t puis on calcul S_t
    #qui est une "fonction" de W_t
    W=q2a.simulerBrownien(T,n)
    h=T/n
    St=np.zeros(n+1)
    for i in range(n+1):
        St[i]=S0*np.exp(s*W[i]+(r-(s*s/2)*i*h))
    return St

## QUESTION (c)
def simulerXTseed(S_t,r,s,S0,K,B,T): 
# permets de simuler une realisation de X_T
    ST=0                     
    if max(S_t[-1]-K,0.)!=0 and max(S_t)>B:
        ST=np.exp(-r*T)*(S_t[-1]-K) #S_t[-1] donne le dernier elements 
    return ST
    
def prixBarriere(r,s,S0,K,B,n,T):
    #on simule piT et sig2 par la methode de monte-carlo
    #on a piT l'esperance empirique et sig2 la variance empirique
    piT=0
    sig2=0
    ST=np.zeros(n)
    S_t=np.zeros(n)
    for i in range(n):
        S_t=simulerSt(r,s,T,n,S0)
        ST[i]=simulerXTseed(S_t,r,s,S0,K,B,T) #on garde en memoire chaque X_t
        piT=piT+ST[i]                         #afin de calculer sig2 avec le
    piT=piT/n                                 #meme n-echantillon de X_t
    
    for i in range(n):
        sig2=sig2+(ST[i]-piT)*(ST[i]-piT)
    sig2=sig2/n
    
    IC=[piT-1.96*np.sqrt(sig2/n),piT+1.96*np.sqrt(sig2/n)]
    IC[0]=max(0.,IC[0]) #etant donner que X_t>=0, on peut rogner l'IC 
    return piT,sig2,IC  #sans perte de precision !

def prixBarriereMaturite(r,s,S0,K,B,n,T):
    #on calcul a chaque etape le nouveau prix barriere pour le 
    #temps (i+1)*h independament des precedents
    h=T/n
    pi=np.zeros(n)
    for i in range(n):
        A=prixBarriere(r,s,S0,K,B,n,(i+1)*h)
        pi[i]=A[0] #le premier element de A est le prix barriere
    return pi

    
    