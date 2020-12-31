from Api import Api
from Read_data import read_file
from Sound import playing_sound_repeatedly

if __name__ == '__main__':
    link_and_price = read_file()
    api = Api(link_and_price[0]["price"], link_and_price[0]["link"])
    api.retrive_and_check()
    playing_sound_repeatedly()
