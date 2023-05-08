import numpy as np
import matplotlib.pyplot as plt
import question2d as q2d

n=100
T=5
h=T/n
r=0.05
s=2
S0=100
K=95
B=105

##plot prix barriere par les variables antithetique
E,Sig2,IC=q2d.prixBarriereREDUCTVAR(r,s,S0,K,B,n,T)
print(f"esp:{E} \n")
print(f"sig2={Sig2}\n")
print(f"IC = [{IC[0]},{IC[1]}]")