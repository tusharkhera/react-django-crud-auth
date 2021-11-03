from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, QuoteSerializer
from .models import Quote
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class QuoteViewSet(viewsets.ModelViewSet) :
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]