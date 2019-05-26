# -*- coding: utf-8 -*-

from numba import jit
import numpy as np
import matplotlib.pyplot as plt

def calcul_nb_voisins(Z):
    """
    Cette fonction prend en argument une liste (de liste) qui 
    représente la "carte" du jeu de la vie.
    Elle renvoie le nombre de voisins vivants de chaque cellules
    """
    forme = len(Z), len(Z[0]) 
    N = [[0, ] * (forme[0]) for i in range(forme[1])] 
    for x in range(1, forme[0] - 1): 
        for y in range(1, forme[1] - 1): 
            N[x][y] = Z[x-1][y-1]+Z[x][y-1]+Z[x+1][y-1] \
            + Z[x-1][y] + 0 +Z[x+1][y] \
            + Z[x-1][y+1]+Z[x][y+1]+Z[x+1][y+1]
    return N


def iteration_jeu(Z):
    """
    Cette fonction prend en argument une liste (de liste) qui 
    représente la "carte" du jeu de la vie.
    Elle retourne la "carte" du jeu de la vie une génération 
    plus tard, après les naissances et décès des cellules.
    """
    forme = len(Z), len(Z[0])
    N = calcul_nb_voisins(Z)
    for x in range(1,forme[0]-1): 
        for y in range(1,forme[1]-1): 
            if Z[x][y] == 1 and (N[x][y] < 2 or N[x][y] > 3):
                Z[x][y] = 0 
            elif Z[x][y] == 0 and N[x][y] == 3: 
                Z[x][y] = 1
    return Z

def plotJeuDeLaVie(nbIterations, Z, iter_func):
    """
    nbIterations = le nombre d'iterations voulu
    Z = une liste (de liste)
    iter_func = une fonction qui affiche l'etat des cellules apres une iteration
    
    Cette fonction affiche l'évolution des matrices du Jeu de la vie
    """
    Zcopy = Z.copy()
    plt.figure(figsize=(15,7))
    plt.subplot(2,5,1)
    plt.title("Iteration 0")
    plt.imshow(Zcopy)
    for i in range(2,nbIterations+1):
        plt.subplot(2,5,i)
        Zcopy = iter_func(Zcopy)
        plt.title("Iteration "+str(i-1))
        plt.imshow(Zcopy)
        
    return plt.imshow(Zcopy)

@jit(nopython=True)
def calcul_nb_voisins_jit(Z):
    """
    Cette fonction prend en argument une liste (de liste)/ numpy array
    qui représente la "carte" du jeu de la vie.
    Elle renvoie le nombre de voisins vivants de chaque cellules
    """
    forme = len(Z), len(Z[0]) 
    N = np.zeros((forme[0],forme[1]))
    for x in range(1, forme[0] - 1): 
        for y in range(1, forme[1] - 1): 
            N[x,y] = Z[x-1,y-1]+Z[x,y-1]+Z[x+1,y-1] \
            + Z[x-1,y] + 0 +Z[x+1,y] \
            + Z[x-1,y+1]+Z[x,y+1]+Z[x+1,y+1]
    return N

@jit(nopython=True)
def iteration_jeu_jit(Z):
    """
    Cette fonction prend en argument une liste (de liste) / numpy array 
    qui représente la "carte" du jeu de la vie.
    Elle retourne la "carte" du jeu de la vie une génération 
    plus tard, après les naissances et décès des cellules.
    """
    forme = len(Z), len(Z[0])
    N = calcul_nb_voisins_jit(Z)
    for x in range(1,forme[0]-1): 
        for y in range(1,forme[1]-1): 
            if Z[x,y] == 1 and (N[x,y] < 2 or N[x,y] > 3):
                Z[x,y] = 0 
            elif Z[x,y] == 0 and N[x,y] == 3: 
                Z[x,y] = 1
    return Z

def plotJeuDeLaVie_manySP(nbIterations, Z, iter_func):
    """
    nbIterations = le nombre d'iterations voulu
    Z = une liste (de liste) / numpy array.
    iter_func = une fonction qui affiche l'etat des cellules apres une iteration
    
    Cette fonction affiche l'évolution des matrices du Jeu de la vie
    """
    plt.figure(figsize=(15,15))
    Zcopy = Z.copy()
    for i in range(6):
        for j in range(5):
            if ((i*5+j)>=nbIterations):
                break
            plt.subplot2grid((6,5), (i,j)) # Have to use subplot2grid instead of subplot for > 10 subplots.
            plt.title("Iteration "+str(i*5+j))
            if (i==0 and j==0):
                plt.imshow(Zcopy)
            else:
                Zcopy = iter_func(Zcopy)
                plt.imshow(Zcopy)
    
    return plt.tight_layout()
    
    
def fig_digit(x, w, alpha):
    """
    x = un individu du jeu de données MNIST
    w = le vecteur appris par la fonction LogisticRegression sur MNIST
    alpha = un reel 
    
    Cette fonction renvoie l'image de xmod qui est défini à la question 4 de l'exercice 2 du TP noté 
    """
    w = np.ravel(w)
    wTx = w.dot(x)
    norm_w = np.linalg.norm(w)
    
    xmod = x - alpha*(wTx/norm_w**2)*w
    
    return plt.imshow(xmod.reshape(28,28))