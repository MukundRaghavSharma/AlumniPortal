import urllib
import csv
import BeautifulSoup

lost_boys = [34, 35, 51, 66, 71, 74, 84, 85, 89, 90, 91,\
        96, 99, 104, 120, 123, 136, 139, 143, 153, 166, 172, \
        182, 183, 184, 189, 190, 191, 195, 197, 198, 199, 200, 202]

def create_lost_boys():
    with open('LostBoys.csv', 'w') as csvfile:
        fieldnames = ['Number', 'Name', 'Major', 'Graduation Class', 'Hometown', 'Pledge Class', 'Nickname', 'Family']
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()
        for lost in lost_boys:
            url = 'http://www.cmuakpsi.org/bro_profile.php?number='
            url += str(lost)
            raw = urllib.urlopen(url)
            soup = BeautifulSoup.BeautifulSoup(raw)
            name = soup.findAll('p')[0].contents[0]
            major = soup.findAll('p')[1].contents[0]
            graduation_class = soup.findAll('p')[2].contents[0]
            hometown = soup.findAll('p')[3].contents[0]
            pledge_class = soup.findAll('p')[4].contents[0]
            nickname = soup.findAll('p')[5].contents[0]
            family = soup.findAll('p')[6].contents[0]
            writer.writerow({'Number' : lost, 
                             'Name' : name, 
                             'Major' : major, 
                             'Graduation Class' : graduation_class, 
                             'Hometown' : hometown,
                             'Pledge Class' : pledge_class, 
                             'Nickname' : nickname, 
                             'Family' : family })


def create_csv():
    with open('Alumni.csv', 'w') as csvfile:
        fieldnames = ['Number', 'Name', 'Major', 'Graduation Class', 'Hometown', 'Pledge Class', 'Nickname', 'Family']
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()
        for i in range(204, 267): 
            url = 'http://www.cmuakpsi.org/bro_profile.php?number='
            url += str(i)
            raw = urllib.urlopen(url)
            soup = BeautifulSoup.BeautifulSoup(raw)
            name = soup.findAll('p')[0].contents[0]
            major = soup.findAll('p')[1].contents[0]
            graduation_class = soup.findAll('p')[2].contents[0]
            hometown = soup.findAll('p')[3].contents[0]
            pledge_class = soup.findAll('p')[4].contents[0]
            nickname = soup.findAll('p')[5].contents[0]
            family = soup.findAll('p')[6].contents[0]
            writer.writerow({'Number' : i, 
                             'Name' : name, 
                             'Major' : major, 
                             'Graduation Class' : graduation_class, 
                             'Hometown' : hometown,
                             'Pledge Class' : pledge_class, 
                             'Nickname' : nickname, 
                             'Family' : family })

if __name__ == '__main__':
    create_lost_boys()
    #create_csv()
