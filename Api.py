# required pip install
import requests
from Sound import playing_sound_repeatedly
import time
from Error_Checking import error_checking
# does not required pip install
import json

# small changes

#---------PRINTING COLOUR------------------#
def prGreen(skk):
    print("\033[92m {}\033[0m" .format(skk))
#---------PRINTING COLOUR------------------#

class Api:
    def __init__(self, price: int, link: str):
        self.link = link
        self.my_price = price
        self.data = None
        self.lowest_price = None

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
            raise TypeError("link is not working")

    def get_min_price(self) -> int:
        """
        get the minimum price from the data
        :return: minimum price
        """
        amount = float(self.data["data"][0]["price"]["amount"])  # amount in string
        # amount_size = len(amount) # get length of amount
        precision = int(self.data["data"][0]["price"]["token_precision"])  # get precision
        amount = amount / 10 ** precision
        return amount


    def is_min(self) -> bool:
        """
        checking price is minimum or not
        :return: True when my price is higher than min price
        """
        if self.lowest_price <= self.my_price:
            return True
        else:
            return False

    def get_collection_name(self) -> str:
        return self.data["data"][0]["assets"][0]["collection"]["collection_name"]

    def get_name(self) -> str:
        return self.data["data"][0]["assets"][0]["template"]["immutable_data"]["name"]

    def print_price(self):
        print("Set price : " + str(self.my_price) + ", lowest price : " + str(self.lowest_price) + ", collection name : " + self.get_collection_name() + ", name : " + self.get_name())

    def print_link(self):
        print("https://wax.atomichub.io/market/sale/" + self.data["data"][0]["sale_id"])

    def retrive_and_check(self) -> None:
        """
        check to min price
        """
        self.data = self.get_data()
        error_checking(self.data)
        self.lowest_price = self.get_min_price()
        self.print_price()
        if self.is_min() == True:
            # You can buy ....
            prGreen('******** Hit item, collection name: ' + self.get_collection_name() + ", schema name : " + self.get_name() + ", current price : " + str(self.lowest_price) + " WAX" " ******")
            self.print_link()
            playing_sound_repeatedly()