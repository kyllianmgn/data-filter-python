import pandas as pd

from utils.utils import dataframe_to_list


def manage_field(data):
    print_field_menu()

    df = pd.DataFrame(data[1:], columns=data[0])
    f_choice = "999"
    while f_choice not in ["0", "1", "2"]:
        f_choice = input("")
        if not f_choice.isdigit():
            continue
    match f_choice:
        case "1":
            field_number = "non"
            while not field_number.isdigit() or int(field_number) > len(data[0]) or int(field_number) < 0:
                for (i, column) in enumerate(list(data[0]), start=1):
                    print(f"{i}) {column}")
                field_number = input("Numéro du champ à supprimer : ")
            print(f"Colonne {df.columns[int(field_number)-1]} supprimé")
            df.drop(columns=[df.columns[int(field_number)-1]], inplace=True)
        case "2":
            field_to_add = input("Nom du champ à rajouté : ")
            values_to_add = []
            after_position = "nan"
            while not after_position.isdigit() or int(after_position) > len(data[0]) or int(after_position) < 0:
                for (i, column) in enumerate(list(data[0]), start=1):
                    print(f"{i}) {column}")
                after_position = input("Numéro du champ à supprimer : ")
            stopped = 0
            for index, row in enumerate(data[1:], start=1):
                print(index)
                print(*row)
                value_to_add = input("Valeur à rajouté pour la données indiqué au dessus\n \"skip\" pour passer la "
                                     "valeur actuelle, \"skipall\" pour passer tout le reste\n")
                match value_to_add:
                    case "skip":
                        values_to_add.append(None)
                        continue
                    case "skipall":
                        stopped = len(data[1:]) - (index-1)
                        break
                    case _:
                        if value_to_add.isdigit():
                            value_to_add = int(value_to_add)
                        values_to_add.append(value_to_add)
            empty_remaining = [None] * stopped
            series = pd.Series(values_to_add+empty_remaining)
            df.insert(loc=int(after_position), column=field_to_add, value=series)
    print(df)
    return dataframe_to_list(df)


def print_field_menu():
    print("\nVeuillez choisir une action dans la liste suivante")
    print("1 - Supprimer un champ")
    print("2 - Créer un champ")
    print("0 - Retour")