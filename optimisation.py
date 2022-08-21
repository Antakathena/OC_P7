import csv
import time
import timeit
from typing import List

datatest = "OC_P7\AlgoInvest_actions.csv"
dataset1 = "OC_P7\dataset1_Python+P7.csv"
dataset2 = "OC_P7\dataset2_Python+P7.csv"


def recuperer_liste_actions(nom_du_csv: str) -> list:
    """
    récupère la data du csv. Dans l'ordre :
    nom, coût, % de gain sur 2 ans attention : tout est en str
    """
    with open(nom_du_csv, 'r') as data:
        reader = csv.reader(data)
        list_of_actions = list(reader)[1:]
    return list_of_actions


def clean_data(list_of_actions):
    clean_data = []
    for action in list_of_actions:
        if not float(action[1]) <= 0.0:
            action = [action[0], float(action[1]), float(action[2].replace("%", ""))]
            clean_data.append(action)
    return clean_data


def create_dictionaries(clean_data) -> list[dict]:
    """
    Renvoie la liste des actions, chacune sous forme d'un dictionnaire
    dont les clés sont : nom, coût, pourcentage de bénéfice après 2 ans,
    dividendes sur 2 ans
    """
    actions_as_dict = []
    for action in clean_data:
        cost = action[1]
        pourcentage_of_gain_over_2_years = action[2]
        dividend_over_2_years = cost * pourcentage_of_gain_over_2_years / 100
        global_yield = (dividend_over_2_years / 2) / cost * 100

        dico_action = {
            "nom": action[0],
            "coût": cost,
            "pourcentage de bénéfice après 2 ans": pourcentage_of_gain_over_2_years,
            "dividendes sur 2 ans": dividend_over_2_years,
            "rendement global": global_yield
        }

        actions_as_dict.append(dico_action)
    return actions_as_dict


def glouton(liste_actions: list[dict], budget=500):
    """
    Prendre l'action au meilleur rendement,
    la retirer des dispos et du budget et l'ajouter au meilleur panier
    continuer avec la prochaine action avec le meilleur rendement
    qui rentre encore dans le budget
    """
    budget_restant = budget
    liste = sorted(liste_actions, key=lambda k: k["rendement global"], reverse=True)
    meilleur_panier = []

    for action in liste:

        if budget_restant - action["coût"] <= 0:
            if liste == []:
                return meilleur_panier
            else:
                liste.remove(action)
                continue

        else:
            liste.remove(action)
            budget_restant = budget_restant - action["coût"]
            meilleur_panier.append(action)

    return meilleur_panier


def check_perf(f, *args):
    """Dans la lambda, on peut passer la fonction avec ses arguments"""
    print(timeit.timeit(lambda: f(*args), number=1))


if __name__ == "__main__":
    a_analyser: str = dataset1

    start_time = time.time()
    list_of_actions = recuperer_liste_actions(a_analyser)[:900]
    taille_liste = len(list_of_actions)
    clean_list = clean_data(list_of_actions)
    list_of_dicos = create_dictionaries(clean_list)

    meilleur_panier = glouton(list_of_dicos)

    temps_programme = "%s seconds" % (time.time() - start_time)

    print(f"\nRAPPORT: {a_analyser}")
    print(f"liste de {taille_liste} éléments")
    print("----------Meilleur panier----------")
    for action in meilleur_panier:
        print(action["nom"])
    print("\n- Coût total du panier:  ", end='')
    print(sum(action["coût"] for action in meilleur_panier))
    print("- dividendes sur 2 ans:  ", end='')
    print(sum(action["dividendes sur 2 ans"] for action in meilleur_panier))
    print("- Temps d'exécution pour la fonction \"glouton\":  ", end='')
    check_perf(glouton, list_of_dicos)
    print(timeit.repeat(lambda: glouton(list_of_dicos), number=1))
    print("- Temps d'exécution de tout le programme (avec aléas du système):  ", end='')
    print(temps_programme)
    print()
