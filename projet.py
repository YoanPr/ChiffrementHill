import numpy as np

def motEnNombre(mot):
    mot = mot.upper()
    lettreNombre = []
    for i in range(0, len(mot)):
        lettreNombre.append(ord(mot[i]) - 65)
    return lettreNombre

def definitionMatrice():
    a = int(input("Entrez la premiere valeur de la matrice\n"))
    b = int(input("Entrez la deuxieme valeur de la matrice\n"))
    c = int(input("Entrez la troisieme valeur de la matrice\n"))
    d = int(input("Entrez la quatrieme valeur de la matrice\n"))
    return np.array([[a,b],[c,d]])

def chiffrement(lettreNombre, matrice):
    motCript = []
    for i in range(0, len(lettreNombre)-1, 2):
        motCript.append((lettreNombre[i] * matrice[0,0] + lettreNombre[i+1] * matrice[0,1])%26)
        motCript.append((lettreNombre[i] * matrice[1,0] + lettreNombre[i+1] * matrice[1,1])%26)
    return motCript

def dechiffrement(lettreNombre, matrice):
    
    return 1



def nombreEnMot(motCodeNombre):
    motCode = []
    for i in range(0, len(motCodeNombre)):
        motCode.append(chr(motCodeNombre[i] + 65))
    return motCode
  
    
mot = str.format(input("Entrez votre mot à chiffrer ou déchiffrer\n"))
lettreNombre = motEnNombre(mot)  
matrice = definitionMatrice()
det = int((np.linalg.det(matrice))%26)
if det == 0:
    print("Matrice non inversible")
else :  
    choix = int(input("Voulez vous chiffrer ou dechiffrer (Entrez 1 ou 2)\n"))
    while choix != 1 and choix != 2 : 
        choix = int(input("Voulez vous chiffrer ou dechiffrer (Entrez 1 pour chiffrer et 2 pour déchiffrer)\n"))
    if choix == 1 :
        motCodeNombre = chiffrement(lettreNombre, matrice)
        print(nombreEnMot(motCodeNombre))
    else :
         dechiffrement(lettreNombre, matrice)
    
    