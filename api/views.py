from rest_framework import generics
from .models import Menu
from .serializers import MenuSerializer

class MenuListCreateView(generics.ListCreateAPIView):
	queryset = Menu.objects.all()
	serializer_class = MenuSerializer

class MenuRetrieveUpdateView(generics.RetrieveUpdateAPIView):
	queryset = Menu.objects.all()
	serializer_class = MenuSerializer
