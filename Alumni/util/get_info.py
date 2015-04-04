import urllib
import csv
import BeautifulSoup

lost_boys = [4, 9, 20, 22, 34, 35, 36, 45, 50, 51, 54,   ]

def create_csv():
    with open('Alumni.csv', 'w') as csvfile:
        fieldnames = ['Number', 'Name', 'Major', 'Graduation Class', 'Hometown', 'Pledge Class', 'Nickname', 'Family']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
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
    create_csv()
