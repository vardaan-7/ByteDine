class DeliveryBoy:
    delivery_boy_count = 0

    def __init__(self, name):
        DeliveryBoy.delivery_boy_count += 1
        self.delivery_boy_id = DeliveryBoy.delivery_boy_count
        self.name = name
        self.available = True
        self.current_order = None

    def assign_order(self, order):
        if self.available:
            self.current_order = order
            self.available = False
            print(f"{self.name} assigned to deliver: {order}")
        else:
            print(f"{self.name} is currently busy.")

    def complete_order(self):
        if not self.available:
            print(f"{self.name} has completed the order: {self.current_order}")
            self.current_order = None
            self.available = True
        else:
            print(f"{self.name} has no current order.")
