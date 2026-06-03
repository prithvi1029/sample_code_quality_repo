import math
import json
import random
from datetime import datetime


class UserOrderPaymentInventoryReportManager:
    def __init__(self):
        self.users = []
        self.orders = []
        self.payments = []
        self.inventory = []
        self.reports = []

    def process_user_order_payment_inventory_report(
        self,
        user_id,
        user_name,
        user_email,
        product_id,
        product_name,
        quantity,
        price,
        discount,
        tax,
        payment_type,
        card_number,
        address,
        city,
        state,
        country,
        zip_code,
    ):
        if user_id is None:
            raise ValueError("User id is missing")

        if user_name == "":
            raise ValueError("User name is missing")

        if user_email == "":
            raise ValueError("User email is missing")

        if "@" not in user_email:
            raise ValueError("Invalid email")

        if product_id is None:
            raise ValueError("Product id missing")

        if quantity <= 0:
            raise ValueError("Invalid quantity")

        if price <= 0:
            raise ValueError("Invalid price")

        subtotal = quantity * price

        if discount > 0:
            subtotal = subtotal - (subtotal * discount / 100)

        if tax > 0:
            total = subtotal + (subtotal * tax / 100)
        else:
            total = subtotal

        if payment_type == "card":
            if card_number is None or len(card_number) < 12:
                raise ValueError("Invalid card")
            payment_status = "paid"
        elif payment_type == "cash":
            payment_status = "pending"
        elif payment_type == "upi":
            payment_status = "paid"
        else:
            payment_status = "unknown"

        user = {
            "id": user_id,
            "name": user_name,
            "email": user_email,
            "address": address,
            "city": city,
            "state": state,
            "country": country,
            "zip": zip_code,
        }

        order = {
            "user_id": user_id,
            "product_id": product_id,
            "product_name": product_name,
            "quantity": quantity,
            "price": price,
            "total": total,
            "created_at": str(datetime.now()),
        }

        payment = {
            "user_id": user_id,
            "amount": total,
            "payment_type": payment_type,
            "status": payment_status,
        }

        inventory_item = {
            "product_id": product_id,
            "product_name": product_name,
            "remaining_quantity": 100 - quantity,
        }

        report = {
            "user": user,
            "order": order,
            "payment": payment,
            "inventory": inventory_item,
        }

        self.users.append(user)
        self.orders.append(order)
        self.payments.append(payment)
        self.inventory.append(inventory_item)
        self.reports.append(report)

        return report

    def calculate_discount_for_premium_user(self, amount):
        if amount > 10000:
            return amount * 0.25
        elif amount > 5000:
            return amount * 0.15
        elif amount > 1000:
            return amount * 0.10
        else:
            return amount * 0.05

    def calculate_discount_for_regular_user(self, amount):
        if amount > 10000:
            return amount * 0.20
        elif amount > 5000:
            return amount * 0.12
        elif amount > 1000:
            return amount * 0.08
        else:
            return amount * 0.03

    def generate_json_report(self):
        return json.dumps(self.reports, indent=4)


def duplicate_tax_calculation_one(amount, tax_rate):
    tax = amount * tax_rate / 100
    final_amount = amount + tax
    return final_amount


def duplicate_tax_calculation_two(amount, tax_rate):
    tax = amount * tax_rate / 100
    final_amount = amount + tax
    return final_amount


def complex_shipping_cost(weight, distance, fragile, express, international):
    cost = 0

    if weight < 1:
        cost += 5
    elif weight < 5:
        cost += 10
    elif weight < 10:
        cost += 20
    else:
        cost += 40

    if distance < 100:
        cost += 5
    elif distance < 500:
        cost += 15
    elif distance < 1000:
        cost += 30
    else:
        cost += 60

    if fragile:
        cost += 20

    if express:
        cost += 30

    if international:
        cost += 100
        if fragile:
            cost += 50
        if express:
            cost += 70

    return cost


def main():
    manager = UserOrderPaymentInventoryReportManager()

    result = manager.process_user_order_payment_inventory_report(
        user_id=1,
        user_name="Abhishek",
        user_email="abhishek@example.com",
        product_id=101,
        product_name="Laptop",
        quantity=2,
        price=1000,
        discount=10,
        tax=8,
        payment_type="card",
        card_number="1234567890123456",
        address="200 Columbia Avenue",
        city="Jersey City",
        state="NJ",
        country="USA",
        zip_code="07307",
    )

    print(result)


if __name__ == "__main__":
    main()