import os


def list_files():
    """
    Liste les fichiers présents dans le dossier files et retourne la liste des noms des fichiers à l'intérieur


    :return: La liste de fichiers dans le dossier files
    :rtype: list[str]
    """
    print("========================Selection de fichier========================")
    print("\nVeuillez choisir un fichier dans la liste suivante")
    files = os.listdir("./files")
    for index, file in enumerate(files, start=1):
        print(f'{index} - {file}')
    return files


def list_actions(name):
    """
    Liste les actions disponibles et retourne le choix


    :return: Le choix de l'utilisateur
    :rtype: int
    """
    print(f"========================Edition de {name}========================")
    print("\nVeuillez choisir une action dans la liste suivante")

    print("\nLecture & Exportation :")
    print("1 - Lire le fichier")
    print("2 - Exportez le fichier\n")

    print("\nManipulation des données :")
    print("3 - Trier en fonction d'un champ")
    print("4 - Avoir les statistiques pour chaque colonne")
    print("5 - Filtrer les données")
    print("6 - Gestion de champs")

    print("0 - Retour")
    return input("")


def print_data(data):
    """
    Affiche les donnés sous formes de tableau

    :param data:
    :return:
    """
    for row in data:
        for column in row:
            print(column, end=', ')
        print('\n')


def is_unique(s):
    a = s.to_numpy()
    return (a[0] == a).all()


def return_column_type(df):
    types = df.map(type)
    if is_unique(types[df.columns[0]]):
        return types.iloc[:, 0][0]
    return False


def dataframe_to_list(df):
    return [df.columns.to_list(), *df.values.tolist()]
