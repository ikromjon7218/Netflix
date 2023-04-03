from unittest import TestCase
from asosiy.views import *
from asosiy.models import *
from rest_framework.test import APIClient
class TestAktyorViewSet(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()

    # def test_aktyorlar(self):
    #     natija = self.client.get("/aktyorlar/")
    #     assert natija.status_code == 200
    #
    #     aklar = natija.data
    #     assert len(aklar) == Aktyor.objects.count()
    #
    #     assert aklar[0]['ism'] == Aktyor.objects.first().ism

    # def test_aktyor_valid(self):
    #     natija = self.client.get('/aktyor/3/')
    #     assert natija.status_code == 200
    #     assert natija.data['id'] == 3
    #     assert natija.data['ism'] == Aktyor.objects.get(id=3).ism

    # def test_aktyor_invalid(self):
    #     natija = self.client.get('/aktyor/29/')
    #     assert natija.status_code == 200
    #     assert natija.data['xabar'] == "BUNaqa yo'q"

    # def test_aktyor_qoshish_invalid(self):
    #     aktyor = {"id": 1,
    #     "ism": "Tom Hanks",
    #     "davlat": "AQSH",
    #     "tugilgan_yil": "1939-02-12",
    #               "jins": "erkak"}
    #     natija = self.client.post('/aktyorlar/', data=aktyor)
    #     assert natija.status_code == 200

    # def test_aktyor_qoshish(self):
    #     aktyor = {"id": 1,
    #               "ism": "Tom Hanks",
    #               "davlat": "AQSH",
    #               "tugilgan_yil": "1939-02-12",
    #               "jins": "Erkak"}
    #     natija = self.client.post('/aktyorlar/', data=aktyor)
    #     print(natija.data)
    #     # assert natija.status_code == 201
    #     # assert natija.data('id') == Aktyor.objects.last().id
    #     assert natija.data.get('ism') == Aktyor.objects.last().ism
    #     assert natija.data.get('davlat') == Aktyor.objects.last().davlat

    def test_aktyor_put(self):
        aktyor = {"id": 1,
                  "ism": "Tom Hanks",
                  "davlat": "AQSH",
                  "tugilgan_yil": "1939-02-12",
                  "jins": "Erkak"}

        natija = self.client.put('/aktyor/5/', data=aktyor)
        assert natija.status_code == 202
        assert natija.data['ism'] == "Tom Hanks" == Aktyor.objects.get(id=5).ism
        assert natija.data['davlat'] == "AQSH" == Aktyor.objects.get(id=5).davlat