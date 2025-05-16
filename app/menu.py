class MenuItem:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def __str__(self):
        print(f"{self.name} - rs{self.price}")