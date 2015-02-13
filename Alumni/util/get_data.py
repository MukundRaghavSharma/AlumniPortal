import csv

def get_all():
        brothers = []
        read_file = open('static/AlumniInformationUpgraded.csv', 'Ur')
        csv_file = csv.reader(read_file, delimiter=',')
        count = 1
        for row in csv_file:
            if count == 1:
                count += 1
                continue
            name = row[0].split(' ')
            del row[0]
            row.insert(0, name[0])
            row.insert(1, name[1])
            brothers.append(row)
        read_file.close()
        return brothers
