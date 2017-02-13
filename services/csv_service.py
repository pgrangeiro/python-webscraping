import csv


class CSVService:

    @classmethod
    def write(cls, *args):
        with open('output.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(args)
