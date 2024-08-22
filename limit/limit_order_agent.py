from trading_framework.execution_client import ExecutionClient
from trading_framework.price_listener import PriceListener


class LimitOrderAgent(PriceListener):

    def __init__(self, execution_client: ExecutionClient) -> None:
        """
        :param execution_client: can be used to buy or sell - see ExecutionClient protocol definition
        """
        super().__init__()
        # set limit of share price to 100 and share will get buy price <= 100 and sell > 100
        self.limit = None
        self.stocks = []
        self.amount = None

    def on_price_tick(self, product_id: str, price: float):
        # see PriceListener protocol and readme file
        # To buy 1000 shares of IBM when price <= 100
        self.limit = 100
        self.amount = 1000
        self.add_order(True, product_id, self.amount, price)

        # To sell 1000 shares of IBM when price > 100
        # self.amount = 1000
        # self.add_order(False, product_id, self.amount, price)

    def add_order(self, buy_flag: bool, product_id:str, amount:float, price:float):
        order = {'product_id': product_id, 'amount': amount, 'price': price, 'buy': buy_flag, 'sell': not buy_flag}
        if buy_flag and price <= self.limit:
            self.buy(product_id, amount)
        elif not buy_flag and price > self.limit:
            self.sell(product_id, amount)
        # I have created self.stocks to maintain order data
        self.stocks.append(order)



