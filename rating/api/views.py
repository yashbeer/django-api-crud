from rest_framework import generics, permissions
from rest_framework import filters

from rating.models import Movie, Genre
from rating.api.serializers import MovieSerializer


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permission to only allow admin to add, edit, and delete.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # User must be superuser
        if request.user.is_authenticated:
            return request.user.is_superuser
        else:
            return False

    
class MovieList(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer