from django.contrib import admin
from django.urls import path, include
from asosiy.views import *
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register("kinolar", KinoViewSet)
router.register("izohlar", IzohViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', HelloAPIView.as_view()),

    path('get_token/', obtain_auth_token),

    path('aktyorlar/', AktyorlarAPIView.as_view()),
    path('aktyor/<int:pk>/', AktyorDetailAPIView.as_view()),

    path('tariflar/', TariflarAPIView.as_view()),
    path('', include(router.urls)),

    # path('kinolar/', KinolarAPIView.as_view()),
    # path('kino/<int:pk>/', KinoDetailAPIView.as_view()),

]
