from utils.utils import list_files, list_actions
from csv_manager.csv_handler import CSVHandler
from json_manager.json_handler import JSONHandler

def main():
    while True:
        file_list = list_files()
        print("Entrez un numéro de fichier ou 'exit' pour quitter.")
        choice = input("")
        if (choice.isdigit() and 0 <= int(choice) - 1 < len(file_list)) or choice in file_list:
            if choice.isdigit():
                choice = file_list[int(choice) - 1]
            extension = choice.split(".")[-1]
            file = None
            match extension:
                case "csv":
                    file = CSVHandler(choice)
                case "json":
                    file = JSONHandler(choice)
            data = file.read()
            action_choice = None
            while action_choice != "back":
                action_choice = list_actions()
                match action_choice:
                    case "1":
                        file.print()
                    case "2":
                        output_name = input("Quel nom pour le fichier de sortie ? ")
                        file.save(output_name + "." + extension, data)
                        print("Données sauvegardées avec succès.")
                    case "back":
                        print("Retour au menu principal.")
                        break  # Sort de la boucle interne pour revenir au choix du fichier
                    case _:
                        print("Veuillez choisir un choix dans la liste ou 'back' pour revenir.")
        elif choice == "exit":
            exit(0)
        else:
            print("Votre choix n'est pas valide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
