from app.menu import MenuItem
class Restaurant:
    restaurant_count=0

    def __init__(self,name,location):
        Restaurant.restaurant_count += 1
        self.restaurant_id=Restaurant.restaurant_count
        self.name = name
        self.location = location
        self.menu = {}
        self.orders = []

    def add_menu_item(self,item: MenuItem):
        self.menu[item.name] = item

    def view_menu(self):
        print(f"the menu for {self.name} is:")
        if not self.menu:
            print("No items in menu yet")
            return
        for item in self.menu.values():
            print(f"-{item.name}: rs{item.price} ")

    def receive_order(self,order):
        self.orders.append(order)
        print(f"\norder #{order.order_id} recieved by {self.name}: {order.item.name}")




