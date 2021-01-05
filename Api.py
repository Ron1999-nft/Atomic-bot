# required pip install
import requests
from Sound import playing_sound_repeatedly
import time

# does not required pip install
import json

#---------PRINTING COLOUR------------------#
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk), end = '')
#---------PRINTING COLOUR------------------#

class Api:
    def __init__(self, price: int, link: str):
        self.link = link
        self.my_price = price
        self.data = self.__get_data()
        self.lowest_price = self.__get_min_price()

    def __get_data(self) -> dict:
        """
        get the data from the link
        :return: dictionary which contain the data
        """
        try:
            # TIme delay cause there is a rate limit in the api
            time.sleep(5)
            data = requests.get(self.link)
            return json.loads(data.text)
        except:
            print("API is not working 1")
            print(self.data)
            self.retrive_and_check()

    def __get_min_price(self) -> int:
        """
        get the minimum price from the data
        :return: minimum price
        """
        try:
            amount = float(self.data["data"][0]["price"]["amount"])  # amount in string
            # amount_size = len(amount) # get length of amount
            precision = int(self.data["data"][0]["price"]["token_precision"])  # get precision
            amount = amount / 10 ** precision
            return amount
        except:
            print(self.data)
            print("API is not working 2")
            self.retrive_and_check()

    def __is_min(self) -> bool:
        if self.lowest_price <= self.my_price:
            return True
        else:
            return False

    def __get_collection_name(self) -> str:
        return self.data["data"][0]["assets"][0]["collection"]["collection_name"]

    def __get_name(self) -> str:
        return self.data["data"][0]["assets"][0]["template"]["immutable_data"]["name"]

    def __get_rarity(self) -> str:
        return self.data["data"][0]["assets"][0]["template"]["immutable_data"]["rarity"]

    def __print_price(self):
        prYellow("Set price : " + str(self.my_price)) 
        print( ", lowest price : " + str(self.lowest_price) + ", collection name : " + self.__get_collection_name() + ", name : " + self.__get_name())

    def retrive_and_check(self) -> None:
        self.data = self.__get_data()
        self.lowest_price = self.__get_min_price()
        self.__print_price()
        if self.__is_min() == True:
            # You can buy ....
            prGreen('******** Hit item, collection name: ' + self.__get_collection_name() + ", schema name : " + self.__get_name() + ", current price : "  + str(self.lowest_price) + " WAX" " ******")
            playing_sound_repeatedly()





