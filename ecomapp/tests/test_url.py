from django.test import SimpleTestCase
from django.urls import resolve, reverse
from ecomapp.views import HomeView, AboutView, ContactView, AllProductsView, ProductDetailView, AddToCartView, \
    MyCartView, ManageCartView, EmptyCartView, CheckoutView, CustomerRegistrationView,  \
    CustomerLogoutView, CustomerLoginView, CustomerProfileView, CustomerOrderDetailView, SearchView, \
    PasswordForgotView, PasswordResetView, AdminLoginView, AdminHomeView, AdminOrderDetailView, AdminOrderListView, \
    AdminOrderStatuChangeView, AdminProductListView, AdminProductCreateView


class TestUrls(SimpleTestCase):
    def test_home_url(self):
        url = reverse('ecomapp:home')
        self.assertEquals(resolve(url).func.view_class, HomeView)

    def test_about_url(self):
        url = reverse('ecomapp:about')
        self.assertEquals(resolve(url).func.view_class, AboutView)

    def test_contact_url(self):
        url = reverse('ecomapp:contact')
        self.assertEquals(resolve(url).func.view_class, ContactView)

    def test_allproducts_url(self):
        url = reverse('ecomapp:allproducts')
        self.assertEquals(resolve(url).func.view_class, AllProductsView)

    def test_productdetail_url(self):
        url = reverse('ecomapp:productdetail', args=['rolex-watch'])
        self.assertEquals(resolve(url).func.view_class, ProductDetailView)

    def test_addtocart_url(self):
        url = reverse('ecomapp:addtocart', args=[12])
        self.assertEquals(resolve(url).func.view_class, AddToCartView)

    def test_mycart_url(self):
        url = reverse('ecomapp:mycart')
        self.assertEquals(resolve(url).func.view_class, MyCartView)

    def test_managecart_url(self):
        url = reverse('ecomapp:managecart', args=[30])
        self.assertEquals(resolve(url).func.view_class, ManageCartView)

    def test_emptycart_url(self):
        url = reverse('ecomapp:emptycart')
        self.assertEquals(resolve(url).func.view_class, EmptyCartView)

    def test_checkout_url(self):
        url = reverse('ecomapp:checkout')
        self.assertEquals(resolve(url).func.view_class, CheckoutView)

    def test_customerregistration_url(self):
        url = reverse('ecomapp:customerregistration')
        self.assertEquals(resolve(url).func.view_class, CustomerRegistrationView)

    def test_customerlogout_url(self):
        url = reverse('ecomapp:customerlogout')
        self.assertEquals(resolve(url).func.view_class, CustomerLogoutView)

    def test_customerlogin_url(self):
        url = reverse('ecomapp:customerlogin')
        self.assertEquals(resolve(url).func.view_class, CustomerLoginView)

    def test_customerprofile_url(self):
        url = reverse('ecomapp:customerprofile')
        self.assertEquals(resolve(url).func.view_class, CustomerProfileView)

    def test_customerorderdetail_url(self):
        url = reverse('ecomapp:customerorderdetail', args=[7])
        self.assertEquals(resolve(url).func.view_class, CustomerOrderDetailView)

    def test_search_url(self):
        url = reverse('ecomapp:search')
        self.assertEquals(resolve(url).func.view_class, SearchView)

    def test_passworforgot_url(self):
        url = reverse('ecomapp:passworforgot')
        self.assertEquals(resolve(url).func.view_class, PasswordForgotView)

    # def test_passwordreset_url(self):
    #     url = reverse('ecomapp:passwordreset', args=["customerone@gmail.com"])
    #     self.assertEquals(resolve(url).func.view_class, PasswordResetView)

    def test_adminlogin_url(self):
        url = reverse('ecomapp:adminlogin')
        self.assertEquals(resolve(url).func.view_class, AdminLoginView)

    def test_adminhome_url(self):
        url = reverse('ecomapp:adminhome')
        self.assertEquals(resolve(url).func.view_class, AdminHomeView)

    def test_adminorderdetail_url(self):
        url = reverse('ecomapp:adminorderdetail', args=[7])
        self.assertEquals(resolve(url).func.view_class, AdminOrderDetailView)

    def test_adminorderlist_url(self):
        url = reverse('ecomapp:adminorderlist')
        self.assertEquals(resolve(url).func.view_class, AdminOrderListView)

    def test_adminorderstatuschange_url(self):
        url = reverse('ecomapp:adminorderstatuschange', args=[7])
        self.assertEquals(resolve(url).func.view_class, AdminOrderStatuChangeView)

    def test_adminproductlist_url(self):
        url = reverse('ecomapp:adminproductlist')
        self.assertEquals(resolve(url).func.view_class, AdminProductListView)

    def test_adminproductcreate_url(self):
        url = reverse('ecomapp:adminproductcreate')
        self.assertEquals(resolve(url).func.view_class, AdminProductCreateView)