import math
from PIL import Image
import random
import numpy as np
image=Image.open('image1_bruitee_snr_13.0913.png')
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
    n=np.array(np.random.normal(0,0.2,hauteur*longueur))
    valeurPixel=np.asarray(image)
    for i in range(longueur-1):
        for j in range (hauteur-1):
            
            v=(n[c]+1)*valeurPixel[i][j]
            
            if v>255 :
                valeurPixel[i][j]=255
            elif v<0 :
                valeurPixel[i][j]=0
            else :
                valeurPixel[i][j]=v
            c+=1
    return valeurPixel

def Bruitage_poivre_et_sel(longueur,hauteur):
     valeurPixel=np.asarray(image)
     for i in range (longueur):
        for j in range(hauteur):  
            if random.randint(0,100) >=50 :
                if random.randint(0,1)==1:
                    valeurPixel[i][j]=255
                else :
                    valeurPixel[i][j]=0
     return valeurPixel

def Debruitage_Median_poivre_et_sel(longueur,hauteur):
    valeurPixel=np.asarray(image)
    for i in range(hauteur):
        for j in range(longueur):
            if valeurPixel[i][j]== 0 or valeurPixel[i][j]==255:
                if i==(hauteur-1)and j!=(longueur-1): # ligne de droite
                    valMoy=[valeurPixel[i][j-1],valeurPixel[i][j+1],valeurPixel[i-1][j],valeurPixel[i-1][j-1],valeurPixel[i-1][j+1]]
                    c=np.median(sorted(valMoy))
                    valeurPixel[i][j]=c
                if i==(hauteur-1) and j==(longueur-1): # coin en bas à droite
                    valMoy=[valeurPixel[i-1][j],valeurPixel[i][j-1],valeurPixel[i-1][j-1]]
                    c=np.median(sorted(valMoy))
                    valeurPixel[i][j]=c
                if j==(longueur-1)and i!=(hauteur-1): # colonne de droite
                    valMoy=[valeurPixel[i-1][j],valeurPixel[i+1][j],valeurPixel[i][j-1],valeurPixel[i-1][j-1],valeurPixel[i+1][j-1]]
                    c=np.median(sorted(valMoy))
                    valeurPixel[i][j]=c
                if i!=(hauteur-1) and j!=(longueur-1): #traitement du reste des pixels
                    valMoy=[valeurPixel[i-1][j+1],valeurPixel[i+1][j-1],valeurPixel[i+1][j],valeurPixel[i][j+1],valeurPixel[i][j-1],valeurPixel[i-1][j],valeurPixel[i-1][j-1],valeurPixel[i+1][j+1]]
                    c=np.median(sorted(valMoy))
                    valeurPixel[i][j]=c
    return valeurPixel

def Debruitage_Convolution(longueur,hauteur):
    valeurPixel=np.asarray(image)

    kernel=[[1/16,2/16,1/16],[2/16,4/16,2/16],[1/16,2/16,1/16]]  
    
    sigma=0.8
    #kernel = np.zeros((3,3),float)+(1/(2*(np.pi)*sigma**2))*np.exp(-((3-1)**2)/2*(sigma**2))
    #print(kernel)
    for i in range(hauteur):
            for j in range(longueur):
                if valeurPixel[i][j]== 0 or valeurPixel[i][j]==255:
                    if i==(hauteur-2)and j!=(longueur-2): # ligne de droite
                        c=valeurPixel[i][j]=kernel[0][0]*valeurPixel[i+1][j+1] +kernel[1][0]*valeurPixel[i][j+1] +kernel[0][1]*valeurPixel[i+1][j] +kernel[1][1]*valeurPixel[i][j] +kernel[0][2]*valeurPixel[i+1][j-1] +kernel[1][2]*valeurPixel[i][j-1]
                    if i==(hauteur-1) and j==(longueur-1): # coint en bas à droite
                        c=valeurPixel[i][j]=kernel[0][0]*valeurPixel[i+1][j+1] +kernel[1][0]*valeurPixel[i][j+1] +kernel[0][1]*valeurPixel[i+1][j] +kernel[1][1]*valeurPixel[i][j] 
                        valeurPixel[i][j]=c
                    if j==(longueur-2)and i!=(hauteur-2): # colonne de droite
                        c=valeurPixel[i][j]=kernel[0][0]*valeurPixel[i+1][j+1] +kernel[1][0]*valeurPixel[i][j+1] +kernel[2][0]*valeurPixel[i-1][j+1] +kernel[0][1]*valeurPixel[i+1][j] +kernel[1][1]*valeurPixel[i][j] +kernel[2][1]*valeurPixel[i-1][j] 
                    if i!=(hauteur-1) and j!=(longueur-1): #traitement du reste des pixels
                        c=valeurPixel[i][j]=kernel[0][0]*valeurPixel[i+1][j+1] +kernel[1][0]*valeurPixel[i][j+1] +kernel[2][0]*valeurPixel[i-1][j+1] +kernel[0][1]*valeurPixel[i+1][j] +kernel[1][1]*valeurPixel[i][j] +kernel[2][1]*valeurPixel[i-1][j] +kernel[0][2]*valeurPixel[i+1][j-1] +kernel[1][2]*valeurPixel[i][j-1] +kernel[2][2]*valeurPixel[i-1][j-1]
                        valeurPixel[i][j]=c
    return valeurPixel

def debruitage_Median(longueur,hauteur):
    valeurPixel=np.asarray(image)
    for i in range(hauteur):
        for j in range(longueur):
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

def calcul_Snr(valeurImageBruitée,l,h):
    pSignal,pBruit=0,0
    imagesnr=Image.open('img2.png')
    valeurImageSnr=np.asarray(imagesnr)
    for i in range(h):
        for j in range (l):
            pSignal+=float(valeurImageBruitée[i][j]**2)
            pBruittmp=float(valeurImageBruitée[i][j])-float(valeurImageSnr[i][j])
            pBruit+=float(pBruittmp**2)

    print("pSignal = ",pSignal)
    print("pBruit = ",pBruit)
    print("pSignal-pBruit = ",pSignal - pBruit)
    snr = float(10*np.log10(pSignal/abs(pBruit)))
    print("Le SNR est :",snr)
    imagesnr.close()
l,h = image.size

while True :
    c=input(" 1 = Bruitage poivre et sel \n 2 = Bruitage additif \n 3 = Bruitage multiplicatif \n 4 = Debruitage median \n 5 Debruitage convolution \n 6 Quitter \n 7 Calcul du snr \n ")
    if (c=='1') :
        valeurImageBruitée = Bruitage_poivre_et_sel(l,h)
        image= Image.fromarray(valeurImageBruitée)
        image.show()
        c=input("Voulez vous calculer le snr de cette image : 1 oui 2 non\n")
        if c=="1" :
            calcul_Snr(valeurImageBruitée,l,h)
        else :
            c="null"

    elif (c=='2'):
        valeurImageBruitée = BruitageGaussAdditf(l,h)
        image= Image.fromarray(valeurImageBruitée)
        image.show()
        c=input("Voulez vous calculer le snr de cette image : 1 oui 2 non\n")
        if c=="1" :
            calcul_Snr(valeurImageBruitée,l,h)
        else :
            c="null"

    elif(c=='3'):
        valeurImageBruitée = BruitageGaussMulti(l,h)
        image= Image.fromarray(valeurImageBruitée)
        image.show()
        c=input("Voulez vous calculer le snr de cette image : 1 oui 2 non\n")
        if c=="1" :
            calcul_Snr(valeurImageBruitée,l,h)
        else :
            c="null"

    elif (c=='4'):
        image=Image.fromarray( debruitage_Median(l,h))
        valeurImageBruitée=debruitage_Median(l,h)
        image.show()
        c=input("Voulez vous calculer le snr de cette image : 1 oui 2 non\n")
        if c=="1" :
            calcul_Snr(valeurImageBruitée,l,h)
        else :
            c="null"

    elif(c=="5"):
        valeurImageBruitée=Debruitage_Convolution(l,h)
        image= Image.fromarray(valeurImageBruitée)
        image.show()
        c=input("Voulez vous calculer le snr de cette image : 1 oui 2 non\n")
        if c=="1" :
            calcul_Snr(valeurImageBruitée,l,h)
        else :
            c="null"

    elif(c=='6'):
        break

    elif (c=="7"):
        image.close()
        image2=Image.open('image2_bruitee_sigma65.tiff')
        valeurImageBruitée=np.asarray(image2)
        calcul_Snr(valeurImageBruitée,l,h)