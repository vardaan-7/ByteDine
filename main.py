from app.user import User
from app.restaurant import Restaurant
from app.menu import MenuItem
from app.deliveryboy import DeliveryBoy

users = []
restaurants = []
deliveryboys = []

r1 = Restaurant("Pizza Palace", "Noida")
r1.add_menu_item("Pepperoni Pizza", 299)
r1.add_menu_item("Veggie Pizza", 249)
restaurants.append(r1)

# Create users
u1 = User("Riya")
users.append(u1)

# Create delivery boys
d1 = DeliveryBoy("Aman")
deliveryboys.append(d1)
