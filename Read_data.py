def read_file() -> dict:
    """
    retrieve link and the price from the txt file
    :return: dictionary with price and link
    """
    link_and_price_array = []
    filename = "Atomic.txt"
    filehandle = open(filename, 'r')
    while True:
        line = filehandle.readline()
        if not line:
            break
        line = line.strip("\n")
        line = line.split(" ")

        link_and_price_array.append({"price" : int(line[0]), "link" : line[1]})

    filehandle.close()
    return link_and_price_array