
import os 

# Initialisation des données
print ("Entrez le texte à crypter en sans ponctuation")
Texte=input()

TexteClair=Texte.upper()

lg_tc=len(TexteClair)
print ("Entrez le mot de codage")
Clein=input()
Cle=Clein.upper()

lg_C=len(Cle)
bl=0                   # variable pour stockage du nombre d'espaces
TexteCrypte=""

# Cryptage
for i in range(lg_tc):
    lettre=TexteClair[i]
    if lettre==" ":
        bl+=1
        TexteCrypte+=" "
    else:
        j=(i-bl)%lg_C
        k=ord(Cle[j])
        h=ord(lettre)
        asc=k+h
        TexteCrypte+= chr(asc-52*((asc<65)-(asc>90)))
        #TexteCrypte+= chr(asc-26*((asc<65)-(asc>90)))
# Affichages

print ("             Clé :")
print (Cle)
print
print ("             Texte crypté :")
print (TexteCrypte)


os.system("pause")
