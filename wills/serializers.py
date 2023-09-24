from .models import Will, Asset #, Inheritor, InheritorGroup, Distribution
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Will Serializer
class WillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # Model to serialize
        model = Will
        # Get fields to serialize
        fields = ['id', 'user_name', 'user_address', 'user_phone', 'user_tax_id', 'created_when']
        #fields  = [f.name for f in Will._meta.get_fields(False)]
        #print(fields)
    
# Asset Serializer
class AssetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # Model to serialize
        model = Asset
        # Get fields to serialize
        fields = ['id', 'will_id', 'name', 'description', 'quantity', 'location']
        #fields  = [f.name for f in Asset._meta.get_fields()]
        #print(fields)

# # Inheritor Serializer
# class InheritorSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         # Model to serialize
#         model = Inheritor
#         # Get fields to serialize
#         fields  = [f.name for f in Inheritor._meta.get_fields()]

# # InheritorGroup Serializer
# class InheritorGroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         # Model to serialize
#         model = InheritorGroup
#         # Get fields to serialize
#         fields  = [f.name for f in InheritorGroup._meta.get_fields()]

# # Distribution Serializer
# class DistributionSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         # Model to serialize
#         model = Distribution
#         # Get fields to serialize
#         fields  = [f.name for f in Distribution._meta.get_fields()]