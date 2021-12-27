# imports généraux
import csv
import itertools
import timeit
# imports locaux
# constantes
# main

def recuperer_dic_actions() -> csv.DictReader :
    """
    lors de la création de la DictReader, on rassemble le CSVfile avec un itertools.islice,
    ce qui fourni au constructeur de DictReader un itérateur sans la tranche-off,
    (ici la 1ère ligne, les headers, mais on peut retirer les lignes voulues).
    NB : ça marche aussi avec csv.reader

    Si fieldnames pas précisés, Dictreader prend les champs de la première ligne du csv comme clés
    """
    with open ("AlgoInvest_actions.csv",'r') as data:
        fieldnames = ['nom', 'coût', 'pourcentage de bénéfice après 2 ans']
        dic_actions = csv.DictReader(itertools.islice(data,1,None), fieldnames= fieldnames )

    return dic_actions

def from_DictReader_to_list_of_dict() -> list[dict] :
    with open ("AlgoInvest_actions.csv",'r') as data:
        fieldnames = ['nom', 'coût', 'pourcentage de bénéfice après 2 ans']
        dic_actions = csv.DictReader(itertools.islice(data,1,None), fieldnames= fieldnames )

        list_of_actions_as_dic = []
        for row in dic_actions :
            dico = {} # le dictionnaire de chaque action
            for key, value in row.items():
                if key == 'coût':
                    print(key, value)
                    print(type(value))
                    print(value.isdigit())
                    dico[key] = int(value)
                    print(type(value))
                elif key == 'pourcentage de bénéfice après 2 ans':
                    dico[key] = int(value.replace("%",""))
                else:
                    dico[key]= value
            list_of_actions_as_dic.append(dico)

        for row in dic_actions:
            print(row['nom'],row['coût'],row['pourcentage de bénéfice après 2 ans'])

        return list_of_actions_as_dic


def recuperer_liste_actions() -> list :
    with open ("AlgoInvest_actions.csv",'r') as data:
        reader = csv.reader(data)
        actions = list(reader)[1:]
    return actions
    

def rendement_sur_2_ans(list_of_actions_as_dic):
    results = []
    for action in list_of_actions_as_dic:
        rendement_sur_2_ans = action['coût']*action['pourcentage de bénéfice après 2 ans']/100
        action.update({'rendement sur 2 ans': rendement_sur_2_ans})
        results.append(action)
        for item in action.items():
            print(item)
    return results


if __name__ == "__main__":

    liste_de_dicos_par_action = from_DictReader_to_list_of_dict()
    print(len(liste_de_dicos_par_action))
    results = rendement_sur_2_ans(liste_de_dicos_par_action)

    



"""
actions_tup = [("Action-1",20,5/100),("Action-2",30,10/100), ("Action-3",50,15/100), ("Action-4",70,20/100), ("Action-5",60,17/100)]


costs = []
for action in actions :
    cost = action[1]
    action[1] = int(cost)
    costs.append(int(cost))


meilleur_panier = None
meilleur_rendement = 0
for i in range(2, lenght + 1):
    paniers = itertools.combinations(costs, i) # nb itertool
    for panier in paniers:
        cout_panier = sum(panier)
        if cout_panier < 500:
            print(panier)
"""

def brute_force(actions:list):
    #for action in actions:
    pass


# CSV.dictreader -> liste de dictionnaires (un par action)
# modif des dicos : Nom de l'action, coût, % sur 2 ans, rendement sur 2 ans
# ( pour opti ajouter rendement relatif absolu = dividende)
# pour chaque combinations pour paniers =< 500 faire :
#     récupérer le rendement total
#     comparer les paniers =< 500 en fonction du rendement total
# if rendement > meilleur_rendement, mettre à jour meilleur_rendement