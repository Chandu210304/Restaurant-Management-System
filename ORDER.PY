class Order:
    def __init__(self, order_id, items):
        self.__order_id = order_id
        self.__items = items

    def calculate_total(self):
        return sum(item['price'] for item in self.__items)

class OrderManager:
    def __init__(self):
        self.orders = []

    def create_order(self, items):
        order_id = len(self.orders) + 1
        new_order = Order(order_id, items)
        self.orders.append(new_order)
        print(f"Order {order_id} created with total {new_order.calculate_total()}")

    def manage_orders(self):
        items = [{'name': 'Pizza', 'price': 10}, {'name': 'Pasta', 'price': 12}]
        self.create_order(items)
        # Add more order management logic here
