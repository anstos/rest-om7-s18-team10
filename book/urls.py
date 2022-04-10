from django.urls import path
from book import views

urlpatterns = [
    path('/', views.book_list),
    path('/<int:pk>/', views.book_detail),
]
