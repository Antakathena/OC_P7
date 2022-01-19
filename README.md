# OC_P7
Programme d'étude de python 3
Comparaison entre deux type d'algorithmes.

## Infos Générales :
Il faut trouver le meilleur panier d'action avec un budget de 500 euros,
sachant que chaque action ne peut être choisie qu'une fois.
Les datasets utilisés sont des listes d'actions dont nous avons le nom, le prix et le pourcentage de rentabilité sur 2 ans.

## Utilité :
Comparaison entre  un algorithme de force brute (qui parcourt toutes les combinaisons possibles)
et un algorythme plus optimisé (ici algorythme glouton) pour le traitement d'un jeu de données.
Approche de la complexité algorithmique.

## Fonctionnalités :

Algorithme de Force Brute dans bruteforce.py pour un petit ensemble de données
Algorithme glouton optimisé dans optimisation.py qui peut être utilisé pour de plus grands ensembles.
optimisation.py effectue une préparation des données avant utilisation (ETL)
puis favorise les actions ayant un meilleur rendement global.
Dans les deux cas le module timeit est employé pour vérifier les performances.

### Fonctions :


## Instruction de démarrage :
Dans un terminal, utiliser les commandes suivantes :

$ python3 -m venv env (créé un dossier env dans le répértoire où vous vous trouvez)

$ source env/bin/activate (sous linux) ou env\Scripts\activate.bat (pour activer l'environnement virtuel sous windows)

$ git clone https://github.com/Antakathena/OC_P7

$ cd ../chemin/du/dossier (de la copie de OC_P7 dans votre dossier env)

$ pip install -r requirements.txt

$ python bruteforce.py ou optimisation.py
