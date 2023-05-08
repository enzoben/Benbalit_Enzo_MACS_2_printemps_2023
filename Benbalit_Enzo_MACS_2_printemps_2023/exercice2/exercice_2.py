import numpy as np
import numpy.random as rnd
import math

def pos(a,b):
    return max(a-b,0)

def binom(n,k):
    #retourne le coeficient binomial de k parmis n
    return math.factorial(n)/(math.factorial(n-k)*math.factorial(k))

def Value_Call(N,n,r,p,u,d,Sn,K):
    #donne la valeur d'un Call de prix d'exercice K et d'echeance T=1 a l'instant n
    Cn=0
    for k in range(N-n+1):
        Cn=Cn+binom(N-n,k)*pos(Sn*math.pow(u,k)*math.pow(d,N-n-k),K)*math.pow(p,k)*math.pow(1-p,N-n-k)
    return Cn/math.pow(1+r,N-n)

def Value_Put(Cn,K,N,r,n,Sn):
    #donne la valeur d'un Put a l'instant n par la relation Call-Put
    return Cn-Sn+K/math.pow(1+r,N-n)

def qteActifs(N,n,r,p,u,d,Sn_1,K):
    #fonction qui donne la quantite d'actif risque et non rique a detenir a l'instant n
    #afin d'avoir la couverture appropriee
    # Hn : la qte d'actif risque pour le Call
    # H0 : la qte d'actif non-risque pour le Call
    # Jn : la qte d'actif risque pour le Put
    # J0 : la qte d'actif non-risque pour le Put
    C_u=Value_Call(N,n,r,p,u,d,u*Sn_1,K)
    C_d=Value_Call(N,n,r,p,u,d,d*Sn_1,K)
    A=math.pow(1+r,n)
    Hn=(C_d-C_u)/((d-u)*Sn_1)
    H0=(d*C_u-u*C_d)/((d-u)*A)
    Jn=Hn-1
    J0=H0+K/math.pow(1+r,N)
    return Hn, H0, Jn, J0

def pricerOption(S_0,r,s,K,N):
    # Cette fonction est un pricer d'option (Call et Put europeen) 
    # qui donne aussi a chaque etape la quantitee d'actifs risque et non-risque
    #  a detenir afin de fournir la couverture approprie
    
    #Ce pricer d'option n'evalue qu'un seul chemin qui est "tire" au hasard.
    
    #C_n : vecteur qui contient le prix du Call europeen c(n,S_n) a chaque instant
    #P_n : vecteur qui contient le prix du Put a chaque instant
    #Sn : vecteur qui contient la valeur de l'option a chaque instant
    #UD : vecteur de taille N qui contient l'information pour si S_n est monte ou descendu
    #     UD[i]=1 => S_n[i+1]=u*S_n[i] , i \in [0,N-1]
    
    # H_n : la qte d'actif risque pour le Call
    # H0 : la qte d'actif non-risque pour le Call
    # J_n : la qte d'actif risque pour le Put
    # J0 : la qte d'actif non-risque pour le Put
    
    dt=1/N
    u=np.exp(s*np.sqrt(dt))
    d=np.exp(-s*np.sqrt(dt))
    p=(1+r-d)/(u-d)
    
    UD=np.zeros(N)
    C_n=np.zeros(N)
    P_n=np.zeros(N)
    Sn=np.zeros(N+1)
    H_n=np.zeros(N)
    H0=np.zeros(N)
    J_n=np.zeros(N)
    J0=np.zeros(N)
    Sn[0]=S_0
    
    for i in range(N):
        if rnd.rand()<p:
            Sn[i+1]=u*Sn[i]
            UD[i]=1
        else :
            Sn[i+1]=d*Sn[i]
            UD[i]=-1
        C_n[i]=Value_Call(N,i+1,r,p,u,d,Sn[i+1],K)
        P_n[i]=Value_Put(C_n[i],K,N,r,i+1,Sn[i+1])
        A,B,C,D=qteActifs(N,i+1,r,p,u,d,Sn[i],K)
        H_n[i]=A
        H0[i]=B
        J_n[i]=C
        J0[i]=D
    return Sn,C_n,P_n,H_n,H0,J_n,J0,UD,p,u,d


        
        
        



