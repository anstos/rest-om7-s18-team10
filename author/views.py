# from django.views import generic
# from django.shortcuts import render, redirect, get_object_or_404
# from author.models import Author
# from .forms import AuthorCreationForm

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from author.models import Author
from author.serializers import AuthorSerializer

# class AuthorListView(generic.ListView):

#     model = Author
#     context_object_name = "authors"
#     template_name = 'author/list.html'


# class AuthorDetailView(generic.DetailView):

#     model = Author
#     context_object_name = "author"
#     template_name = 'author/detail.html'


# def create_author(request):
#     if request.method == "POST":
#         form = AuthorCreationForm(request.POST)
#         if form.is_valid():
#             post = form.save()
#             return redirect('author_detail', pk=post.pk)
#     else:
#         form = AuthorCreationForm()

#     return render(request, 'author/create_author.html', {'form': form})


# def edit_author(request, pk):
#     author = get_object_or_404(Author, pk=pk)
#     if request.method == "POST":
#         form = AuthorCreationForm(request.POST, instance=author)
#         if form.is_valid():
#             author = form.save()
#             return redirect('author_detail', pk=author.pk)
#     else:
#         form = AuthorCreationForm(instance=author)
#     return render(request, 'author/edit_author.html', {'form': form, 'pk': pk})

@csrf_exempt
def author_list(request):
    """
    List all code authors, or create a new author.
    """
    if request.method == 'GET':
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def author_detail(request, pk):
    """
    Retrieve, update or delete a code author.
    """
    try:
        author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AuthorSerializer(author)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AuthorSerializer(author, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        author.delete()
        return HttpResponse(status=204)