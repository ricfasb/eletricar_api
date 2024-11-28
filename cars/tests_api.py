from rest_framework import status
from rest_framework.test import APITestCase

from .models import Car


class CarAPITest(APITestCase):
    def setUp(self):
        self.car = Car.objects.create(
            brand="Honda",
            model="Civic",
            year=2020,
            price=90000.00
        )
        self.car_data = {
            "brand": "Ford",
            "model": "Fiesta",
            "year": 2019,
            "price": 70000.00
        }
        self.url = "/api/cars/"

    def test_get_cars(self):
        """Testando a listagem"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_car(self):
        """Testando o post."""
        response = self.client.post(self.url, self.car_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Car.objects.count(), 2)

    def test_update_car(self):
        """Testando o update."""
        url = f"{self.url}{self.car.id}/"
        updated_data = {"brand": "Honda", "model": "Accord", "year": 2021, "price": 100000.00}
        response = self.client.put(url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.car.refresh_from_db()
        self.assertEqual(self.car.model, "Accord")

    def test_delete_car(self):
        """Testando o delete."""
        url = f"{self.url}{self.car.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Car.objects.count(), 0)
