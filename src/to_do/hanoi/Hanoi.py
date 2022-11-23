#!/usr/bin/env python3.9.15
# -*- coding: utf-8 -*-

def affichageHanoi(tour1, tour2, tour3, nbCoups):
    # Display the actual state of the game
    print(f"""Situation actuelle :
    Tour 1 : {tour1}
    Tour 2 : {tour2}
    Tour 3 : {tour3}
    
    Nombre de coups actuel : {nbCoups}""")

def hanoi(nbanneau):
    """Main part of the game.
The smaller disk will do a loop. Each cycle will move the smaller disk from tower 1 to 2, then 2 to 3 and last 3 to 1
The other disk will move on the only tower left, depending on the disks already on it"""

    #Initialise the towers
    tour1 = []
    tour2 = []
    tour3 = []
    if (nbanneau % 2) == 0:
        tourSuivante = "tour2"
    elif (nbanneau % 2) == 1:
        tourSuivante = "tour3"

    nbCoups = 0
    
    #Fill the first tower
    for i in range(nbanneau):
        tour1.append(i+1)

    print(f"""Situation de depart:
    Tour 1 : {tour1}
    Tour 2 : {tour2}
    Tour 3 : {tour3}""")

    #Continue while the disks are not all in the third towers
    while len(tour3) != nbanneau:

        if nbanneau == 1 :
            anneau = tour1.pop()
            tour3.append(anneau)
            nbCoups+=1

        elif (nbanneau % 2) == 0:
            if tourSuivante == "tour1" :
                anneau1 = tour3.pop(0)
                tour1.insert(0, anneau1)
                nbCoups+=1

                # Test if the second tower is filled : False if empty, True if filled
                try:
                    tour2[0]

                except:
                    ok2 = False
                
                else:
                    ok2 = True

                # Test if the third tower is filled : False if empty, True if filled
                try:
                    tour3[0]

                except: 
                    ok3 = False

                else:
                    ok3 = True

                if ok2:
                    if ok3:
                        if tour2[0] > tour3[0]:
                            anneau2 = tour3.pop()
                            tour2.insert(0, anneau2)
                            nbCoups+=1
                        elif tour2[0] < tour3[0]:
                            anneau2 = tour2.pop(0)
                            tour3.insert(0, anneau2)
                            nbCoups+=1
                    else:
                        anneau2 = tour2.pop(0)
                        tour3.append(anneau2)
                        nbCoups+=1             
                else:
                    if ok3:
                        anneau2 = tour3.pop(0)
                        tour2.append(anneau2)
                        nbCoups+=1
                    else:
                        print("Tour 1 complete")

                tourSuivante = "tour2"

                affichageHanoi(tour1, tour2, tour3, nbCoups)

            elif tourSuivante == "tour2" :
                anneau1 = tour1.pop(0)
                tour2.insert(0, anneau1)
                nbCoups+=1

                # Test if the first tower is filled : False if empty, True if filled
                try:
                    tour1[0]

                except:
                    ok1 = False
                
                else:
                    ok1 = True

                # Test if the third tower is filled : False if empty, True if filled
                try:

                    tour3[0]

                except: 
                    ok3 = False

                else:
                    ok3 = True

                if ok1:
                    if ok3:
                        if tour1[0] > tour3[0]:
                            anneau2 = tour3.pop(0)
                            tour1.insert(0, anneau2)
                            nbCoups+=1
                        elif tour1[0] < tour3[0]:
                            anneau2 = tour1.pop(0)
                            tour3.insert(0, anneau2)
                            nbCoups+=1
                    else:
                        anneau2 = tour1.pop(0)
                        tour3.append(anneau2)
                        nbCoups+=1               
                else:
                    if ok3:
                        anneau2 = tour3.pop(0)
                        tour2.append(anneau2)
                        nbCoups+=1
                    else:
                        print("Tour 2 complete")

                tourSuivante = "tour3"

                affichageHanoi(tour1, tour2, tour3, nbCoups)  
                
            elif tourSuivante == "tour3" :
                anneau1 = tour2.pop(0)
                tour3.insert(0, anneau1)
                nbCoups+=1

                # Test if the second tower is filled : False if empty, True if filled
                try:
                    tour2[0]

                except:
                    ok2 = False
                
                else:
                    ok2 = True

                # Test if the first tower is filled : False if empty, True if filled
                try:

                    tour1[0]

                except: 
                    ok1 = False

                else:
                    ok1 = True

                if ok2:
                    if ok1:
                        if tour2[0] > tour1[0]:
                            anneau2 = tour1.pop(0)
                            tour2.insert(0, anneau2)
                            nbCoups+=1
                        elif tour2[0] < tour1[0]:
                            anneau2 = tour2.pop(0)
                            tour1.insert(0, anneau2)
                            nbCoups+=1
                    else:
                        anneau2 = tour2.pop(0)
                        tour1.append(anneau2)
                        nbCoups+=1   
                else:
                    if ok1:
                        anneau2 = tour1.pop(0)
                        tour2.append(anneau2)
                        nbCoups+=1
                    else:
                        print("Tour 3 complete")

                tourSuivante = "tour1"

                affichageHanoi(tour1, tour2, tour3, nbCoups)

        elif (nbanneau % 2) == 1:
            if tourSuivante == "tour1" :
                anneau1 = tour2.pop(0)
                tour1.insert(0, anneau1)
                nbCoups+=1

                # Test if the second tower is filled : False if empty, True if filled
                try:
                    tour2[0]

                except:
                    ok2 = False
                
                else:
                    ok2 = True

                # Test if the third tower is filled : False if empty, True if filled
                try:
                    tour3[0]

                except: 
                    ok3 = False

                else:
                    ok3 = True

                if ok2:
                    if ok3:
                        if tour2[0] > tour3[0]:
                            anneau2 = tour3.pop()
                            tour2.insert(0, anneau2)
                            nbCoups+=1
                        elif tour2[0] < tour3[0]:
                            anneau2 = tour2.pop(0)
                            tour3.insert(0, anneau2)
                            nbCoups+=1
                    else:
                        anneau2 = tour2.pop(0)
                        tour3.append(anneau2)
                        nbCoups+=1             
                else:
                    if ok3:
                        anneau2 = tour3.pop(0)
                        tour2.append(anneau2)
                        nbCoups+=1
                    else:
                        print("Tour 1 complete")

                tourSuivante = "tour3"

                affichageHanoi(tour1, tour2, tour3, nbCoups)

            elif tourSuivante == "tour2" :
                anneau1 = tour3.pop(0)
                tour2.insert(0, anneau1)
                nbCoups+=1

                # Test if the first tower is filled : False if empty, True if filled
                try:
                    tour1[0]

                except:
                    ok1 = False
                
                else:
                    ok1 = True

                # Test if the third tower is filled : False if empty, True if filled
                try:

                    tour3[0]

                except: 
                    ok3 = False

                else:
                    ok3 = True

                if ok1:
                    if ok3:
                        if tour1[0] > tour3[0]:
                            anneau2 = tour3.pop(0)
                            tour1.insert(0, anneau2)
                            nbCoups+=1
                        elif tour1[0] < tour3[0]:
                            anneau2 = tour1.pop(0)
                            tour3.insert(0, anneau2)
                            nbCoups+=1
                    else:
                        anneau2 = tour1.pop(0)
                        tour3.append(anneau2)
                        nbCoups+=1               
                else:
                    if ok3:
                        anneau2 = tour3.pop(0)
                        tour2.append(anneau2)
                        nbCoups+=1
                    else:
                        print("Tour 2 complete")

                tourSuivante = "tour1"

                affichageHanoi(tour1, tour2, tour3, nbCoups)  
                
            elif tourSuivante == "tour3" :
                anneau1 = tour1.pop(0)
                tour3.insert(0, anneau1)
                nbCoups+=1

                # Test if the second tower is filled : False if empty, True if filled
                try:
                    tour2[0]

                except:
                    ok2 = False
                
                else:
                    ok2 = True

                # Test if the first tower is filled : False if empty, True if filled
                try:

                    tour1[0]

                except: 
                    ok1 = False

                else:
                    ok1 = True

                if ok2:
                    if ok1:
                        if tour2[0] > tour1[0]:
                            anneau2 = tour1.pop(0)
                            tour2.insert(0, anneau2)
                            nbCoups+=1
                        elif tour2[0] < tour1[0]:
                            anneau2 = tour2.pop(0)
                            tour1.insert(0, anneau2)
                            nbCoups+=1
                    else:
                        anneau2 = tour2.pop(0)
                        tour1.append(anneau2)
                        nbCoups+=1   
                else:
                    if ok1:
                        anneau2 = tour1.pop(0)
                        tour2.append(anneau2)
                        nbCoups+=1
                    else:
                        print("Tour 3 complete")

                tourSuivante = "tour2"

                affichageHanoi(tour1, tour2, tour3, nbCoups)

def main() :
    nbanneau = 7
    hanoi(nbanneau)

main()