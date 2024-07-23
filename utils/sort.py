import pandas as pd

from utils.utils import dataframe_to_list


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
