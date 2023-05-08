import numpy as np
import question2a as q2a
import question2bc as q2bc

### QUESTION (d)
def simulerStSeed(W,r,s,T,S0):
    #cette fonction donne la valeur de S_t pour un W_t 
    #bien precis
    n=len(W)
    h=T/(n-1)
    St=np.zeros(n)
    for i in range(n):
        St[i]=S0*np.exp(s*W[i]+(r-(s*s/2)*i*h))
    return St

def prixBarriereREDUCTVAR(r,s,S0,K,B,n,T):
    #on commence par simuler un n-echantillon de loi W et l'on calcul
    #S_t(W_t) et S_t(-W_t) afin de pouvoir faire la reduction de variance
    piT=0
    sig2=0
    ST1=np.zeros(n)
    S_T1=np.zeros(n)
    ST2=np.zeros(n)
    S_T2=np.zeros(n)
    
    for i in range(n):
        W=q2a.simulerBrownien(T,n)
        ST1=simulerStSeed(W,r,s,T,S0) #S_t(W_t)
        ST2=simulerStSeed(-W,r,s,T,S0)#S_t(-W_t)
        S_T1[i]=q2bc.simulerXTseed(ST1,r,s,S0,K,B,T) #calcul de X_t pour W_t
        S_T2[i]=q2bc.simulerXTseed(ST2,r,s,S0,K,B,T) #calcul de X_t pour -W_t
        piT=piT+(S_T1[i]+S_T2[i])/2 #formule de reduction de variance
    piT=piT/n
    
    for i in range(n):
        sig2=sig2+(((S_T1[i]+S_T2[i])/2)-piT)**2
    sig2=sig2/(n-1)
    
    IC=[piT-1.96*np.sqrt(sig2/n),piT+1.96*np.sqrt(sig2/n)]
    IC[0]=max(0.,IC[0]) #ici aussi l'IC peut etre rogner sans perte de precision
    return piT,sig2,IC