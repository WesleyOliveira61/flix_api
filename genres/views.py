
from genres.models import Genre
from genres.serializers import GenreSerailizer
from rest_framework.permissions import IsAuthenticated
# restframework
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from app.permissions import GlobalDefaultPermission

# Create your views here.

"""
@csrf_exempt
def genre_create_list_view(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        data = [{'id': genre.id, 'name': genre.name} for genre in genres]
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        new_genre = Genre(name=data['name'])
        new_genre.save()
        return JsonResponse(
            {'id': new_genre.id, 'name':new_genre.name},
            status=201,
            )
"""


class GenreCreateListView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerailizer


class GenreRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Genre.objects.all()
    serializer_class = GenreSerailizer
