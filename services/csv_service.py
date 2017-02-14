import csv


class CSVService:

    @classmethod
    def write(cls, *args):
        with open('output.csv', 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(args)
