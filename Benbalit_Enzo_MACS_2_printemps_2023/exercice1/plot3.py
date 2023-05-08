import numpy as np
import matplotlib.pyplot as plt
import question3 as q3

N1=500
N2=200
N3=10
T=5
h=T/N3
r=0.05
s=2
S0=100
K=95
B=105

##plot option asiatique
Index= [(s+1)*h for s in range(N3)]
S=q3.prixBarriereAsiatiqueMaturite(r,s,S0,K,B,N1,N2,T,N3)
fig, a2=plt.subplots()
a2.plot(Index,S,color='blue',label=r'$\bar{\pi_t}$')
plt.title(r'prix barriere option asiatique')
plt.xlabel("t")
plt.ylabel("y")
plt.legend()
plt.show()