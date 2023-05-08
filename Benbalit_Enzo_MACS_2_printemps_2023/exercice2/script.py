import exercice_2 as ex2

s=4.40
r=0.95
K=66
S0=86
N=10

Sn,C_n,P_n,H_n,H0,J_n,J0,UD,p,u,d=ex2.pricerOption(S0,r,s,K,N)

## ecriture dans un fichier texte de l'ensemble des valeurs dans un tableau organisé
fichier = open("result_pricer.txt","w")
fichier.write("Fichier qui contient l'évolution à chaque instant des différentes valeurs du Call,\n du Put, de la quantité d'actifs risqués et non risqués à détenir et\n qui décris aussi l'état de l'actif risqué (s'il est monté ou descendu). \n")
fichier.write("\n")
fichier.write(f"s={s:.2f}\n")
fichier.write(f"r={r:.2f}\n")
fichier.write(f"K={K:.2f}\n")
fichier.write(f"S0={S0:.2f}\n")
fichier.write(f"N={N:.2f}\n")
fichier.write("\n")
fichier.write(f"p={p:.2f}\n")
fichier.write(f"u={u:.2f}\n")
fichier.write(f"1+r={1+r}\n")
fichier.write(f"d={d:.2f}\n")
fichier.write("\n")
fichier.write("S_n : valeur à l'instant i de l'actif risqué\n")
fichier.write("C_n : valeur à l'instant i du Call Européen\n")
fichier.write("P_n : valeur à l'instant i du Put Européen\n")
fichier.write("H0 : la quantité d’actifs non risqués à détenir à l’instant i pour avoir la couverture appropriée dans le cas d'un Call\n")
fichier.write("H_n : la quantité d’actifs risqués à détenir à l’instant i pour avoir la couverture appropriée dans le cas d'un Call\n")
fichier.write("J0 : la quantité d’actifs non risqués à détenir à l’instant i pour avoir la couverture appropriée dans le cas d'un Put\n")
fichier.write("J_n : la quantité d’actifs risqués à détenir à l’instant i pour avoir la couverture appropriée dans le cas d'un Put\n")
fichier.write("\n")
fichier.write("\n")
fichier.write("i | S_n | C_n | P_n | H0 | H_n | J0 | J_n\n")
ku=0
kd=0
for i in range(1,N+1):
    if UD[i-1]==1:
        ku=ku+1
    else : 
        kd=kd+1
    fichier.write(f"{i} | S_0*u^{ku}*d^{kd}={Sn[i]:.2f} | {C_n[i-1]:.2f} | {P_n[i-1]:.2f} | {H0[i-1]:.2f} | {H_n[i-1]:.2f} | {J0[i-1]:.2f} | {J_n[i-1]:.2f}\n")
fichier.close()
