class ProductDiscountError(Exception):
    pass


class Product:
    def __init__(self, name: str, price: float, discount: float = 0.0) -> None:
        if discount > price:
            raise ProductDiscountError("Discount can't be higher than product price.")

        self.name = name
        self.price = price
        self.discount = discount
