from django.urls import path
from author import views

urlpatterns = [
    path('/', views.author_list),
    path('/<int:pk>/', views.author_detail),
]
