# django에 내장된 class가 아닌 DRF에 내장된 class를 사용
from rest_framework.test import APITestCase
from . import models


class TestAmenities(APITestCase):
    # 이후 같은 부분 반복과 수정을 줄이기 위해 class 변수로 지정
    NAME = "Amenity Test"
    DESC = "Amenity Des"

    # setUp method로 인해 Amenity가 test하자마자 생성 될 예정.
    def setUp(self):
        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    def test_all_amenities(self):  # self는 APITestCase를 가리킴.
        response = self.client.get("/api/v1/rooms/amenities/")
        data = response.json()

        # 로그인을 하지 않아도 200 code를 준다면, 아무나 접근 가능함을 의미.
        self.assertEqual(
            response.status_code,
            200,
            "Status code isn't 200.",
        )

        # data가 list인지 아닌지 확인 -> 통과 시, 우리의 코드(views.py)가 list를 줄거라는 확신이 생김.
        self.assertIsInstance(
            data,
            list,
        )
        # data의 길이를 확인
        self.assertEqual(
            len(data),
            1,
        )
        # name과 description확인
        self.assertEqual(
            data[0]["name"],
            self.NAME,
        )
        self.assertEqual(
            data[0]["description"],
            self.DESC,
        )
