from utils.utils import list_files, list_actions, sort_data_by_value
from csv_manager.csv_handler import CSVHandler
from json_manager.json_handler import JSONHandler
from xml_manager.xml_handler import XMLHandler


def main():
    try:
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
                    case "xml":
                        file = XMLHandler(choice)
                data = file.read()
                action_choice = None
                while action_choice != "0":
                    action_choice = list_actions()
                    match action_choice:
                        case "1":
                            file.print()
                        case "2":
                            output_name = input("Quel nom pour le fichier de sortie ? ")
                            file.save(output_name + "." + extension, data)
                            print("Données sauvegardées avec succès.")
                        case "3":
                            field_number = input("Numéro du champ de tri : ")
                            file = sort_data_by_value(data, int(field_number))
                        case "back":
                            print("Retour au menu principal.")
                            break
                        case _:
                            print("Veuillez choisir un choix dans la liste suivante.")
            elif choice == "exit":
                exit(0)
            else:
                print("Votre choix n'est pas valide. Veuillez réessayer.")

    except KeyboardInterrupt:
        print("Programme interrompu par l'utilisateur. Fermeture propre.")

if __name__ == "__main__":
    main()
