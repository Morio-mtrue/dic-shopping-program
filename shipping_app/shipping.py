class ShippingMethod:
    """配送方法の共通部分を扱うclass。"""

    def __init__(self, name, base_fee):
        self.name = name
        self.base_fee = base_fee

    def fee(self):
        return self.base_fee

    def delivery_guide(self):
        return "到着日未定"


class StandardShipping(ShippingMethod):
    """標準配送を扱うclass。"""

    def __init__(self):
        # TODO: super()を使い、配送方法名と基本料金500円を初期化する
        pass

    def delivery_guide(self):
        # TODO: 標準配送の案内を返す
        pass


class ExpressShipping(ShippingMethod):
    """速達配送を扱うclass。"""

    def __init__(self):
        # TODO: super()を使い、配送方法名と基本料金500円を初期化する
        pass

    def fee(self):
        # TODO: super().fee()の結果へ速達料金800円を加算して返す
        pass

    def delivery_guide(self):
        # TODO: 速達配送の案内を返す
        pass
