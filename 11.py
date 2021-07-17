R1=float(input("please entre resistances R1"))
R2=float(input("please entre resistances R2"))
R3=float(input("please entre resistances R3"))

RenSerie=R1+R2+R3
Renparallele=(R1+R2+R3)/(R1*R2+R1*R3+R3*R2)

print(f"les résistances en série :{RenSerie}")
print(f"les résistances en parallèle :{Renparallele}")


#Comment calculer la valeur de résistances en série ou en dérivation
#https://fr.wikihow.com/calculer-la-valeur-de-r%C3%A9sistances-en-s%C3%A9rie-ou-en-d%C3%A9rivation