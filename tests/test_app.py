from app import (
    duplicate_tax_calculation_one,
    duplicate_tax_calculation_two,
    complex_shipping_cost,
    UserOrderPaymentInventoryReportManager,
)


def test_duplicate_tax_calculation():
    assert duplicate_tax_calculation_one(100, 10) == 110
    assert duplicate_tax_calculation_two(100, 10) == 110


def test_shipping_cost():
    assert complex_shipping_cost(2, 200, True, False, False) == 45


def test_order_processing():
    manager = UserOrderPaymentInventoryReportManager()

    result = manager.process_user_order_payment_inventory_report(
        user_id=1,
        user_name="Test User",
        user_email="test@example.com",
        product_id=101,
        product_name="Laptop",
        quantity=1,
        price=1000,
        discount=10,
        tax=10,
        payment_type="card",
        card_number="1234567890123456",
        address="Address",
        city="City",
        state="State",
        country="Country",
        zip_code="12345",
    )

    assert result["payment"]["status"] == "paid"
    assert result["order"]["total"] == 990