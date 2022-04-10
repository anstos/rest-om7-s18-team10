from django.urls import path
from author import views
# from author.views import AuthorListView, AuthorDetailView, create_author, edit_author

urlpatterns = [
    # path('all/', AuthorListView.as_view(), name="all_authors"),
    # path('<int:pk>/', AuthorDetailView.as_view(), name="author_detail"),
    # path('new/', create_author, name="create_author"),
    # path('<int:pk>/edit/', edit_author, name="edit_author"),
    path('/', views.author_list),
    path('/<int:pk>/', views.author_detail),
]
