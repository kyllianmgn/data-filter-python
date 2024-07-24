import pandas as pd

from utils.utils import return_column_type, dataframe_to_list


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
        while op_choice not in ["0", "1", "2", "3", "4"]:
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
