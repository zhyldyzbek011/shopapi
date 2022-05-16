from django.urls import path
from Basket import views

urlpatterns = [
    path('order/', views.BasketApiView.as_view())
]