from csv_manager.csv_convertor import convert_to_csv
from json_manager.json_convertor import convert_to_json
from csv_manager.csv_handler import CSVHandler
from json_manager.json_handler import JSONHandler
from utils.fields import manage_field
from utils.filter import process_filtering
from utils.sort import sort_data_by_value
from utils.stats import get_statistics, statistics_actions, print_statistics
from utils.utils import list_files, list_actions, print_data
from xml_manager.xml_handler import XMLHandler


def main():
    try:
        while True:
            undo = []
            redo = []
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
                undo.append(data)
                action_choice = None
                while action_choice != "0":
                    action_choice = list_actions(choice)
                    if len(undo) > 1:
                        print("Vous avez aussi la possibilité d'annuler avec undo")
                    if len(redo) > 0:
                        print("ou d'avancer avec redo")
                    match action_choice:
                        case "1":
                            print_data(data)
                        case "2":
                            output_name = input("Quel nom pour le fichier de sortie ? ")
                            export_format = "jaga"
                            while export_format.lower() not in ["json", "csv", "xml"]:
                                export_format = input("Quel format pour le fichier de sortie (json,csv) ? ")
                                match export_format.lower():
                                    case "json":
                                        export = convert_to_json(data)
                                        file.save(output_name + ".json", export)
                                    case "csv":
                                        convert_to_csv(data, output_name)
                                    case _:
                                        print("Veuillez choisir un choix dans la liste suivante.")
                            print("Données sauvegardées avec succès.")
                        case "3":
                            for (i, column) in enumerate(list(data[0]), start=1):
                                print(f"{i}) {column}")
                            field_number = input("Numéro du champ de tri : ")
                            data = sort_data_by_value(data, int(field_number))
                            print_data(data)
                        case "4":
                            stats = get_statistics(data)
                            s_choice = None
                            while s_choice not in ["1", "2", "3"]:
                                s_choice = statistics_actions()
                                match s_choice:
                                    case "1":
                                        print_statistics(stats)
                                    case "2":
                                        output_name = input("Quel nom pour le fichier de sortie ? ")
                                        file.save(output_name + ".json", stats)
                                        print("Données exportés avec succès.")
                                    case _:
                                        print("Veuillez choisir un choix dans la liste suivante.")
                        case "5":
                            undo.append(data)
                            for (i, column) in enumerate(list(data[0]), start=1):
                                print(f"{i}) {column}")
                            field_number = input("Numéro du champ à filter : ")
                            response = process_filtering(field_number, data)
                            if response:
                                data = response
                        case "6":
                            response = manage_field(data)
                            if response:
                                data = response
                            undo.append(data)
                        case "undo":
                            if len(undo) > 1:
                                data = undo.pop()
                            print("Dernière Action Annulé.")
                            print_data(data)
                        case "redo":
                            if len(redo) > 0:
                                data = redo.pop()
                            print("Dernière Action Restoré.")
                            print_data(data)
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
