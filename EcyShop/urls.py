from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('mycart/', views.CartView.as_view(), name='mycart'),
]
