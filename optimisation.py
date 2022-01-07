# imports généraux
import csv
import itertools
import time
import pprint
# imports locaux
# constantes
# main

def recuperer_liste_actions(nom_du_csv:str) -> list :
    """
    récupère la data du csv. Dans l'ordre :
    nom, coût, % de gain sur 2 ans attention : tout est en str
    """
    with open (nom_du_csv,'r') as data:
        reader = csv.reader(data)
        list_of_actions = list(reader)[1:]
    return list_of_actions

def clean_data(list_of_actions):
    clean_data = []
    for action in list_of_actions:
        if not float(action[1]) <= 0.0:
            action = [action[0], float(action[1]), float(action[2].replace("%",""))]
            clean_data.append(action)
    return clean_data

def create_dictionaries(clean_data)->list[dict]:
        """
        Renvoie la liste des actions, chacune sous forme d'un dictionnaire
        dont les clés sont : nom, coût, pourcentage de bénéfice après 2 ans,
        rendement sur 2 ans 
        """
        actions_as_dict= []
        for action in clean_data:
            cost = action[1]
            pourcentage_of_gain_over_2_years = action[2]
            dividend_over_2_years = cost*pourcentage_of_gain_over_2_years/100

            dico_action = {
                "nom":action[0],
                "coût": cost,
                "pourcentage de bénéfice après 2 ans":pourcentage_of_gain_over_2_years,
                "rendement sur 2 ans":dividend_over_2_years
            }

            actions_as_dict.append(dico_action)
        return actions_as_dict

def brute_force(actions_as_dict:list):
    meilleur_panier = None
    meilleur_rendement = 0

    paniers_acceptables = []
    for i in range(1, len(actions_as_dict) + 1):
        paniers = itertools.combinations(actions_as_dict, i)
        for panier in paniers:
            cout_panier = sum(action["coût"] for action in panier)
            # memory concious vs sum([action["cout"] for action in panier]) time concious, pourquoi?
            if cout_panier < 500:
                paniers_acceptables.append(panier)

    for panier in paniers_acceptables:
        rendement_panier = sum(action["rendement sur 2 ans"] for action in panier)
        if rendement_panier > meilleur_rendement:
            meilleur_panier = panier
            meilleur_rendement = rendement_panier

if __name__ == "__main__":

    start_time = time.time()
    # liste de dictionnaires (un par action):
    # Nom de l'action, coût, % sur 2 ans, rendement sur 2 ans, rendement global absolu
    # (rendement relatif absolu = dividende)
    # pour chaque combinations pour paniers =< 500 faire :
    #     récupérer le rendement total
    #     comparer les paniers =< 500 en fonction du rendement total
    # if rendement > meilleur_rendement, mettre à jour meilleur_rendement

    # opti : panda? memoïsation, backpack, prog dynamique

    dataset1 = "dataset1_Python+P7.csv"
    dataset2 = "dataset2_Python+P7.csv"
    list_of_actions =  recuperer_liste_actions(dataset1)
    clean_list = clean_data(list_of_actions)
    print(clean_list)
    list_of_dicos = create_dictionaries(clean_list)

    """
    meilleur_panier = brute_force(list_of_dicos)
    for action in meilleur_panier:
        print(action["nom"])
    print(sum(action["coût"] for action in meilleur_panier))
    print(sum(action["rendement sur 2 ans"] for action in meilleur_panier))
    """

    print("---%s seconds ---" % (time.time() - start_time))