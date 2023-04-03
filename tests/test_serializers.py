from unittest import TestCase
from asosiy.serializers import *
#
#
# class TestAktyorSerializer(TestCase):
    # def test_aktyor(self):
    #     aktyor = {"id": 2,
    #               "ism":"Dveyn Jonson",
    #               "davlat": "AQSH",
    #               "tugilgan_yil": "1965-02-12",
    #               "jins": "erkak"
    #     }
    #     serializer = AktyorSerializer(data=aktyor)
    #     assert serializer.is_valid() == False
    #     malumot = serializer.validated_data
    #     assert malumot.get('ism') == "Dveyn Jonson"
    # def test_invalid_aktyor(self):
    #     aktyor = {"id": 3,
    #               "ism": "n",
    #               "davlat": "AQSH",
    #               "tugilgan_yil": "1965-02-12",
    #               "jins": "erkak"
    #               }
    #     serializer = AktyorSerializer(data=aktyor)
    #     assert serializer.is_valid() == False
    #     print(serializer.errors)
#     def test_jins_validation(self):
#         aktyor = {"id": 3,
#                   "ism": "Dveyn Jonson",
#                   "davlat": "AQSH",
#                   "tugilgan_yil": "1965-02-12",
#                   "jins": "Erkak"
#                   }
#         serializer = AktyorSerializer(data=aktyor)
#         assert serializer.is_valid() == False
#         assert serializer.errors['jins'][0] == "Jins 'Erkak' yoki 'Ayol' bo'lishi kerak."
# class TestKinoSerializer(TestCase):
#     kino = {"nom": "Titanik",
#             "janr": "Action",
#             "yil": "1999-02-03",
#             "aktyorlar": [1, 2]
#     }
#     serializer = KinoCreateSerializer(data=kino)
#     assert serializer.is_valid() == True
#     assert serializer.validated_data["nom"] == "Titanik"
#
#
