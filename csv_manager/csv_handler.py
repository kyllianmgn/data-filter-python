import csv
import os.path
from file.file_class import File


class CSVHandler(File):

    def __init__(self, file):
        self.data = None
        self.file = file

    def load(self):
        with open(f'./files/{self.file}', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
        return csv_reader

    def print(self):
        """
        Afficher le contenu du fichier csv
        """
        with open(f'./files/{self.file}', 'r') as csv_file:
            data = list(csv.reader(csv_file, delimiter=','))
            for row in data:
                for column in row:
                    print(column, end=', ')
                print('\n')

    def read(self):
        """
        Afficher le contenu du fichier csv
        """
        with open(f'./files/{self.file}', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            return list(csv_reader)

    def save(self, output, data):
        """
        Sauvegarde le contenu du fichier csv

        :param output: Le nom du fichier d'output
        :param data: Les données à écrire dans le fichier
        """
        if not os.path.isdir("./output"):
            os.mkdir("./output")
        with open(f'./output/{output}', 'w+', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerows(data)
