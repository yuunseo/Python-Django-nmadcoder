# django에 내장된 class가 아닌 DRF에 내장된 class를 사용
from rest_framework.test import APITestCase
from . import models


class TestAmenities(APITestCase):
    # 이후 같은 부분 반복과 수정을 줄이기 위해 class 변수로 지정
    NAME = "Amenity Test"
    DESC = "Amenity Des"
    URL = "/api/v1/rooms/amenities/"

    # setUp method로 인해 Amenity가 test하자마자 생성 될 예정.
    def setUp(self):
        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    def test_all_amenities(self):  # self는 APITestCase를 가리킴.
        response = self.client.get(self.URL)
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

    def test_create_amenity(self):
        new_amenity_name = "New Amenity"
        new_amenity_description = "New Amenity desc."

        # data={}를 보낼 수도 있음.
        response = self.client.post(
            self.URL,
            data={
                "name": "New Amenity",
                "description": "New Amenity desc.",
            },
        )
        data = response.json()

        # msg부분(assert가 참이 아닐 경우) 번거롭더라도 꼭 쓰기!
        self.assertEqual(
            response.status_code,
            200,
            "Status code isn't 200.",
        )

        self.assertEqual(
            data["name"],
            new_amenity_name,
        )
        self.assertEqual(
            data["description"],
            new_amenity_description,
        )

        # 예외처리를 위해 아무런 data없이 post request 전송
        response = self.client.post(self.URL)
        data = response.json()

        self.assertEqual(response.status_code, 400)
        # 에러 메세지 안에 담긴 "name"을 찾아.
        # "name"이 에러 메세지 안에 담겨있다면 "name"에서 error 발생인거지.
        self.assertIn("name", data)
