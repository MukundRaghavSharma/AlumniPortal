import csv

def get_first(max_count = 10):
        brothers = []
        read_file = open('static/AlumniInformationUpgraded.csv', 'Ur')
        csv_file = csv.reader(read_file, delimiter=',')
        count = 0 
        for row in csv_file:
            if count == 0:
                count += 1
                continue
            if count == max_count:
                break
            name = row[0].split(' ')
            del row[0]
            row.insert(0, name[0])
            row.insert(1, name[1])
            brothers.append(row)
            count += 1
        read_file.close()
        return brothers
