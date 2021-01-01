from Api import Api
from Read_data import File
from Sound import playing_sound_repeatedly

if __name__ == '__main__':
    file = File()
    api_arr = []
    for i in range(file.size):
        api_arr.append(Api(int(file.price[i]), file.link[i]))
    api_arr[0].retrive_and_check()