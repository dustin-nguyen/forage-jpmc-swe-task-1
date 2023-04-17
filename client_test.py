import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            stock, bid_price, ask_price, price = (quote['stock'], float(quote['top_bid']['price']), float(
                quote['top_ask']['price']), (float(quote['top_bid']['price']) + float(quote['top_ask']['price'])) / 2)
            self.assertEqual(getDataPoint(quote),
                             (stock, bid_price, ask_price, price))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            stock, bid_price, ask_price, price = (quote['stock'], float(quote['top_bid']['price']), float(
                quote['top_ask']['price']), (float(quote['top_bid']['price']) + float(quote['top_ask']['price'])) / 2)
            self.assertEqual(getDataPoint(quote),
                             (stock, bid_price, ask_price, price))

    """ ------------ Add more unit tests ------------ """

    def test_getRatio_calculateRatio(self):
        stock_ABC = {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                     'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
        stock_DEF = {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
                     'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        """ ------------ Add the assertion below ------------ """

        stock_name_abc, bid_price_abc, ask_price_abc, price_abc = getDataPoint(
            stock_ABC)
        stock_name_def, bid_price_def, ask_price_def, price_def = getDataPoint(
            stock_DEF)
        self.assertEqual(getRatio(price_abc, price_def),
                         (price_abc/price_def))

    def test_getRatio_calculateRatioDivideZero(self):
        stock_ABC = {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                     'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
        stock_DEF = {'top_ask': {'price': 0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
                     'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        """ ------------ Add the assertion below ------------ """

        stock_name_abc, bid_price_abc, ask_price_abc, price_abc = getDataPoint(
            stock_ABC)
        stock_name_def, bid_price_def, ask_price_def, price_def = getDataPoint(
            stock_DEF)
        self.assertIsNone(getRatio(price_abc, price_def))

    def test_getRatio_calculateRatioZeroDivide(self):
        stock_ABC = {'top_ask': {'price': 0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                     'top_bid': {'price': 0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
        stock_DEF = {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
                     'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        """ ------------ Add the assertion below ------------ """

        stock_name_abc, bid_price_abc, ask_price_abc, price_abc = getDataPoint(
            stock_ABC)
        stock_name_def, bid_price_def, ask_price_def, price_def = getDataPoint(
            stock_DEF)
        self.assertEqual(getRatio(price_abc, price_def),
                         (price_abc/price_def))


if __name__ == '__main__':
    unittest.main()
