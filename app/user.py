class User:
    user_count=0
    def __init__(self,name):
        User.user_count +=1
        self.user_id = User.user_count
        self.name=name
        self.order_history = []

    def place_order(self,order):
        self.order_history.append(order)
        print(f"{self.name} placed an order. The order is:{order}")
        
    def view_order_history(self):
        print(f"order history for {self.name}:")
        for order in self.order_history:
            print(f"->{order}")

user1 = User("Vardaan")
user1.place_order("pizza")
user1.place_order("burger")
user1.view_order_history()