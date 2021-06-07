import datetime

from django.test import TestCase,Client
from django.urls import reverse, reverse_lazy
from ecomapp.models import User, Product, Category, Customer, Cart, CartProduct, ProductReviews
import json


class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.home = reverse('ecomapp:home')
        self.about = reverse('ecomapp:about')
        self.contact = reverse('ecomapp:contact')
        self.allproducts = reverse('ecomapp:allproducts')
        self.productdetail = reverse('ecomapp:productdetail',  args=["product-test"])
        self.addtocart = reverse('ecomapp:addtocart', args=[1])
        self.mycart = reverse('ecomapp:mycart')
        self.managecart = reverse('ecomapp:managecart', args=[1])
        self.emptycart =reverse('ecomapp:emptycart')
        self.chekout = reverse('ecomapp:checkout')
        self.cr = reverse('ecomapp:customerregistration')
        self.clo = reverse('ecomapp:customerlogout')
        self.cli = reverse('ecomapp:customerlogin')
        self.cp = reverse('ecomapp:customerprofile')
        self.cod = reverse('ecomapp:customerorderdetail', args=[7])
        self.s = reverse('ecomapp:search')
        self.pf = reverse('ecomapp:passworforgot')
        # self.al = reverse('ecomapp:adminlogin')
        # self.ah = reverse('ecomapp:adminhome')
        # self.aod = reverse('ecomapp:adminorderdetail', args=[7])
        # self.aol = reverse('ecomapp:adminorderlist')
        # self.aosc = reverse('ecomapp:adminorderstatuschange', args=[7])
        # self.apl = reverse('ecomapp:adminproductlist')
        # self.apc = reverse_lazy('ecomapp:adminproductcreate')
        self.u = User()
        self.u.save()
        self.testC = Category.objects.create(
            title = "TestCategory",
            slug = "test-category"
        )
        self.test = Product.objects.create(
            title='TEST',
            slug="product-test",
            category=self.testC,
            image='products/iphone.jpg',
            marked_price = 1500,
            selling_price = 1200,
            description = "A test",
            warranty = "Test",
            return_policy = "Test"
        )
        self.Customer = Customer.objects.create(
            user = self.u,
            full_name = "Test",
            address = "test address",
        )
        self.testCart = Cart.objects.create(
            customer= self.Customer,
            total = 10000
                         )
        self.testCartProduct = CartProduct.objects.create(
            cart = self.testCart,
            product = self.test,
            rate = 10000,
            quantity = 10,
            subtotal = 9000
                         )

    def test_home_GET(self):
        response = self.client.get(self.home)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_about_GET(self):
        response = self.client.get(self.about)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "about.html")

    def test_contact_GET(self):
        response = self.client.get(self.contact)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "contactus.html")

    def test_allproducts_GET(self):
        response = self.client.get(self.allproducts)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "allproducts.html")

    def test_productdetail_GET(self):
        response = self.client.get(self.productdetail)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "productdetail.html")

    def test_addtocart_GET(self):
        response = self.client.get(self.addtocart)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "addtocart.html")

    def test_mycart_GET(self):
        response = self.client.get(self.mycart)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "mycart.html")

    def test_managecart_GET(self):
        response = self.client.get(self.managecart)

        self.assertEquals(response.status_code, 302)

    def test_emptycart_GET(self):
        response = self.client.get(self.emptycart)

        self.assertEquals(response.status_code, 302)

    def test_chekout_GET(self):
        response = self.client.get(self.chekout)

        self.assertEquals(response.status_code, 302)

    def test_cr_GET(self):
        response = self.client.get(self.cr)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "customerregistration.html")

    def test_clo_GET(self):
        response = self.client.get(self.clo)

        self.assertEquals(response.status_code, 302)

    def test_cli_GET(self):
        response = self.client.get(self.cli)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "customerlogin.html")

    def test_cp_GET(self):
        response = self.client.get(self.cp)

        self.assertEquals(response.status_code, 302)

    def test_cod_GET(self):
        response = self.client.get(self.cod)

        self.assertEquals(response.status_code, 302)

    def test_s_GET(self):
        response = self.client.get(self.s, {"keyword" : "car"})

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "search.html")

    def test_pf_GET(self):
        response = self.client.get(self.pf)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "forgotpassword.html")

    # def test_al_GET(self):
    #     response = self.client.get(self.al)
    #
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, "adminlogin.html")
    #
    # def test_ah_GET(self):
    #     response = self.client.get(self.ah)
    #
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, "adminhome.html")
    #
    # def test_aod_GET(self):
    #     response = self.client.get(self.aod)
    #
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, "adminorderdetail.html")
    #
    # def test_aol_GET(self):
    #     response = self.client.get(self.aol)
    #
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, "adminorderlist.html")
    #
    # def test_aosc_GET(self):
    #     response = self.client.get(self.aosc)
    #
    #     self.assertEquals(response.status_code, 302)
    #
    # def test_apl_GET(self):
    #     response = self.client.get(self.apl)
    #
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, "adminproductlist.html")
    #
    # def test_apc_GET(self):
    #     response = self.client.get(self.apc)
    #
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, "adminproductlist.html")
