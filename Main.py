from Api import Api
from Read_data import File

if __name__ == '__main__':
    """
    Main which read file
    """
    file = File()
    api_arr = []
    for i in range(file.size):
        api_arr.append(Api(float(file.price[i]), file.link[i]))
    while True:
        for i in range(file.size):
            api_arr[i].retrive_and_check()
