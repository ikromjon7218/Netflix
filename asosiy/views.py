from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import *

from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from .serializers import *
from .models import *

class HelloAPIView(APIView):
    def get(self, request):
        contend = {"xabar": "Salom, Dunyo !"}
        return Response(contend)

    def post(self, request):
        data = request.data
        content = {"xabar": "Malumot qo'shildi.",
                   "ma'lumot": data}
        return Response(content)

class AktyorlarAPIView(APIView):
    def get(self, request):
        aktyorlar = Aktyor.objects.all()
        serializer = AktyorSerializer(aktyorlar, many=True)
        return Response(serializer.data)
    def post(self, request):
        aktyor = request.data
        serializer = AktyorSerializer(data=aktyor)
        if serializer.is_valid():
            Aktyor.objects.create(
                ism = serializer.validated_data.get('ism'),
                tugilgan_yil=serializer.validated_data.get('tugilgan_yil'),
                davlat=serializer.validated_data.get('davlat'),
                jins=serializer.validated_data.get('jins'),)
            return Response(serializer.data)
        return Response(serializer.errors)

class AktyorDetailAPIView(APIView):
    def get(self, request, pk):
        aktyor = Aktyor.objects.get(id=pk)
        serializer = AktyorSerializer(aktyor)
        return Response(serializer.data)
    def put(self, request, pk):
        aktyor = Aktyor.objects.get(id=pk)
        serializer = AktyorSerializer(aktyor, data=request.data)
        if serializer.is_valid():
            aktyor.ism = serializer.validated_data.get('ism')
            aktyor.davlat = serializer.validated_data.get('davlat')
            aktyor.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class TariflarAPIView(APIView):
    def get(self, request):
        tariflar = Tarif.objects.all()
        serializer = TarifSerializer(tariflar, many=True)
        return Response(serializer.data)

    def post(self, request):
        tarif = request.data
        serializer = TarifCreateSerializer(data=tarif)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TarifDetailAPIView(APIView):
    def get(self, request, pk):
        tarif = Tarif.objects.get(id=pk)
        serializer = TarifSerializer(tarif)
        return Response(serializer.data)

    def put(self, request, pk):
        tarif = Tarif.objects.get(id=pk)
        serializer = TarifSerializer(tarif, data=request.data)
        if serializer.is_valid():
            tarif.nom = serializer.validated_data.get('nom')
            tarif.narx = serializer.validated_data.get('narx')
            tarif.muddat = serializer.validated_data.get('muddat')
            tarif.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tarif = Tarif.objects.get(id=pk)
        tarif.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# class KinolarAPIView(APIView):
#     def get(self, request):
#         kinolar = Kino.objects.all()
#         serializer = KinoSerializer(kinolar, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         kino = request.data
#         serializer = KinoCreateSerializer(data=kino)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class KinoViewSet(ModelViewSet):
    queryset = Kino.objects.all()
    serializer_class = KinoSerializer
    @action(detail=True)
    def aktyorlar(self, request, pk):
        actors = Kino.objects.get(id=pk).aktyorlar.all()
        serializer = AktyorSerializer(actors, many=True)
        return(Response(serializer.data))


# class KinoDetailAPIView(APIView):
#     def get(self, request, pk):
#         kino = Kino.objects.get(id=pk)
#         serializer = AktyorSerializer(kino)
#         return Response(serializer.data)
#     def put(self, request, pk):
#         kino = Kino.objects.get(id=pk)
#         serializer = KinoCreateSerializer(kino, data=request.data)
#         if serializer.is_valid():
#             kino.save()
#             raise Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class IzohViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Izoh.objects.all()
    serializer_class = IzohSerializer

    def get_queryset(self):
        queryset = Izoh.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)