from rest_framework import serializers
from .models import *
from django.core.validators import MinValueValidator

class AktyorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    ism = serializers.CharField(max_length=100)
    tugilgan_yil = serializers.DateField()
    jins = serializers.CharField(max_length=10)
    davlat = serializers.CharField(max_length=100, allow_blank=True)

    def validate_ism(self, qiymat):
        if len(qiymat) < 3:
            raise serializers.ValidationError("Ism qiymati 3 tadan kam bo'lmaydi")
        return qiymat

    def validate_jins(self, qiymat):
        if qiymat != "Erkak" and qiymat != "Ayol":

            raise serializers.ValidationError("Jins 'Erkak' yoki 'Ayol' bo'lishi kerak.")
        return qiymat

class TarifSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nom = serializers.CharField(max_length=100)
    narx = serializers.IntegerField(validators=[MinValueValidator(0)])
    muddat = serializers.CharField(max_length=30)

class TarifCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarif
        fields = '__all__'

class KinoSerializer(serializers.ModelSerializer):
    aktyorlar = AktyorSerializer(many=True)
    class Meta:
        model = Kino
        fields = '__all__'

class KinoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kino
        fields = '__all__'

class IzohSerializer(serializers.ModelSerializer):
    class Meta:
        model = Izoh
        fields = '__all__'