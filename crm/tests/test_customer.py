from django.test import TestCase
from crm.models import Customer


class TestCustomer(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.customer = Customer.objects.create(
            name='Yuri Teixeira',
            email='yuriteixeirac@proton.me'
        )
    

    def test_customer_creation(self):
        self.assertEqual(self.customer.name, 'Yuri Teixeira')
