from rest_framework.test import APITestCase


class TestAmenities(APITestCase):
    def test_two_plus_two(self):  # self는 APITestCase를 가리킴.
        self.assertEqual(2 + 2, 4, "The math is wrong.")
