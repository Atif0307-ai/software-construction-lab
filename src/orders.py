from typing import TypedDict


class OrderItem(TypedDict):
    price: float
    qty: int


class Order(TypedDict):
    items: list[OrderItem]
    member: bool
    country: str


def calculate_items_subtotal(items: list[OrderItem]) -> float:
    subtotal = 0.0

    for item in items:
        price = item["price"]
        quantity = item["qty"]

        if price <= 0:
            continue
        if quantity <= 0:
            continue

        subtotal += price * quantity

    return subtotal


def calculate_member_discount(subtotal: float, is_member: bool) -> float:
    if not is_member:
        return 0.0
    if subtotal > 100:
        return subtotal * 0.2
    if subtotal > 50:
        return subtotal * 0.1

    return 0.0


def calculate_shipping_cost(country: str) -> float:
    if country == "PK":
        return 5.0
    if country == "US":
        return 15.0

    return 25.0


def calculate_order_total(order: Order) -> float:
    subtotal = calculate_items_subtotal(order["items"])
    discount = calculate_member_discount(subtotal, order["member"])
    shipping_cost = calculate_shipping_cost(order["country"])

    return subtotal - discount + shipping_cost