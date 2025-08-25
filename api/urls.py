from django.urls import path
from .views import MenuListCreateView, MenuRetrieveUpdateView

urlpatterns = [
    path('menus/', MenuListCreateView.as_view(), name='menu-list'),
    path('menus/<int:pk>/', MenuRetrieveUpdateView.as_view(), name='menu-detail'),
]
