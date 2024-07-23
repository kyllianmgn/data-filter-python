import os
import statistics

from operator import itemgetter
import pandas as pd


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


def sort_data_by_value(data, field_number):
    """
    Trie les données par les valeurs du champ

    :return: Les données triées par les valeurs du champ
    :rtype: data
    """
    df = pd.DataFrame(data[1:], columns=data[0])
    b_choice = "999"
    while b_choice not in ["0", "1"]:
        b_choice = input("Veuillez choisir Ascendant (1) ou Descendant (0)")
        if not b_choice.isdigit():
            continue
    boolean = None
    if b_choice == "0":
        boolean = False
    else:
        boolean = True
    return dataframe_to_list(df.sort_values(by=df.columns[field_number-1], ascending=boolean))


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


def statistics_actions():
    print("\nVeuillez choisir une action dans la liste suivante")
    print("1 - Afficher les statistiques")
    print("2 - Exporter les statistiques")
    print("0 - Retour")
    return input("")


def get_statistics(data):
    """
    Affiche les statistiques du champ

    :param data:
    :return:
    """
    df = pd.DataFrame(data[1:], columns=data[0])
    df_type = df.map(type)
    types_to_keep = []
    for types in df_type.columns:
        if df_type[types][0] == list:
            df[types] = df[types].map(lambda x: statistics.mean(x))
        df_type = df.map(type)
        if is_unique(df_type[types]) and df_type[types][0] != str and df_type[types][0] != list:
            types_to_keep.append(types)
    df_to_stats = df[types_to_keep].mean()
    df_to_stats = df_to_stats.to_dict()
    stats = []
    for key, value in df_to_stats.items():
        data_type = None
        result_value = value
        if df_type[key][0] == int:
            data_type = "Integer"
            result_value = {"Minimum": int(df[key].min()), "Maximum": int(df[key].max()), "Moyenne": value}
        elif df_type[key][0] == float:
            data_type = "Float"
        elif df_type[key][0] == bool:
            data_type = "Boolean"
        stats.append({"type": data_type, "column": key, "value": result_value})
    return stats


def print_statistics(stats):
    """
    Affiche les statistiques

    :param stats:
    :return:
    """
    for stat in stats:
        print(f"Colonne {stat['column']} de type {stat['type']} : {stat['value']}")


def is_unique(s):
    a = s.to_numpy()
    return (a[0] == a).all()


def return_column_type(df):
    types = df.map(type)
    if is_unique(types[df.columns[0]]):
        return types.iloc[:, 0][0]
    return False


def filter_actions():
    print("\nVeuillez choisir une action dans la liste suivante")
    print("1 - Afficher les statistiques")
    print("2 - Exporter les statistiques")
    print("0 - Retour")
    return input("")


def process_filtering(field_number, data):
    df = pd.DataFrame(data[1:], columns=data[0])
    column_name = df.columns[int(field_number)-1]
    only_wanted = df.iloc[:, int(field_number)-1]
    column_type = return_column_type(only_wanted.to_frame())

    if column_type == str:
        regex = input("Veuillez rentrez la chaînes de caractères voulu : ")
        df = df.query(f"{column_name}.str.match('{regex}')")
    elif column_type == float or column_type == int:
        op_choice = "999"
        while op_choice not in ["0","1", "2","3","4"]:
            op_choice = input("Veuillez choisir si vous voulez :\n 1) >= (Supérieur ou égale)\n 2) >(Supérieur)\n 3) "
                              "<= (Inférieur ou égale)\n 4) <(Inférieur)\n 0) Annulez\n")
            if not op_choice.isdigit():
                continue
        operator = None
        match op_choice:
            case "1":
                operator = ">="
            case "2":
                operator = ">"
            case "3":
                operator = "<="
            case "4":
                operator = "<"
        value = "non non non"
        while not value.isdigit() and op_choice != "0":
            value = input("Veuillez choisir votre valeur : \n")
            if not value.isdigit():
                continue
        if op_choice != "0":
            df = df.query(f"{column_name} {operator} {value}")
        else:
            print("Opération annulé")
    elif column_type == bool:
        b_choice = "999"
        while b_choice not in ["0", "1"]:
            b_choice = input("Veuillez choisir Vrai (1) ou Faux (0)")
            if not b_choice.isdigit():
                continue
        boolean = None
        if b_choice == "0":
            boolean = "False"
        else:
            boolean = "True"
        df = df.query(f"{column_name} == {boolean}")
    else:
        return False

    final_data = dataframe_to_list(df)
    return final_data


def dataframe_to_list(df):
    return [df.columns.to_list(), *df.values.tolist()]