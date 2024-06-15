import json
import os

def load_json_file(file):
    """
    Charger le fichier json
    :param file: Chemin vers le fichier json
    :return: JSON Object
    """
    with open(f'{file}', 'r') as json_file:
        json_data = json.load(json_file)
    return json_data

def read_json_file(file):
    """
    Lire le contenu du fichier json

    :param json_data: JSON Object
    """
    with open(f'{file}', 'r') as json_file:
        json_data = json.load(json_file)
    return json_data


def save_json_file(output, data):
    """
    Enregistre les données dans un fichier JSON.

    Args:
        output (str): Chemin vers le fichier JSON de destination.
        data (dict ou list): Les données à enregistrer.

    Raises:
        IOError: Si une erreur se produit lors de l'écriture du fichier.
    """
    try:
        os.makedirs(os.path.dirname(output), exist_ok=True)
        with open(output, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
    except IOError as e:
        raise IOError(f"Erreur lors de l'écriture du fichier '{output}': {e}")

