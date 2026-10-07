from typing import TypedDict
 
 
class OrderItem(TypedDict):
    price: float
    qty: int
 
 
class Order(TypedDict):
    items: list[OrderItem]
    member: bool
    country: str
 
 
def calculate_items_subtotal(order: Order) -> float:
    subtotal = 0.0
    for item in order["items"]:
        price = item["price"]
        quantity = item["qty"]
        if price <= 0 or quantity <= 0:
            continue
        subtotal += price * quantity
    return subtotal
 
 
def calculate_member_discount(order: Order, subtotal: float) -> float:
    if not order["member"]:
        return 0.0
    if subtotal > 100:
        return subtotal * 0.2
    if subtotal > 50:
        return subtotal * 0.1
    return 0.0
 
 
def calculate_shipping_cost(order: Order) -> float:
    if order["country"] == "PK":
        return 5.0
    if order["country"] == "US":
        return 15.0
    return 25.0
 
 
def calculate_order_total(order: Order) -> float:
    subtotal = calculate_items_subtotal(order)
    discount = calculate_member_discount(order, subtotal)
    shipping = calculate_shipping_cost(order)
    return subtotal - discount + shipping
