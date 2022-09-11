from django.urls import path
from .views import home, order

urlpatterns = [
    path("", home, name="home"),
    path('order/', order, name='order'),
]
