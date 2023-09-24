
class Order:
    order_id: str = ""
    user_id: str = ""
    username: str = ""
    price: float = 0.0
    time: str = ""
    destination: str = ""
    status: bool = False

    def __int__(self, order_id, user_id, username, price, time, destination, status):
        self.order_id = order_id
        self.user_id = user_id
        self.username = username
        self.price = price
        self.time = time
        self.destination = destination
        self.status = status

    # Instance method to print all information about the order
    def info(self):
        print("Order ID:", self.order_id, "\nUser ID:", self.user_id, "\nUsername: ", self.username, "\nPrice: ",
              self.price, "\nTime: ", self.time, "\nDestination ", self.destination, "\nStatus: ", self.status)

