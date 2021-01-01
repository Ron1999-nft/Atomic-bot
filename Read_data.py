class File():

    def __init__(self):
        self.size = 0
        self.link = []
        self.price = []
        self.__read_file()

    def __read_file(self) -> dict:
        """
        retrieve link and the price from the txt file
        :return: dictionary with price and link
        """
        filename = "Atomic.txt"
        filehandle = open(filename, 'r')
        while True:
            line = filehandle.readline()
            if not line:
                break
            line = line.strip("\n")
            line = line.split(" ")

            self.size = self.size + 1
            self.link.append(line[1])
            self.price.append(line[0])

        filehandle.close()