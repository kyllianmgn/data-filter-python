from utils.utils import list_files, list_actions
from csv_manager.csv_handler import CSVHandler
from json_manager.json_handler import load_json_file, save_json_file

def main():
    while True:
        file_list = list_files()
        choice = input("")
        if (choice.isdigit() and 0 <= int(choice) - 1 < len(file_list)) or choice in file_list:
            if choice.isdigit():
                choice = file_list[int(choice) - 1]
            extension = choice.split(".")[-1]
            file = None
            match extension:
                case "csv":
                    file = CSVHandler(choice)
            data = file.read()
            while choice:
                action_choice = list_actions()
                match action_choice:
                    case "1":
                        file.print()
                    case "2":
                        file.save(input("Quelle nom pour le fichier de sortie ?") + ".csv", data)
                    case _:
                        print("Veuillez choisir un choix dans la liste")

        elif choice == "exit":
            exit(0)
        else:
            print("Votre choix n'est pas dans le dossier")


if __name__ == "__main__":
    main()
