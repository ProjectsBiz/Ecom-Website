from django.test import TestCase
from ecomapp.forms import PasswordForgotForm, CustomerRegistrationForm, ProductForm
from ecomapp.models import User, Product, Category, Customer, Cart, CartProduct, ProductReviews, Order, ProductImage


class TestForms(TestCase):
    def setUp(self):
        u = User()
        u.save()
        self.category = Category.objects.create(
            title="TestCategory",
            slug="test-category"
        )
        self.test = Product.objects.create(
            title='TEST',
            slug="product-test",
            category=self.category,
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
            product=self.test,
            user=u,
            content="test",
            stars=4,
        )

        self.testOrder = Order.objects.create(
            cart=self.testCart,
            ordered_by="ME",
            shipping_address="TEST-address",
            mobile="5645645",
            email="afasfsa@sfas.asd",
            subtotal=5,
            discount=5,
            total=10,
            order_status="test-status"
        )

        self.image = ProductImage.objects.create(
            product=self.test,
            image="products/images/apple-watch.jpeg"
        )

    def test_p_form(self):
        form = ProductForm(data={
            "title": "test",
            "slug": "test",
            "category": self.category,
            "image": "products/images/apple-watch.jpeg",
            "marked_price": 100,
            "selling_price": 50,
            "description": "test",
            "warranty": "test",
            "return_policy": "test"})

        self.assertFalse(form.is_valid())

    def test_f_form(self):
        form = PasswordForgotForm(data={
            'email' : 'zakir@mail.com'
        })

        self.assertFalse(form.is_valid())

    def test_cr_form(self):
        form = CustomerRegistrationForm(data={
            'username' : 'test',
            'password' : 'test',
            'email' :  'afasfa@fada.ada',
            "full_name": "Test-name",
            "address": "Test"
        })

        self.assertTrue(form.is_valid())