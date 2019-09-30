from django.test import TestCase
from .models import Content, Footer, Header
# Create your tests here.

class HeaderTest(TestCase):
    """Test Header class module"""

    def setUp(self):
        Header.objects.create(email_from='dummymail@gmail.com', email_title='Hello there')
