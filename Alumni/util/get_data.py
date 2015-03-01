import csv
import os.path
import sys
if sys.version_info >= (3, 0):
    import urllib.request
else:
    import urllib
from bs4 import BeautifulSoup 

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../')

def get_first():
        brothers = []
        read_file = open(os.path.join(BASE, 'static/AlumniInformationUpgraded_new.csv', ), 'Ur')
        csv_file = csv.reader(read_file, delimiter=',')
        count = 0 
        for row in csv_file:
            if count == 0:
                count += 1
                continue
            name = row[1].split(' ')
            del row[1]
            row.insert(0, name[0])
            row.insert(1, name[1])
            brothers.append(row)
            count += 1
        read_file.close()
        return brothers

def get_number_dictionary():
    brother_dictionary = {}
    for i in range(1, 211):
        url = 'http://www.cmuakpsi.org/bro_profile.php?number='
        raw = urllib.request.urlopen(url + str(i))
        soup = BeautifulSoup(raw)
        name = soup.find('p').contents[0]
        brother_dictionary[name] = i
    return brother_dictionary

'''
def match_csv():
    read_file = open(os.path.join(BASE, 'static/AlumniInformationUpgraded.csv', ), 'Ur')
    csv_file = csv.reader(read_file, delimiter=',')
    for row in csv_file:
        for brother in get_number_dictionary().keys():
            if row[0] in brother:
                row.write(
'''
