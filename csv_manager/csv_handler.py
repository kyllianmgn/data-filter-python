import csv


def load_csv(file):
    with open(f'./files/{file}', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
    return csv_reader


def print_csv(file):
    """
    Afficher le contenu du fichier csv

    :param csv_reader: CSV Object
    """
    with open(f'./files/{file}', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row)


def read_csv(file):
    """
    Afficher le contenu du fichier csv

    :param csv_reader: CSV Object
    """
    with open(f'./files/{file}', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        return list(csv_reader)



def save_csv(output, data):
    """
    Sauvegarde le contenu du fichier csv

    :param output: Le nom du fichier d'output
    :param data: Les données à écrire dans le fichier
    """
    with open(f'./output/{output}', 'w+', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerows(data)
