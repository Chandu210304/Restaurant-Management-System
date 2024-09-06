import unittest
from orders import Order

class TestRestaurantManagementSystem(unittest.TestCase):
    def test_order_total(self):
        items = [{'name': 'Pizza', 'price': 10}, {'name': 'Pasta', 'price': 12}]
        order = Order(1, items)
        self.assertEqual(order.calculate_total(), 22)

if __name__ == "__main__":
    unittest.main()
