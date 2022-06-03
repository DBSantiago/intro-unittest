import unittest

from product import Product, ProductDiscountError
from shopping_cart import ShoppingCart


class TestShoppingCart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Class method setUpClass is executed once before all tests.")

    @classmethod
    def tearDownClass(cls):
        print("Class method tearDownClass is executed once after all tests.")

    def setUp(self):
        self.smartphone = Product("IPhone", 500.00)
        print("Method setUp is executed before each test.")

        self.shopping_cart_1 = ShoppingCart()
        self.shopping_cart_2 = ShoppingCart()
        self.shopping_cart_2.add_product(self.smartphone)

    def tearDown(self):
        print("Method tearDown is executed before each test.")

    def test_product_object(self):
        name = "Apple"
        price = 1.70

        product = Product(name, price)

        self.assertEqual(product.name, name)
        self.assertEqual(product.price, price)

    def test_product_name(self):
        self.assertEqual(self.smartphone.name, "IPhone")

    def test_product_price(self):
        self.assertEqual(self.smartphone.price, 500.00)

    def test_shopping_cart_empty(self):
        self.assertTrue(self.shopping_cart_1.empty(), "Shopping cart is not empty.")

    def test_shopping_cart_has_product(self):
        self.assertTrue(self.shopping_cart_2.has_products())
        self.assertFalse(self.shopping_cart_2.empty())

    def test_product_in_shopping_cart(self):
        self.assertIn(self.smartphone, self.shopping_cart_2.products)

        product = Product("Notebook", 20.0)
        self.shopping_cart_2.add_product(product)

        self.assertIn(product, self.shopping_cart_2.products)

    def test_product_not_in_shopping_cart(self):
        self.shopping_cart_2.remove_product(self.smartphone)

        self.assertNotIn(self.smartphone, self.shopping_cart_2.products)

    def test_product_discount_error(self):
        with self.assertRaises(ProductDiscountError):
            Product("Product Example", 10.0, discount=11.0)

    def test_total_shopping_cart(self):
        self.shopping_cart_1.add_product(Product("Pen", 5.0))
        self.shopping_cart_1.add_product(Product("Camera", 320.0, discount=50.0))

        self.assertGreater(self.shopping_cart_1.total, 0)
        self.assertGreaterEqual(self.shopping_cart_1.total, 0)
        self.assertLessEqual(self.shopping_cart_1.total, 99999)
        self.assertEqual(self.shopping_cart_1.total, 275.0)

    def test_total_empty_shopping_cart(self):
        self.assertEqual(self.shopping_cart_1.total, 0)

    @unittest.skip("This test doesn't meet the requirements")
    def test_skip_example(self):
        self.assertEqual(1, 1)

    # skipIf -> skips if condition == True
    # skipUnless -> skips if condition == False
    @unittest.skipIf(True, "This test is skipped because condition is True.")
    def test_skip_if(self):
        self.assertEqual(1, 1)

    @unittest.skipUnless(False, "This test is skipped because condition is False.")
    def test_skip_unless(self):
        self.assertEqual(1, 1)


if __name__ == "__main__":
    unittest.main()
