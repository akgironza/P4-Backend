from django.shortcuts import render
from .models import Will, Asset #, Inheritor, InheritorGroup, Distribution
from rest_framework import viewsets, permissions
from .serializers import WillSerializer, AssetSerializer #, InheritorSerializer, InheritorGroupSerializer, DistributionSerializer

# Create your views here.

class WillViewSet(viewsets.ModelViewSet):
    # Main query for index route
    queryset = Will.objects.all()
    # Serializer class for serializing output
    serializer_class = WillSerializer
    # Set permission level, optional
    permission_classes = [permissions.AllowAny]

class AssetViewSet(viewsets.ModelViewSet):
    # Main query for index route
    queryset = Asset.objects.all()
    # Serializer class for serializing output
    serializer_class = AssetSerializer
    # Set permission level, optional
    permission_classes = [permissions.AllowAny]

# class InheritorViewSet(viewsets.ModelViewSet):
#     # Main query for index route
#     queryset = Inheritor.objects.all()
#     # Serializer class for serializing output
#     serializer_class = InheritorSerializer
#     # Set permission level, optional
#     permission_classes  = [permissions.AllowAny]

# class InheritorGroupViewSet(viewsets.ModelViewSet):
#     # Main query for index route
#     queryset = InheritorGroup.objects.all()
#     # Serializer class for serializing output
#     serializer_class = InheritorGroupSerializer
#     # Set permission level, optional
#     permission_classes  = [permissions.AllowAny]

# class DistributionViewSet(viewsets.ModelViewSet):
#     # Main query for index route
#     queryset = Distribution.objects.all()
#     # Serializer class for serializing output
#     serializer_class = DistributionSerializer
#     # Set permission level, optional
#     permission_classes  = [permissions.AllowAny]

