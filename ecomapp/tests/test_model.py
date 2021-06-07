from django.test import TestCase
from ecomapp.models import User, Product, Category, Customer, Cart, CartProduct, ProductReviews, Order, ProductImage


class TestView(TestCase):
    def setUp(self):
        u = User()
        u.save()
        self.testC = Category.objects.create(
            title="TestCategory",
            slug="test-category"
        )
        self.test = Product.objects.create(
            title='TEST',
            slug="product-test",
            category=self.testC,
            image='products/iphone.jpg',
            marked_price=1500,
            selling_price=1200,
            description="A test",
            warranty="Test",
            return_policy="Test"
        )
        self.Customer = Customer.objects.create(
            user=u,
            full_name="Test",
            address="test address",
        )
        self.testCart = Cart.objects.create(
            customer=self.Customer,
            total=10000
        )
        self.testCartProduct = CartProduct.objects.create(
            cart=self.testCart,
            product=self.test,
            rate=10000,
            quantity=10,
            subtotal=9000
        )

        self.testReview = ProductReviews.objects.create(
            product = self.test,
            user = u,
            content = "test",
            stars = 4,
        )

        self.testOrder = Order.objects.create(
            cart = self.testCart,
            ordered_by = "ME",
            shipping_address = "TEST-address",
            mobile = "5645645",
            email = "afasfsa@sfas.asd",
            subtotal = 5,
            discount = 5,
            total = 10,
            order_status = "test-status"
        )

        self.testImage = ProductImage.objects.create(
            product = self.test,
            image = "products/images/apple-watch.jpeg"
        )

    def test_Category(self):
        self.assertEquals(self.testC.slug, 'test-category')

    def test_Product(self):
        self.assertEquals(self.test.slug, 'product-test')
        self.assertEquals(self.test.get_rating(), 4)
        self.assertEquals(self.test.number_of_ratings(), 1)

    def test_Customer(self):
        self.assertEquals(self.Customer.full_name, 'Test')

    def test_Cart(self):
        self.assertEquals(self.testCart.total, 10000)

    def test_CartProduct(self):
        self.assertEquals(self.testCartProduct.rate, 10000)

    def test_ProductReviews(self):
        self.assertEquals(self.testReview.stars, 4)
        self.assertEquals(self.testReview.get_user_name(), "Test")

    def test_Order(self):
        self.assertEquals(self.testOrder.ordered_by, 'ME')

    def test_ProductImage(self):
        self.assertEquals(self.testImage.image, "products/images/apple-watch.jpeg")