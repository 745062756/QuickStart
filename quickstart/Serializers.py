from django.contrib.auth.models import User, Group #import model because it will be used. 
from rest_framework import serializers #import class, url is from Hyperlink. 

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=User
		fields=('url','username','email','groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Group
		fields=('url','name')
