"""
Docstring pour main
"""
#### Imports et définition des variables globales

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open(filename, mode="r", encoding="utf8") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if line != "":
            l.append([int(x) for x in line.split(";")])
    return l

def get_list_k(data, k):
    """
    Retourne la liste d'indice k contenue dans la liste de listes data.
    """
    l = data[k]
    return l

def get_first(l):
    """
    Retourne le premier élément de la liste
    """
    return l[0]

def get_last(l):
    """
    Retourne le dernier élément de la liste
    """
    return l[-1]

def get_max(l):
    """
    Retourne la valeur maximale de la liste
    """
    return max(l)

def get_min(l):
    """
    Retourne la valeur minimale de la liste
    """
    return min(l)

def get_sum(l):
    """
    Retourne la somme de la liste
    """
    return sum(l)


#### Fonction principale


def main():
    """
    Test de la fonction
    """
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
