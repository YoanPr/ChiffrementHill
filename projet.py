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

def criptage(lettreNombre, matrice):
    motCript = []
    for i in range(0, len(lettreNombre)-1, 2):
        motCript.append((lettreNombre[i] * matrice[0,0] + lettreNombre[i+1] * matrice[0,1])%26)
        motCript.append((lettreNombre[i] * matrice[1,0] + lettreNombre[i+1] * matrice[1,1])%26)
    return motCript

def nombreEnMot(motCodeNombre):
    motCode = []
    for i in range(0, len(motCodeNombre)):
        motCode.append(chr(motCodeNombre[i] + 65))
    return motCode
    
    
mot = str.format(input("Entrez votre mot\n"))
lettreNombre = motEnNombre(mot)  
matrice = definitionMatrice()
print(matrice)
det = int((np.linalg.det(matrice))%26)
if det == 0:
    print("Matrice non inversible")
else: 
    motCodeNombre = criptage(lettreNombre, matrice)
    print(nombreEnMot(motCodeNombre))
    
    