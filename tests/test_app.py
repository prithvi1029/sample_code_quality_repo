import sys
from pathlib import Path
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))
from app import duplicate_tax_calculation_one, duplicate_tax_calculation_two, complex_shipping_cost, UserOrderPaymentInventoryReportManager

def test_duplicate_tax_calculation():
    """Execute test_duplicate_tax_calculation with validated inputs."""
    assert duplicate_tax_calculation_one(100, 10) == 110
    assert duplicate_tax_calculation_two(100, 10) == 110

def test_shipping_cost():
    """Execute test_shipping_cost with validated inputs."""
    assert complex_shipping_cost(2, 200, True, False, False) == 45

def test_order_processing():
    """Execute test_order_processing with validated inputs."""
    manager = UserOrderPaymentInventoryReportManager()
    result = manager.process_user_order_payment_inventory_report(user_id=1, user_name='Test User', user_email='test@example.com', product_id=101, product_name='Laptop', quantity=1, price=1000, discount=10, tax=10, payment_type='card', card_number='1234567890123456', address='Address', city='City', state='State', country='Country', zip_code='12345')
    assert result['payment']['status'] == 'paid'
    assert result['order']['total'] == 990
