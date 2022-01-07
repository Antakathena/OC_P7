import itertools
import pandas as pd

test = "AlgoInvest_actions.csv"
dataset1 = "dataset1_Python+P7.csv"
dataset2 = "dataset2_Python+P7.csv"
fichier_csv: str = test

ACTIONS = pd.read_csv(fichier_csv)

action["coût"] = ? # float
action["rendement"] = ? # float
panier["coût total"] = ? # float
panier["rendement global total"] = ? # float

def prepa_data(ACTIONS):


def glouton(actions: pd.Dataframe, budget=500):
# tri
# est-ce qu'on tri d'abord les actions par rendement global pour éliminer celles qui sont vraiment moches?
# ou est-ce qu'on selectionne de base le meilleur rendement + le meilleur rendement etc jusqu'à atteindre le budget?
actions = actions.sort_values (by = "rendement", ascending=False)

# là trouver comment ne garder que les paniers < budget
actions["coût total"] = actions[?].cumsum()

# puis ne garder que le meilleur rendement global total

"""
Notes sur Pandas :
import numpy as np
import matplotlib as plt # directement lié à pandas
import pandas as pd

data = pd.read_csv("titre du csv")

data.shape # nombre de lignes
data.head() # check si bien chargé


"""