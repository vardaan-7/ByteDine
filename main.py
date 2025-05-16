from app.user import User
from app.restaurant import Restaurant
from app.menu import MenuItem
from app.deliveryboy import DeliveryBoy
from app.order import Order

r1 = Restaurant("Pizza Palace", "Noida")
r1.add_menu_item(MenuItem("Pepperoni Pizza", 299))
r1.add_menu_item(MenuItem("Veggie Pizza", 249))

# Create users
u1 = User("Riya")
d1 = DeliveryBoy("Aman")

r1.view_menu()
order = u1.place_order(r1,"Veggie Pizza")

if order:
    d1.assign_order(order)

u1.view_order_history()