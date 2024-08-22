import unittest
from ..limit_order_agent import LimitOrderAgent

class LimitOrderAgentTest(unittest.TestCase):

    def setUp(self):
        self.order_agent = LimitOrderAgent()

    def test_something(self):
        # To test buy functionality
        self.agent.add_order(True, 'IBM', 1000, 100)
        self.assertEqual(len(self.agent.orders), 1)
        self.assertEqual(self.agent.orders[0]['action'], True)
        self.assertEqual(self.agent.orders[0]['product_id'], 'IBM')
        self.assertEqual(self.agent.orders[0]['amount'], 1000)
        self.assertEqual(self.agent.orders[0]['limit'], 100)





