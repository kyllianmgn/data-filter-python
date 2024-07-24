import csv


def convert_to_csv(data, output_filename):
    with open(f"./output/{output_filename}.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)
