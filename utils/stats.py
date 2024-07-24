import statistics

import pandas as pd

from utils.utils import is_unique


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

