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


class TestAmenity(APITestCase):
    NAME = "Test Amenity"
    DESC = "Test Des"
    UPDATED_NAME = "Updated name"
    UPDATED_DESC = "Updated description"

    # test를 위한 database생성
    def setUp(self):
        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    # get_object handler
    def test_amenity_not_found(self):
        response = self.client.get("/api/v1/rooms/amenities/2")
        self.assertEqual(response.status_code, 404)

    # get handler
    def test_get_amenity(self):
        # amenity가 존재하지 않음 확인
        self.test_amenity_not_found()

        # amenity가 존재함 확인
        response = self.client.get("/api/v1/rooms/amenities/1")
        self.assertEqual(response.status_code, 200)

        # amenity가 동일한 지 확인
        data = response.json()
        self.assertEqual(data["name"], self.NAME)
        self.assertEqual(data["description"], self.DESC)

    # put handler
    def test_put_amenity(self):
        # failed case
        failed_name = "aaaaaaaaaaaaaaaaaaaaaa"

        # amenity가 존재하지 않음 확인
        self.test_amenity_not_found()

        response = self.client.put(
            "/api/v1/rooms/amenities/1",
            amenity=models.Amenity.objects.get(pk=1),
            data={
                "name": self.UPDATED_NAME,
                "description": self.UPDATED_DESC,
            },
        )

        data = response.json()
        self.assertEqual(data["name"], self.UPDATED_NAME)
        self.assertEqual(data["description"], self.UPDATED_DESC)
        self.assertEqual(response.status_code, 200)

        fail_response = self.client.put(
            "/api/v1/rooms/amenities/1",
            data={"name": failed_name},
        )
        data = fail_response.json()
        self.assertEqual(fail_response.status_code, 400)

    # delete handler
    def test_delete_amenity(self):
        response = self.client.delete("/api/v1/rooms/amenities/1")
        self.assertEqual(response.status_code, 204)
