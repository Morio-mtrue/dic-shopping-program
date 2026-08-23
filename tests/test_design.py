import ast
from pathlib import Path

from shipping_app.order import Order
from shipping_app.shipping import ExpressShipping, ShippingMethod, StandardShipping

ROOT = Path(__file__).resolve().parents[1]


def class_node(path, class_name):
    tree = ast.parse(path.read_text(encoding="utf-8"))
    return next(
        node
        for node in tree.body
        if isinstance(node, ast.ClassDef) and node.name == class_name
    )


def method_node(node, method_name):
    return next(
        child
        for child in node.body
        if isinstance(child, ast.FunctionDef) and child.name == method_name
    )


def calls_super_method(node, method_name):
    for child in ast.walk(node):
        if not isinstance(child, ast.Call) or not isinstance(child.func, ast.Attribute):
            continue
        receiver = child.func.value
        if (
            child.func.attr == method_name
            and isinstance(receiver, ast.Call)
            and isinstance(receiver.func, ast.Name)
            and receiver.func.id == "super"
        ):
            return True
    return False


def test_child_classes_call_parent_implementation_with_super():
    path = ROOT / "shipping_app" / "shipping.py"
    standard = class_node(path, "StandardShipping")
    express = class_node(path, "ExpressShipping")

    assert calls_super_method(method_node(standard, "__init__"), "__init__")
    assert calls_super_method(method_node(express, "__init__"), "__init__")
    assert calls_super_method(method_node(express, "fee"), "fee")


def test_order_uses_composition_without_type_conditionals():
    path = ROOT / "shipping_app" / "order.py"
    order_node = class_node(path, "Order")

    forbidden_nodes = (ast.If, ast.IfExp, ast.Match)
    forbidden_calls = {"isinstance", "issubclass", "type"}

    assert not any(isinstance(node, forbidden_nodes) for node in ast.walk(order_node))
    assert not any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id in forbidden_calls
        for node in ast.walk(order_node)
    )


def test_different_shipping_objects_share_the_same_operations():
    shipping_methods = [StandardShipping(), ExpressShipping()]

    totals = [Order(12000, method).total() for method in shipping_methods]

    assert totals == [12500, 13300]
    assert all(isinstance(method, ShippingMethod) for method in shipping_methods)
