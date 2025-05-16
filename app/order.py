class Order:
    order_count = 0

    def __init__(self,user,restaurant,item):
        Order.order_count +=1
        self.order_id = Order.order_count
        self.user=user
        self.restaurant = restaurant
        self.item = item

    def __str__(self):
        return f"Order #{self.order_id} by {self.user.name} from {self.restaurant.name}"    