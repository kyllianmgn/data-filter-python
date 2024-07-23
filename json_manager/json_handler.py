import json
import os

import numpy

from file.file_class import File


class JSONHandler(File):

    def __init__(self, file):
        self.file = file

    def load(self):
        """
            Charger le fichier json
            :param file: Chemin vers le fichier json
            :return: JSON Object
            """
        with open(f'./files/{self.file}', 'r') as json_file:
            json_data = json.load(json_file)
        return json_data

    def print(self):
        """
            Afficher le contenu du fichier json

            :param json_data: JSON Object
            """
        with open(f'./files/{self.file}', 'r') as json_file:
            json_data = json.load(json_file)
            print(json_data)

    def read(self):
        """
            Lire le contenu du fichier json

            :param json_data: JSON Object
            """
        with open(f'./files/{self.file}', 'r') as json_file:
            json_data = json.load(json_file)
        header_columns = []
        data = [""]
        print(json_data)
        for row in json_data:
            for columns in row.keys():
                header_columns.append(columns)
        indexes = numpy.unique(header_columns, return_index=True)[1]
        data[0] = [header_columns[index] for index in sorted(indexes)]
        for item in json_data:
            item_to_add = []
            for column in data[0]:
                if column in item:
                    item_to_add.append(item[column])
                else:
                    item_to_add.append(None)
            data.append(item_to_add)
        return data

    def save(self, output, data):
        """
            Enregistre les données dans un fichier JSON.

            Args:
                output (str): Chemin vers le fichier JSON de destination.
                data (dict ou list): Les données à enregistrer.

            Raises:
                IOError: Si une erreur se produit lors de l'écriture du fichier.
            """
        output_path = f'./output/{output}'
        try:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file, indent=4)
                print(f"Les données ont été enregistrées dans '{output_path}'")
        except IOError as e:
            raise IOError(f"Erreur lors de l'écriture du fichier '{output_path}': {e}")

