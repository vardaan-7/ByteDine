import pandas as pd
import os
from app.order import Order

class User:
    user_count = 0

    def __init__(self, name):
        User.user_count += 1
        self.user_id = User.user_count
        self.name = name
        self.order_history = []
        self.save_to_excel()  

    def save_to_excel(self):
        data = {
            "User ID": [self.user_id],
            "Name": [self.name]
        }

        df = pd.DataFrame(data)
        file_path = "users.xlsx"

        if os.path.exists(file_path):
            existing_df = pd.read_excel(file_path)
            updated_df = pd.concat([existing_df, df], ignore_index=True)
            updated_df.to_excel(file_path, index=False)
        else:
            df.to_excel(file_path, index=False)

    def place_order(self, restaurant, item_name):
        if item_name in restaurant.menu:
            item = restaurant.menu[item_name]
            order = Order(self, restaurant, item)
            self.order_history.append(order)
            restaurant.receive_order(order)
            print(f"{self.name} placed an order for {item.name}")
            return order
        else:
            print(f"{item_name} not found in {restaurant.name}'s menu.")
            return None

    def view_order_history(self):
        print(f"\nOrder history for {self.name}:")
        for order in self.order_history:
            print(f"-> {order.item.name} from {order.restaurant.name}")
