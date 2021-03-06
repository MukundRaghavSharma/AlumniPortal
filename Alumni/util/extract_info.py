from bs4 import BeautifulSoup
import codecs
import csv
import unicodedata
import urllib.request

class AlumniData(object):
    def __init__(self, name, number, nickname = '', family = '', info = ''):
        self.name = name
        self.nickname = nickname
        self.family = family
        self.info = info
        self.number = number

    def __str__(self):
        return self.name

def get_info():
    alumni = []
    for num in range(1, 210):
        url = 'http://www.cmuakpsi.org/bro_profile.php?number='
        url += str(num)
        raw = urllib.request.urlopen(url)
        soup = BeautifulSoup(raw)
        paras = soup.findAll('p')
        name = soup.findAll('p')[0].contents[0]
        nickname = ''
        family = ''
        info = ''
        for i in range(0, len(soup.findAll('p'))):
            if 'Nickname' in soup.findAll('p')[i].contents[0]:
                nickname = soup.findAll('p')[i].contents[0] 
            if 'Family' in soup.findAll('p')[i].contents[0]:
                family = soup.findAll('p')[i].contents[0]
        
        nickname = nickname.split(':')[1:]
        if len(nickname) < 1:
            nickname = ''
        else:
            nickname = nickname[0][1:]

        if len(family) < 1:
            family = ''
        else:
            family = family.encode('utf-8')

        if len(soup.findAll('em')) > 0:
            info = soup.findAll('em')[0].contents[0]
            info = info.encode('utf-8')

        name = name.encode('utf-8')
        name = name.decode('utf-8')
        nickname = nickname.encode('utf-8')
        #family = family.decode('utf-8')
        print (name, ' ', num, ' ', nickname, ' ', family, ' ', info)
        alumn = AlumniData(name, num, nickname, family, info)
        alumni.append(alumn)
    return alumni

def add_to_csv(alumni):
    with open('data.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        for alumn in alumni:
            alumn_list = [alumn.number, alumn.name, alumn.family, alumn.nickname, alumn.info]
            writer.writerow(alumn_list)

def encode(s, name, *args, **kwargs):
    codec = codecs.lookup(name)
    rv, length = codec.encode(s, *args, **kwargs)
    if not isinstance(rv, (str, bytes, bytearray)):
        raise TypeError('Not a string or byte codec')
    return rv

if __name__ == '__main__':
    add_to_csv(get_info())
