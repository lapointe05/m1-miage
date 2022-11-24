#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/lapointe05/m1-miage/blob/main/M1_MIAGE_TD_03.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# <img src="https://upload.wikimedia.org/wikipedia/fr/0/0b/Polytech_Lyon_logo.png" alt="drawing" height="200"/>
# 
# # Algorithmique Avancée & Programmation en Python
# ---
# 
# 

# # TD 03
# 
# Intro aux traitement de données
# 
# ```python
# print("Hello, friend! It's been a while...")
# ```
#  
# Elements à consulter:
# 
# 
# Doc                                   |             Link
# --------------------------------------|------------------------------------
# Python en 30 jours | [>link<](https://moncoachdata.com/courses/apprendre-python-en-30-jours/)
# Get started with pandas | [>link<](https://colab.research.google.com/notebooks/snippets/pandas.ipynb)

# ## Intro
# 
# Le premier bloc devrait toujours contenir les installs/imports dont on aura besoin pour le reste

# In[ ]:


# Installs
get_ipython().system('pip install emoji --quiet')


# In[ ]:


# Imports
import os
import json
from random import randint
# import pandas as pd
# import numpy as np
from getpass import getpass
import emoji

print(emoji.emojize('Python is awesome :thumbs_up:'))


# ##EX01
# ### Révision boucles / compréhension de listes
# 
# Avec l'usage de la boucle `for`, répondez aux questions ci-dessous
# 
# 
# > PS: Code pris et modifié à partir d'exo sur github

# In[10]:


##############################################################
nombres = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
nombres_pairs = []
i = 0
for i in nombres: 
    if i % 2 == 0 :
        nombres_pairs.append(i)
print(nombres_pairs)

##############################################################

nombres = range(-10, 10)
nombres_positifs = []
i = -10
for i in nombres : 
    if i >= 0 :
        nombres_positifs.append(i) 
print(nombres_positifs)

##############################################################

nombres = range(5)
nombres_x2 = []
i = 0
for i in nombres : 
    nombres_x2.append(i*2)
print(nombres_x2)


# ### PART 2
# Changez le code ci-dessus, et remplacez les blocs `for` par des [compréhensions de listes](https://duckduckgo.com/?q=list+comprehension+python)

# In[17]:


nombres_pairs = [i for i in [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38] if i%2==0]
print(nombres_pairs)

nombres_positifs =[i for i in range (-10, 10) if i>=0]
print(nombres_positifs)

nombres_x2 = [ i*2 for i in range(5) ]
print(nombres_x2)


# ##EX02
# ### Les sets
# 
#   1. Créez un `set` vide et attribuez-le à une variable.
#   2. Ajoutez trois éléments à votre ensemble vide en utilisant soit plusieurs appels `add`, soit un seul appel de `update`.
# 
#   3. Créez un deuxième `set` qui comprend au moins un élément commun avec le premier ensemble.
# 
#   4. Trouvez l’union, la différence et l’intersection des deux `set`. >>
# Imprimez les résultats de chaque opération.
# 
#   5. Créez une `set` de nombres en utilisant `range()`, puis demandez à l’utilisateur d’entrer un nombre. Indiquez à l’utilisateur si son nombre se situe ou non dans la plage de valeurs que vous avez spécifiée.
# 
# >Bonus: 
# >>Indiquer à l’utilisateur si son nombre était trop élevé ou trop bas.

# In[28]:


a=set()
a.update('1','2','3')
print(a)
b=set()
b.update('1','2','5')
print(b)
print("l'union des deux ensembles est : ",a.union(b))
print("la différence des deux ensembles est : ",a.difference(b))
print("l'intersection des deux ensembles est : ",a.intersection(b))


# ## EX03
# ### Revision listes
# 1. Créez une liste de séries (`binge_watch_list`) contenant un seul tuple. Le tuple doit contenir le titre de la série, la plateforme de streaming (légal), le nombre d'épisodes de la série, l'année de sortie et une note /10.
# 
# 2. Créez une fonction (`input_series`) qui receuil des informations sur d'autres séries à l'aide de la fonction native `input`. Et nous retourne un tuple. \n
# Tout les champs sont obligatoires.
# 
# 4. Utilisez `f-string` pour imprimer le nom et l’année de sortie de la série qu'on vient d'input.
# 
# 3. Alimenter la liste (`binge_watch_list`) avec le retour de la fonction (`input_series`) \n
# Assurez vous que l'ordre des champs soit le même que dans (`binge_watch_list`).
# 
# 
# 5. Afficher le nom et l’année de sortie de toutes les séries dans `binge_watch_list`.
# 
# > Bonus:
# 
# 6. Supprimez la série la moins bien noté de `binge_watch_list`. Utilisez la méthode de votre choix.

# In[1]:


binge_watch_list = (('friends','netflix','100','1990','9/10'),('snk','voiranime','90','2010','10/10'))
print(binge_watch_list)

def input_series ():

    infos = ()
    binge_watch_list = (('friends','netflix','100','1990','9/10'),('snk','voiranime','90','2010','10/10'))
    print("Entrez les informations d'une série : ")
    titre = input("Entrez le titre d'une série : ")
    plateforme = input("Entrez la plateforme de streaming de la série : ")
    nb_episodes = input("Entrez le nombre d'épisodes la série : ")
    while not nb_episodes.isdigit() :
        nb_episodes = input("Entrez le nombre d'épisodes la série : ")
    annee_sortie = input("Entrez l'année de sortie de la série : ")
    while not annee_sortie.isdigit() :
        annee_sortie = input("Entrez l'année de sortie de la série : ")
    note = input("Attribuez une note à la série : ")
    while not note.isdigit() :
        note = input("Attribuez une note à la série sur 10 : ")
    
    if int(note) > 10 : 
        print("La note ne doit pas dépasser 10")  
        note = input("Attribuez une note à la série sur 10 : ")
    elif int(note) < 0 : 
        print("La note ne doit pas être en dessous de 0")
        note = input("Attribuez une note à la série sur 10 : ")
  
    infos=(titre,plateforme,nb_episodes,annee_sortie,note)
    print("Merci pour ces informations ! ")
    print(f"le nom du film est : {titre} et il est sorti en {annee_sortie}")
    print(f"{titre}\n{plateforme}\n{nb_episodes}\n{annee_sortie}\n{note}")
    return infos

def main() :
    input_series()
    binge_watch_list = input_series()
    print(binge_watch_list)

main()


# Transformer le code ci-dessous de liste a dictionnaire

# In[ ]:





# ## EX04
# ### Révision strings / fonctions
# Implementer deux fonctions `input_password()` & `password_check(x)` qui :
# 
# 1. `input_password()` fait:
#     * Demande à l'utilisateur un mot de passe d'au moins 8 caractères, 12 c'est mieux.
#     * retourne ce dernier
# 
# 2. `password_check(x)` verifie:
# 
#     * print `mot de passe trop court!` **avec une majuscule sur la première lettre** si la longueur du mot de passe entré est `plus petite que 8`.
# 
#     * Verifier que le mot de passe soit une combinaison de `lettres majuscules, de lettres minuscules, de chiffres et de symboles.` 
#     > Si le mot de passe manque de répondre à une condition, l'afficher à l'utilisateur
# 
#     *  Afficher la phrase `"Mot de passe valide."` si le mot de passe répond à **toutes les conditions**.
# 
# > bonus 
# 
# * Verifier qu'un même mot de passe ne peut pas etre saisie deux fois, ex. utiliser une variable `previous_password`

# In[3]:


import string
import getpass

def input_password() : 
    mdp = getpass.getpass("Entrez un mot de passe d'au moins 8 caractères, 12 c'est mieux : ")
    return mdp

def password_check() :
    mdp = input_password()
    symboles = ["@","#","?","/",",",";","$","*","€","."]
    while len(mdp) < 8 :
        print("Mot de passe trop court!")
        mdp = input_password()
    ("")
    lis=[0,0,0,0]
    for i in mdp:
        if i.isupper():
            lis[0] = 1
        elif i.islower():
            lis[1] = 1
        elif i in symboles:
            lis[2] = 1
        elif i.isdigit():
            lis[3] = 1
    print(lis)
    if 0 not in lis and len(s) > 8 :
        print('Mot de passe valide')
        mdp = input_password()
    else :
        print('mot de passe invalide')
        mdp = input_password()

        

password_check()


# ## EX05
# ### To do list
# 1. Créez une fonction (`to_do_list()`) qui demande à l'utilisateur de choisir parmis 5 options
#     1. Ajouter un élément à la to do list
#     2. Retirer un élément de la to do list
#     3. Afficher les éléments de la to do list
#     4. Vider la to do list
#     5. Quitter le programme
# 2. L'utilisateur doit entrer un nombre (entre 1 et 5) pour choisir l'option souhaité 
#     * Vous devez verifier que l'input est un nombre
#     * Vous devez verifier que l'input est entre 1 et 5
# 
# 3. Implementez chancune des options de la fonction 😃
# 
# 3. Exemple de run du code ci dessous 👇

# In[ ]:


def option():
    print("Choisissez parmis ce 5 options s'il-vous-plaît :\n1 . Ajout élément à la to do list\n2 . Retirer élément à la to do list\n3 . Afficher les éléments à la to do list\n4 . Vider à la to do list\n5 . Quitter à la to do list")
    a = input("veuillez entrez le numéro correspondant à l'option choisi :")
    return a

def to_do_list() : 
    l = []
    a = option()
    while not a.isdigit() :
        print("Entrez un nombre s'il-vous-plaît !")
        a = option()
    ("")
    while int(a)>5 or int(a)<1:
        print("Entrez un nombre compris entre 1 et 5 s'il-vous-plaît !")
        a = option()
    ("")
    while int(a) == 1 :
        b = input("veuillez entrez l'élément à ajouter :")
        l.append(b)
        a = option()
        print(l)
        a = input("veuillez entrez le numéro correspondant à l'option choisi :")
    ("")
    while int(a) == 2 :
        b = input("veuillez entrez l'élément à retirer :")
        l.remove(b)
        a = option()
        print(l)
    ("")
    while int(a) == 3 :
        print(l)
        a = option()
    ("")
    while int(a)== 4 :
        l.clear()
        print(l)
        a = option()
    ("")
    while int(a) == 5 :
        print("Vous avez quitter la fonction !")
        print(exit())
    ("")

to_do_list()


# In[55]:


##


# # Bonus (Mandatory)
# 
# 
# 

# ## Github
# Pour soumettre votre travail: 
# 
# 1.   Commit changes to a branch and push to [github](https://google.com)
# 2.   Create pull request / merge request
# 
