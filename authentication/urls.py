from django.urls import path
from authentication import views

urlpatterns = [
    path('/', views.user_list),
    path('/<int:pk>/', views.user_detail),
]
