from django.test import TestCase

from cars.models import Car



class CarModelTest(TestCase):
    def setUp(self):
        self.car = Car.objects.create(
            brand="Ford",
            model="Focus",
            year=2010,
            price=30000.00
        )

    def test_car_creation(self):
        self.assertEqual(self.car.brand, "Ford")
        self.assertEqual(self.car.model, "Focus")
        self.assertEqual(self.car.year, 2010)
        self.assertEqual(float(self.car.price), 30000.00)

    def test_car_string_representation(self):
        self.assertEqual(str(self.car), "Ford Focus (2010)")
