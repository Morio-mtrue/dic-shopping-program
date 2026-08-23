import pytest

from shipping_app.shipping import ExpressShipping, ShippingMethod, StandardShipping


def test_shipping_classes_use_inheritance():
    assert issubclass(StandardShipping, ShippingMethod)
    assert issubclass(ExpressShipping, ShippingMethod)


@pytest.mark.parametrize(
    ("shipping_method", "name", "fee", "guide"),
    [
        (StandardShipping(), "標準配送", 500, "2〜4日でお届け"),
        (ExpressShipping(), "速達配送", 1300, "翌日お届け"),
    ],
)
def test_shipping_methods_return_each_result(shipping_method, name, fee, guide):
    assert shipping_method.name == name
    assert shipping_method.fee() == fee
    assert shipping_method.delivery_guide() == guide
