from shipping_app.order import Order
from shipping_app.shipping import ExpressShipping, StandardShipping


def main():
    shipping_methods = [StandardShipping(), ExpressShipping()]

    for shipping_method in shipping_methods:
        order = Order(12000, shipping_method)
        print(order.summary())


if __name__ == "__main__":
    main()
