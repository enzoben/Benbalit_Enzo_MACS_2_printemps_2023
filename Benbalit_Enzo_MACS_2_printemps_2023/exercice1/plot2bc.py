import numpy as np
import matplotlib.pyplot as plt
import question2bc as q2bc


n=100
T=5
h=T/n
r=0.05
s=2
S0=100
K=95
B=105

##plot question (b)

###plot St
# Index= [s*h for s in range(n+1)]
# S=q2bc.simulerSt(r,s,T,n,S0)
# fig, a2=plt.subplots()
# a2.plot(Index,S,color='blue',label=r'$S_t$')
# plt.title(r'représentation dans le temps de notre mouvement brownien géométrique $S_t$')
# plt.xlabel("t")
# plt.ylabel("y")
# plt.legend()
# plt.show()

###plot prixBarriere
E,Sig2,IC=q2bc.prixBarriere(r,s,S0,K,B,n,T)
print(f"esp:{E} \n")
print(f"sig2={Sig2}\n")
print(f"IC = [{IC[0]},{IC[1]}]")

##plot question (c)

# p=q2bc.prixBarriereMaturite(r,s,S0,K,B,n,T)
# Index= [(s+1)*h for s in range(n)]
# fig, a3=plt.subplots()
# a3.plot(Index,p,color='blue',label=r'$\pi_t$')
# plt.title(r'représentation dans le temps du prix de notre option barrière $\pi_t$')
# plt.xlabel("t")
# plt.ylabel("y")
# plt.legend()
# plt.show()

### affichage d'une série de X_T
# for i in range(10):
#     S_t=q2bc.simulerSt(r,s,T,n,S0)
#     x=q2bc.simulerXTseed(S_t,r,s,S0,K,B,T)
#     print(f"{x} \n")
