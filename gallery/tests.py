from django.test import TestCase
from .models import Category, Image
from django.utils import timezone
from django.urls import reverse
from datetime import date

class ModelTests(TestCase):

    def setUp(self) -> None:
        category = Category.objects.create(name="Test Category")
        image = Image.objects.create(
            title="Test Image",
            image="test_image.jpg",
            created_date=date.today(),
            age_limit=18
        )
        image.categories.add(category)

    def test_image_addition(self):
        image = Image.objects.get(title='Test Image')
        category = Category.objects.get(name='Test Category')
        self.assertEqual(image.title, "Test Image")
        self.assertEqual(image.image, "test_image.jpg")
        self.assertEqual(image.age_limit, 18)
        self.assertEqual(image.categories.count(), 1)
        self.assertEqual(image.categories.first(), category)

