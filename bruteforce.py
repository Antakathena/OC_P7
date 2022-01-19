import csv
import itertools
import timeit
import time

def recuperer_liste_actions() -> list :
    """
    récupère la data du csv. Dans l'ordre :
    nom, coût, % de gain sur 2 ans attention : tout est en str
    """
    with open ("OC_P7\AlgoInvest_actions.csv",'r') as data:
        reader = csv.reader(data)
        list_of_actions = list(reader)[1:]
    return list_of_actions

def create_dictionaries(list_of_actions)->list[dict]:
        """
        Renvoie la liste des actions, chacune sous forme d'un dictionnaire
        dont les clés sont : nom, coût, pourcentage de bénéfice après 2 ans,
        dividendes sur 2 ans 
        """
        actions_as_dict= []
        for action in list_of_actions:
            dico = {
                "nom":action[0],
                "coût":int(action[1]),
                "pourcentage de bénéfice après 2 ans":int(action[2].replace("%","")),
                "dividendes sur 2 ans": int(action[1])*int(action[2].replace("%",""))/100}
            actions_as_dict.append(dico)
        return actions_as_dict

def brute_force(actions_as_dict:list):
    """Créé une liste de tous les paniers d'action dont le montant total est inférieur à 500 €.
    Puis selection parmi ces paniers celui dont le rendement est le meilleur."""
    
    meilleur_panier = None
    meilleur_rendement = 0

    paniers_acceptables = []
    for i in range(2, len(actions_as_dict) + 1):
        paniers = itertools.combinations(actions_as_dict, i)
        for panier in paniers:
            cout_panier = sum(action["coût"] for action in panier)
            # memory concious vs sum([action["cout"] for action in panier]) time concious
            if cout_panier < 500:
                paniers_acceptables.append(panier)

    for panier in paniers_acceptables:
        rendement_panier = sum(action["dividendes sur 2 ans"] for action in panier)
        if rendement_panier > meilleur_rendement:
            meilleur_panier = panier
            meilleur_rendement = rendement_panier
    return meilleur_panier

def check_perf(f, *args):
    """dans la lambda on peut passer la fonction avec ses arguments"""
    print(timeit.timeit(lambda: f(*args), number = 1))
    print(timeit.repeat(lambda: brute_force(list_of_dicos), repeat=5, number=1))

if __name__ == "__main__":
    start_time = time.time()

    list_of_actions = recuperer_liste_actions()
    taille_liste = len(list_of_actions)
    
    list_of_dicos = create_dictionaries(list_of_actions)

    meilleur_panier = brute_force(list_of_dicos)

    temps_programme = "%s seconds" % (time.time() - start_time)

    print("\nRAPPORT:")
    print(f"liste de {taille_liste} éléments")
    print("----------Meilleur panier----------")
    for action in meilleur_panier:
        print(action["nom"])
    print("\n- Coût total du panier:  ", end ='')
    print(sum(action["coût"] for action in meilleur_panier))
    print("- dividendes sur 2 ans:  ", end ='')
    print(sum(action["dividendes sur 2 ans"] for action in meilleur_panier))
    print("- Temps d'execution pour la fonction de Force Brute:  ", end ='')
    check_perf(brute_force,list_of_dicos) 
    print("- Temps d'execution de tout le programme (avec aléas du système):  ", end ='')
    print(temps_programme)
    print()
