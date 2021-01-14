from Api import Api
from Read_data import File

#---------PRINTING COLOUR------------------#
def prYellow(text):
    print('\033[33m', text, '\033[0m', sep='')
#---------PRINTING COLOUR------------------#

if __name__ == '__main__':
    """
    Main which read file and read file and determine
    """
    while True:
        filename = "Atomic.txt"
        filehandle = open(filename, 'r')
        while True:
            line = filehandle.readline()
            if not line:
                filehandle.close()
                break
            if line == "\n":
                continue
            if line[0] == "*":
                line = line.strip("\n")
                prYellow(line)
                continue
            line = line.strip("\n")
            line = line.split(" ")
            api = Api(float(line[0]),line[1])
            api.retrive_and_check()