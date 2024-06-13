import os


def list_files():
    """
    Liste les fichiers présents dans le dossier files et retourne la liste des noms des fichiers à l'intérieur


    :return: La liste de fichiers dans le dossier files
    :rtype: list[str]
    """
    print("\nVeuillez choisir un fichier dans la liste suivante")
    files = os.listdir("./files")
    for index, file in enumerate(files, start=1):
        print(f'{index} - {file}')
    return files


def list_actions():
    """
    Liste les actions disponibles et retourne le choix


    :return: Le choix de l'utilisateur
    :rtype: int
    """
    print("\nVeuillez choisir une action dans la liste suivante")
    print("1 - Lire le fichier")
    print("2 - Exportez le fichier")
    return input("")
