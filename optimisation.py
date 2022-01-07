# imports généraux
import csv
import itertools
import timeit
import pprint
# imports locaux
# constantes
# main

def clean_data(cost):
    return cost <= 0.0

def recuperer_liste_actions(nom_du_csv:str) -> list :
    """
    récupère la data du csv. Dans l'ordre :
    nom, coût, % de gain sur 2 ans attention : tout est en str
    """
    with open (nom_du_csv,'r') as data:
        reader = csv.reader(data)
        actions = list(reader)[1:]
    return actions

def create_dictionaries(list_of_actions)->list[dict]:
        """
        Renvoie la liste des actions, chacune sous forme d'un dictionnaire
        dont les clés sont : nom, coût, pourcentage de bénéfice après 2 ans,
        rendement sur 2 ans 
        """
        actions_as_dict= []
        for action in list_of_actions:
            cost = float(action[1])
            pourcentage_of_gain_over_2_years = float(action[2].replace("%",""))
            dividend_over_2_years = cost*pourcentage_of_gain_over_2_years/100
            annual_yield = dividend_over_2_years/2
            global_yield = annual_yield/cost*100

            dico = {
                "nom":action[0],
                "coût": cost,
                "pourcentage de bénéfice après 2 ans":pourcentage_of_gain_over_2_years ,
                "rendement sur 2 ans":dividend_over_2_years ,
                "rendement global": global_yield
            }

            actions_as_dict.append(dico)
        return actions_as_dict

if __name__ == "__main__":
    # liste de dictionnaires (un par action):
    # Nom de l'action, coût, % sur 2 ans, rendement sur 2 ans, rendement global absolu
    # (rendement relatif absolu = dividende)
    # pour chaque combinations pour paniers =< 500 faire :
    #     récupérer le rendement total
    #     comparer les paniers =< 500 en fonction du rendement total
    # if rendement > meilleur_rendement, mettre à jour meilleur_rendement

    # opti : panda? memoïsation, backpack, prog dynamique