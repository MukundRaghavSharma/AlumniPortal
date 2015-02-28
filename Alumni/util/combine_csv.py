import csv

def combine_csv():
    count = 0
    with open('names.csv', 'w') as csvfile:

        fieldnames = ['Number',
                      'Name', 
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

        with open('AlumniInformationUpgraded.csv', 'r') as read_1:
            writer.writeheader()
            for row in read_1:
                if count == 0:
                    count += 1
                    continue
                row = row.split(',')
                #print (row)
                retrived = retrive_val(row[0])
                #retrived[1] = retrived[1].split(':')[1][1:]
                writer.writerow({'Number': retrived[3],
                                 'Name': row[0], 
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
    val = str(val)
    nickname = ''
    family = ''
    bio = ''
    number = ''
    with open('data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print ('Row', row)
            if str(row[1]) == val:
                nickname = row[3]
                family = row[2]
                bio = row[4]
                number = row[0]
        return [nickname, family, bio, number]
             
if __name__ == '__main__':
    combine_csv()    
