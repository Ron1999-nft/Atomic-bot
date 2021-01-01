import requests
import json
from Sound import playing_sound_repeatedly

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
        data = requests.get(self.link)
        return json.loads(data.text)

    def __get_min_price(self) -> int:
        """
        get the minimum price from the data
        :return: minimum price
        """
        amount = float(self.data["data"][0]["price"]["amount"])  # amount in string
        # amount_size = len(amount) # get length of amount
        precision = int(self.data["data"][0]["price"]["token_precision"])  # get precision
        amount = amount / 10 ** precision
        return amount

    def __is_min(self) -> bool:
        if self.lowest_price <= self.my_price:
            self.__print_price()
            return True
        else:
            return False

    def __print_price(self):
        print("The lowest price is now " + str(self.lowest_price))
        
    def retrive_and_check(self) -> None:
        self.__print_price()
        self.data = self.__get_data()
        self.lowest_price = self.__get_min_price()
        if self.__is_min() == True:
            playing_sound_repeatedly()




