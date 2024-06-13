from utils.utils import list_files, list_actions
from csv_manager.csv_handler import load_csv, print_csv, save_csv, read_csv


def main():
    while True:
        file_list = list_files()
        choice = input("")
        if choice in file_list:
            extension = choice.split(".")[-1]
            data = read_csv(choice)
            while choice:
                action_choice = list_actions()
                match action_choice:
                    case "1":
                        match extension:
                            case "csv":
                                print_csv(choice)
                    case "2":
                        match extension:
                            case "csv":

                                save_csv(input("Quelle nom pour le fichier de sortie ?")+".csv", data)
                    case _:
                        print("Veuillez choisir un choix dans la liste")

        elif choice == "exit":
            exit(0)
        else:
            print("Votre choix n'est pas dans le dossier")


if __name__ == "__main__":
    main()
