import math
from PIL import Image
import random
import numpy as np
image=Image.open('image2.png')
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
    kernel = np.ones((3,3),float)
    i=0
    while i+3<longueur :
        j=0
        while j+3 < hauteur:
            valeurPixel[i][j]=kernel[0][0]*valeurPixel[i+2][j+2] #A/9
            +kernel[1][0]*valeurPixel[i+1][j+2] #B/8
            +kernel[2][0]*valeurPixel[i][j+2] #C/7
            +kernel[0][1]*valeurPixel[i+2][j+1] #D/6
            +kernel[1][1]*valeurPixel[i+1][j+1] #E/5
            +kernel[2][1]*valeurPixel[i][j+1] #F/4
            +kernel[0][2]*valeurPixel[i+2][j] #G/3
            +kernel[1][2]*valeurPixel[i+1][j] #H/2
            +kernel[2][2]*valeurPixel[i][j] #I/1
            j+=1
        i+=1

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

def calcul_Snr(valeurImage,valeurImageBruitée,l,h):
    pSignal,pBruit=0,0
    for i in range(h):
        for j in range (l):
            pSignal+=float(valeurImageBruitée[i][j]**2)
            pBruittmp=float(valeurImageBruitée[i][j])-float(valeurImage[i][j])
            pBruit+=float(pBruittmp**2)

    print("pSignal = ",pSignal)
    print("pBruit = ",pBruit)
    print("pSignal-pBruit = ",pSignal - pBruit)
    snr = float(10*np.log10(pSignal/abs(pBruit)))
    print("Le SNR est :",snr)

l,h = image.size

while True :
    c=input(" 1 = Bruitage poivre et sel \n 2 = Bruitage additif \n 3 = Bruitage multiplicatif \n 4 = Debruitage Median \n 5 pour quitter \n 6 pour le test et le debug snr \n 7 pour le debruitage par concolution \n")
    if (c=='1') :
        valeurImageBruitée = Bruitage_poivre_et_sel(l,h)
        image= Image.fromarray(valeurImageBruitée)
        image.show()
        c=input("Voulez vous calculer le snr de cette image : 1 oui 2 non\n")
        if c=="1" :
            calcul_Snr(valeurImage,valeurImageBruitée,l,h)
        else :
            c="null"

    elif (c=='2'):
        
        valeurImageBruitée = BruitageGaussAdditf(l,h)
        image= Image.fromarray(valeurImageBruitée)
        image.show()
        c=input("Voulez vous calculer le snr de cette image : 1 oui 2 non\n")
        if c=="1" :
            calcul_Snr(valeurImage,valeurImageBruitée,l,h)
        else :
            c="null"

    elif(c=='3'):
        valeurImageBruitée = BruitageGaussMulti(l,h)
        image= Image.fromarray(valeurImageBruitée)
        image.show()
        c=input("Voulez vous calculer le snr de cette image : 1 oui 2 non\n")
        if c=="1" :
            calcul_Snr(valeurImage,valeurImageBruitée,l,h)
        else :
            c="null"

    elif (c=='4'):
        image=Image.fromarray( debruitage_Median(l,h))
        image.show()

    elif(c=='5'):
        break

    elif (c=="6"):
        image.close()
        image2=Image.open('image1_bruitee_snr_41.8939.png')
        valeurImageBruitée=np.asarray(image2)
        calcul_Snr(valeurImage,valeurImageBruitée,l,h)
    elif(c=="7"):
        valeurImageBruitée=Debruitage_Convolution(l,h)
        image= Image.fromarray(valeurImageBruitée)
        image.show()