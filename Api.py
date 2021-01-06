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
        self.data = self.get_data()
        self.lowest_price = self.get_min_price()

    def get_data(self) -> dict:
        """
        get the data from the link
        :return: dictionary which contain the data
        """
        try:
            # TIme delay cause there is a rate limit in the api
            time.sleep(0.3)
            data = requests.get(self.link)
            return json.loads(data.text)
        except:
            print("API is not working 1")
            print(self.data)
            self.retrive_and_check()

    def get_min_price(self) -> int:
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

    def is_min(self) -> bool:
        if self.lowest_price <= self.my_price:
            return True
        else:
            return False

    def get_collection_name(self) -> str:
        return self.data["data"][0]["assets"][0]["collection"]["collection_name"]

    def get_name(self) -> str:
        return self.data["data"][0]["assets"][0]["template"]["immutable_data"]["name"]

    def get_rarity(self) -> str:
        return self.data["data"][0]["assets"][0]["template"]["immutable_data"]["rarity"]

    def print_price(self):
        print("Set price : " + str(self.my_price) + ", lowest price : " + str(self.lowest_price) + ", collection name : " + self.get_collection_name() + ", name : " + self.get_name())

    def retrive_and_check(self) -> None:
        self.data = self.get_data()
        self.lowest_price = self.get_min_price()
        self.print_price()
        if self.is_min() == True:
            # You can buy ....
            prGreen('******** Hit item, collection name: ' + self.get_collection_name() + ", schema name : " + self.get_name() + ", current price : " + str(self.lowest_price) + " WAX" " ******")






