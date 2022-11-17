# Import

# Globals and constants variables

# Functions


def déplacer(palet, tour_depart="A", tour_arrivée="C", tour_inter="B") -> None:
    """
    Déplace les palets d'une tour à une autre. S'il y a plus de 1 palet,
    on appelle récursivement la fonction.
    Sinon on déplace uniquement le palet.

    Args :
    - palet : le numéro de palet à déplacer.
    - tour_depart : la tour de départ.
    - tour_arrivée : la tour de destination.
    - tour_inter : la tour intermédiaire.
    """
    global tours
    if palet == 1:
        print(f"Move palet {palet} from {tour_depart} to {tour_arrivée}")
        tours[tour_arrivée].append(tours[tour_depart].pop())
        return
    déplacer(palet-1, tour_depart=tour_depart, tour_arrivée=tour_inter, tour_inter=tour_arrivée)
    print(f"Move palet {palet} from {tour_depart} to {tour_arrivée}")
    déplacer(palet-1, tour_depart=tour_inter, tour_arrivée=tour_arrivée, tour_inter=tour_arrivée)


# Code
# Initialiser variables
nombre_palets = int(input("Combien de palets ?"))

tours = {}
tours["A"] = [palet for palet in range(nombre_palets, 0, -1)]
tours["B"] = []
tours["C"] = []

déplacer(nombre_palets)
