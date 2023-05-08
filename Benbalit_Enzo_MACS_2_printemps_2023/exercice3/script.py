from math import nan
import question1 as q1
import question2 as q2
import numpy as np

#######################
# #question 1
# P = [0.1, 0.15, 0.3, 0.25, 0.2]
# F,G=q1.Calcul_fg(P)
########################

###########################
#question 2
P=[0.1,0.08,0.5,0.1,0.22]
a=40
b=60
r=220
F,G=q2.Calcul_fg(P,a,b,r)
##########################

n=len(P)
rt=np.zeros(n)
rt[0]=nan
for i in range(1,n):
    rt[i]=F[i]/G[i]
abs_r=[abs(x-1) for x in rt[1:]]
    
#écriture dans un fichier texte "result2" du tableau des différents profits
fichier=open("result_ex3.txt","w")
fichier.write("Voici un tableau contenant l'ensemble des profits réalisable aisni que leurs risques en fonction du stock s\n")
fichier.write("\n")
fichier.write(f"Ici, les probas sont P=[ {P[0]} | {P[1]} | {P[2]} | {P[3]} | {P[4]} ]\n")
fichier.write("\n")
##########################
fichier.write(f"les frais d'exploitation a={a}\n")
fichier.write(f"les frais fixes b={b}\n")
fichier.write(f"le prix d'une location r={r}\n")
#########################
fichier.write("\n")
fichier.write("s | f(s) | g(s) | ratio \n")
for i in range(n):
    fichier.write(f"{i} | {F[i]:.2f} | {G[i]:.2f} | {rt[i]:.2f} \n")
fichier.write("\n")
fichier.write("\n")
fichier.write(f"Ainsi la valeur de s qui maximise le profit tout en minimisant les risques est s= {abs_r.index(min(abs_r))+1}\n")
fichier.close()
