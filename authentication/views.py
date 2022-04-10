# from django.views import generic

# from authentication.forms import CustomUserCreationForm, CustomUserUpdateForm
# from authentication.models import CustomUser


# class CustomUserCreationView(generic.CreateView):

#     model = CustomUser
#     form_class = CustomUserCreationForm
#     template_name = 'authentication/create_update.html'
#     success_url = '/book/all'
#     extra_context = {'title': 'Create User'}


# class CustomUserUpdateView(generic.UpdateView):

#     model = CustomUser
#     form_class = CustomUserUpdateForm
#     template_name = 'authentication/create_update.html'
#     success_url = '/book/all'
#     extra_context = {'title': 'Update User'}


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authentication.models import CustomUser
from authentication.serializers import UserSerializer


@api_view(['GET', 'POST'])
def user_list(request):
    """
    View a list of all users, or create a new user.
    """
    if request.method == 'GET':
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    """
    Retrieve, update or delete an user.
    """
    try:
        user = CustomUser.objects.get(pk=pk)
    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
