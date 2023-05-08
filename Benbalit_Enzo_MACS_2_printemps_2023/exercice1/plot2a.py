import numpy as np
import matplotlib.pyplot as plt
import question2a as q2a


#test
##plot pour (a)
n=10000
T=5
h=T/n
Index= [s*h for s in range(n+1)]
W=q2a.simulerBrownien(T,n)
fig, a1=plt.subplots()
a1.plot(Index,W,color='blue',label=r'$W_t$')
a1.plot(Index,1.96*np.sqrt(Index), color='green',label=r'$1,96 \frac{1}{\sqrt{x}}$')
a1.plot(Index,-1.96*np.sqrt(Index),color='green',label=r'$-1,96 \frac{1}{\sqrt{x}}$')
plt.title("représentation graphique d'un mouvement brownien issu de 0")
plt.xlabel("t")
plt.ylabel("y")
plt.legend()
plt.show()

