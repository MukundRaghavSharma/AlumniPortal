import csv
import os.path

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../')

def get_first(max_count = 10):
        brothers = []
        read_file = open(os.path.join(BASE, 'static/AlumniInformationUpgraded.csv', ), 'Ur')
        csv_file = csv.reader(read_file, delimiter=',')
        count = 0 
        for row in csv_file:
            if count == 0:
                count += 1
                continue
            #if count == max_count:
            #    break
            name = row[0].split(' ')
            del row[0]
            row.insert(0, name[0])
            row.insert(1, name[1])
            brothers.append(row)
            count += 1
        read_file.close()
        return brothers

if __name__ == '__main__':
    for brother in get_first():
        for i in xrange(0, len(brother)):
            print i, ' ', brother[i]
        print '***********'
