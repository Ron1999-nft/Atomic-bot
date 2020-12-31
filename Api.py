import requests
import json

class Api:
    def __init__(self, price : int, link : str):
        self.link = link
        self.price = price
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



