import csv

def combine_csv():
    count = 0
    with open('names.csv', 'wb') as csvfile:

        fieldnames = ['Name', 
                      'Current Employer', 
                      'Current City',
                      'Email',
                      'Phone Number',
                      'Major',
                      'Graduation Year',
                      'Hometown',
                      'Pledge Class',
                      'Family',
                      'Nickname',
                      'Info']

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        with open('AlumniInformationUpgraded.csv', 'Urb') as read_1:
            writer.writeheader()
            for row in read_1:
                if count == 0:
                    count += 1
                    continue
                row = row.split(',')
                retrived = retrive_val(row[0])
                retrived[1] = retrived[1].split(':')[1][1:]
                writer.writerow({'Name': row[0], 
                                 'Current Employer': row[1],
                                 'Current City': row[2].replace('"', ''),
                                 'Email' : row[3],
                                 'Phone Number': row[4],
                                 'Major': row[5],
                                 'Graduation Year': row[6],
                                 'Hometown': row[7],
                                 'Pledge Class': row[8],
                                 'Nickname': retrived[0],
                                 'Family': retrived[1]})

def retrive_val(val):
    nickname = ''
    family = ''
    bio = ''
    with open('data.csv', 'Urb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == val:
                nickname = row[2]
                family = row[1]
                bio = row[3]
    return [nickname, family, bio]
             

if __name__ == '__main__':
    combine_csv()    
