import csv
import os
import sys
from tornado.web import RequestHandler

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  

class SearchService(RequestHandler):
    def search_all(self):
        brothers = []
        read_file = open('AlumniInformationUpgraded.csv', 'Ur')
        csv_file = csv.reader(read_file, delimiter=',')
        count = 1
        for row in csv_file:
            if count == 1:
                count += 1
                continue
            brothers.append(row)
        read_file.close()
        return brothers
    
    def get(self):
        brothers = []
        read_file = open('AlumniInformationUpgraded.csv', 'Ur')
        csv_file = csv.reader(read_file, delimiter=',')
        count = 1
        for row in csv_file:
            if count == 1:
                count += 1
                continue
            brothers.append(row)
        read_file.close()
        self.render("../front_end/index.html", results=brothers)
