import pytest

from shipping_app.order import Order
from shipping_app.shipping import ExpressShipping, StandardShipping


@pytest.mark.parametrize(
    ("shipping_method", "expected_total", "expected_summary"),
    [
        (
            StandardShipping(),
            12500,
            "標準配送 | 配送料: 500円 | 支払合計: 12,500円 | 2〜4日でお届け",
        ),
        (
            ExpressShipping(),
            13300,
            "速達配送 | 配送料: 1,300円 | 支払合計: 13,300円 | 翌日お届け",
        ),
    ],
)
def test_order_uses_shipping_method(shipping_method, expected_total, expected_summary):
    order = Order(12000, shipping_method)

    assert order.subtotal == 12000
    assert order.shipping_method is shipping_method
    assert order.total() == expected_total
    assert order.summary() == expected_summary
