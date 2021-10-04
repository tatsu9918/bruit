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
# def Bruitage_couleur_poivre_et_sel(longueur,hauteur):
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
# def Debruitage_Median_Couleur(longueur,hauteur):
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

def Calcul_Snr(valeurImage,valeurImageBruitée):
    v1=np.sum(valeurImage)
    v2 =np.sum(valeurImage)-np.sum(valeurImageBruitée)
    v2=abs(v2)
    print(v2)
    SNR=10*math.log10(v1**2/v2**2)
    print("Le SNR est :",SNR)  

l,h = image.size
image= Image.fromarray(Debruitage_Median_poivre_et_sel(l,h))
image.show()
valeurImageBruitée=np.asarray(image)
print(Calcul_Snr(valeurImage,valeurImageBruitée))
# image.save('buitcouleur.png')
# image= Image.fromarray(bruitageGaussAdditf(l,h))
# image.show()
# image= Image.fromarray(bruitageGaussMulti(l,h))
# image.show()