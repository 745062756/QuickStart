from django.shortcuts import render
from rest_framework import viewsets
from quickstart.Serializers import UserSerializer,GroupSerializer
from django.contrib.auth.models import User, Group
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):#modelviewset has its own fields. 
	
	queryset=User.objects.all().order_by('-date_joined')#order_by is method under Queryset, datejoined is field under user model. 
	serializer_class=UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
	queryset=Group.objects.all()
	serializer_class=GroupSerializer


