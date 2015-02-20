import os

if __name__ == '__main__':
    for filename in os.listdir("."):
        new_file_name = filename.split('.')
        if len(new_file_name) > 2:
            new_file_name = new_file_name[1] + '.' + new_file_name[2] + '.jpg'
            os.rename(filename, new_file_name)
