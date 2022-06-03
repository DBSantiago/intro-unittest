import unittest

from product import Product


class TestShoppingCart(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("Class method setUpClass is executed once before all tests.")

    @classmethod
    def tearDownClass(cls) -> None:
        print("Class method tearDownClass is executed once after all tests.")

    def setUp(self) -> None:
        self.smartphone = Product("IPhone", 500.00)
        print("Method setUp is executed before each test.")

    def tearDown(self) -> None:
        print("Method tearDown is executed before each test.")

    def test_product_object(self) -> None:
        name = "Apple"
        price = 1.70

        product = Product(name, price)

        self.assertEqual(product.name, name)
        self.assertEqual(product.price, price)

    def test_product_name(self) -> None:
        self.assertEqual(self.smartphone.name, "IPhone")

    def test_product_price(self) -> None:
        self.assertEqual(self.smartphone.price, 500.00)


if __name__ == "__main__":
    unittest.main()
