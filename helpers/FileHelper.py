import os

class FileHelper:
    data_file_directory = os.path.abspath(os.curdir) + '/csv/'

    def append_to_file(file, data):
        f = open(FileHelper.data_file_directory + file, 'a+')
        f.write(','.join(data) + "\r\n")
        f.close()

    def get_file(file):
        return FileHelper.data_file_directory + file;


    def truncate_file(file):
        with open(FileHelper.data_file_directory + file, 'w'):
            pass