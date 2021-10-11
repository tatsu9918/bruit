import math
from PIL import Image
import random
import numpy as np
image=Image.open('image1_bruitee_snr_9.2885.png')

image=image.convert('L') 
valeurImage=np.asarray(image)

def BruitageGaussAdditf(longueur,hauteur):
    c=0
    n=np.array(np.random.normal(0,20,hauteur*longueur))
    valeurPixel=np.asarray(image)
    for i in range(longueur-1):
        for j in range (hauteur-1):
            
            v=n[c]+valeurPixel[i][j]
            if v>255 :
                valeurPixel[i][j]=255
            elif v<0 :
                valeurPixel[i][j]=0
            else :
                valeurPixel[i][j]=v
            c+=1
    return valeurPixel

def BruitageGaussMulti(longueur,hauteur):
    c=0
    n=np.array(np.random.normal(0,1,hauteur*longueur))
    valeurPixel=np.asarray(image)
    for i in range(longueur-1):
        for j in range (hauteur-1):
            
            v=(n[c]+1)*valeurPixel[i][j]
            print(v)
            
            if v>255 :
                valeurPixel[i][j]=255
            elif v<0 :
                valeurPixel[i][j]=0
            else :
                valeurPixel[i][j]=v
            c+=1
    return valeurPixel

def Bruitage_couleur_poivre_et_sel(longueur,hauteur):
    for i in range (longueur):
        for j in range(hauteur): 
            if random.randint(0,5) ==5 :
                if random.randint(0,1)==1:
                    image.putpixel((i,j),(255,255,255))
                else :
                    image.putpixel((i,j),(0,0,0))

def Bruitage_poivre_et_sel(longueur,hauteur):
     for i in range (longueur):
        for j in range(hauteur):  
            if random.randint(0,5) ==5 :
                if random.randint(0,1)==1:
                    image.putpixel((i,j),(255))
                else :
                    image.putpixel((i,j),(0))

def Debruitage_Median_poivre_et_sel(longueur,hauteur):
    valeurPixel=np.asarray(image)
    for i in range(hauteur):
        for j in range(longueur):
            if valeurPixel[i][j]== 0 or valeurPixel[i][j]==255:
                if i==(hauteur-1)and j!=(longueur-1):
                    valMoy=[valeurPixel[i][j-1],valeurPixel[i][j+1],valeurPixel[i-1][j],valeurPixel[i-1][j-1],valeurPixel[i-1][j+1]]
                    c=np.median(sorted(valMoy))
                    valeurPixel[i][j]=c
                if i==(hauteur-1) and j==(longueur-1):
                    valMoy=[valeurPixel[i-1][j],valeurPixel[i][j-1],valeurPixel[i-1][j-1]]
                    c=np.median(sorted(valMoy))
                    valeurPixel[i][j]=c
                if j==(longueur-1)and i!=(hauteur-1):
                    valMoy=[valeurPixel[i-1][j],valeurPixel[i+1][j],valeurPixel[i][j-1],valeurPixel[i-1][j-1],valeurPixel[i+1][j-1]]
                    c=np.median(sorted(valMoy))
                    valeurPixel[i][j]=c
                if i!=(hauteur-1) and j!=(longueur-1):
                    valMoy=[valeurPixel[i-1][j+1],valeurPixel[i+1][j-1],valeurPixel[i+1][j],valeurPixel[i][j+1],valeurPixel[i][j-1],valeurPixel[i-1][j],valeurPixel[i-1][j-1],valeurPixel[i+1][j+1]]
                    c=np.median(sorted(valMoy))
                    valeurPixel[i][j]=c
    return valeurPixel

def Debruitage_Median_Couleur(longueur,hauteur):
    valeurPixel=np.asarray(image)
    for i in range(hauteur):
        for j in range(longueur):
            if valeurPixel[i][j]== (0,0,0) or valeurPixel[i][j]==(255,255,255):
                if i==(hauteur-1)and j!=(longueur-1):
                    valMoy=[valeurPixel[i][j-1],valeurPixel[i][j+1],valeurPixel[i-1][j],valeurPixel[i-1][j-1],valeurPixel[i-1][j+1]]
                    c=np.median(sorted(valMoy))
                    valeurPixel[i][j]=c
                if i==(hauteur-1) and j==(longueur-1):
                    valMoy=[valeurPixel[i-1][j],valeurPixel[i][j-1],valeurPixel[i-1][j-1]]
                    c=np.median(sorted(valMoy))
                    valeurPixel[i][j]=c
                if j==(longueur-1)and i!=(hauteur-1):
                    valMoy=[valeurPixel[i-1][j],valeurPixel[i+1][j],valeurPixel[i][j-1],valeurPixel[i-1][j-1],valeurPixel[i+1][j-1]]
                    c=np.median(sorted(valMoy))
                    valeurPixel[i][j]=c
                if i!=(hauteur-1) and j!=(longueur-1):
                    valMoy=[valeurPixel[i-1][j+1],valeurPixel[i+1][j-1],valeurPixel[i+1][j],valeurPixel[i][j+1],valeurPixel[i][j-1],valeurPixel[i-1][j],valeurPixel[i-1][j-1],valeurPixel[i+1][j+1]]
                    c=np.median(sorted(valMoy))
                    valeurPixel[i][j]=c
    return valeurPixel
def Debruitage_Convolution(longueur,hauteur):
    valeurPixel=np.asarray(image)

def Calcul_Snr(valeurImage,l,h):
    c=int(input(" 1 pour un bruitage poivre et sel \n 2 pour un bruitage additif \n 3 pour un bruitage multiplicatif \n 4 pour le debug \n "))
    if (c==1):
        valeurImageBruitée=Bruitage_poivre_et_sel(l,h)
    if (c==2):
        valeurImageBruitée =BruitageGaussAdditf(l,h)
    if (c==3):
       valeurImageBruitée= BruitageGaussMulti(l,h)
    if (c==4):
        image.close()
        image2=Image.open('image1_bruitee_snr_41.8939.png')
        valeurImageBruitée=np.asarray(image2)
    v1,v2=0,0

    for i in range(h):
        for j in range (l):
            vtmp=valeurImage[i,j]**2
            v1+=np.float64(vtmp)
            vtmp=valeurImageBruitée[i,j]**2
            v2+=np.float64(vtmp)
    print("p")
    print("v1 = ",v1)
    print("v2 = ",v2)
    print("V1-v2 = ",v1 - v2)  

l,h = image.size
while True :
    c=input(" 1 = Bruitage poivre et sel \n 2 = Bruitage additif \n 3 = Bruitage multiplicatif \n 4 = Debruitage Median \n 5 pour calculer le SNR\n 6 pour quitter \n")
    if (c=='1') :
       couleurPoivreEtSel(l,h)
       image.show()
    elif (c=='2'):
        image= Image.fromarray(BruitageGaussAdditf(l,h))
        image.show()
    elif(c=='3'):
        image= Image.fromarray(BruitageGaussMulti(l,h))
        image.show()
    elif (c=='4'):
        image=Image.fromarray( DebruitageMedian(l,h))
        image.show()
    elif(c=='5'):
        Calcul_Snr(valeurImage,l,h)
    elif(c=='6'):
        break
