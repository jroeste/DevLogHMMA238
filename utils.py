# -*- coding: utf-8 -*-
"""
Created on Wed May  1 22:55:13 2019

@author: julie
"""

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
