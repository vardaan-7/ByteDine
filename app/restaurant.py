class Restaurant:
    restaurant_count=0

    def __init__(self,name,location):
        Restaurant.restaurant_count += 1
        self.restaurant_id=Restaurant.restaurant_count
        self.name = name
        self.location = location
        self.menu = {}
        self.orders = []

    def add_menu_item(self,item,price):
        self.menu[item]=price
        print(f"{item} added to {self.name}'s menu at price rs.{price}")

    def view_menu(self):
        print(f"the menu for {self.name} is:")
        for item,price in self.menu.items():
            print(f"-{item}: rs{price} ")

    def receive_order(self,order):
        self.orders.append(order)
        print(f"order recieved at {self.name}: {order}")




# res1 = Restaurant("Pizza Planet", "Delhi")

# # Add items to its menu
# res1.add_menu_item("Margherita", 250)
# res1.add_menu_item("Farmhouse", 350)

# # View menu
# res1.view_menu()

# # Receive an order
# res1.receive_order("2x Margherita")