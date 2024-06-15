from utils.utils import list_files, list_actions
from csv_manager.csv_handler import load_csv, print_csv, save_csv, read_csv
from json_manager.json_handler import load_json_file, save_json_file



def main():
    while True:
        file_list = list_files()
        choice = input("")
        if (choice.isdigit() and 0 <= int(choice) - 1 < len(file_list)) or choice in file_list:
            if choice.isdigit():
                choice = file_list[int(choice) - 1]
            extension = choice.split(".")[-1]
            if extension == "csv":
                data = read_csv(choice)
            elif extension == "json":
                data = load_json_file(f"./files/{choice}")
            else:
                print("Extension de fichier non prise en charge.")
                continue
            while choice:
                action_choice = list_actions()
                match action_choice:
                    case "1":
                        match extension:
                            case "csv":
                                print_csv(choice)
                            case "json":
                                print(data)
                    case "2":
                        output_file = input("Quel nom pour le fichier de sortie ? ") + "." + extension
                        match extension:
                            case "csv":
                                save_csv(f"./output/{output_file}", data)
                            case "json":
                                save_json_file(f"./output/{output_file}", data)
                    case "*":
                        print("Veuillez choisir un choix dans la liste")

        elif choice == "exit":
            exit(0)
        else:
            print("Votre choix n'est pas dans le dossier")


if __name__ == "__main__":
    main()
