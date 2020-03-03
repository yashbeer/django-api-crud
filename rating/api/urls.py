from django.conf.urls import url

from .views import (
    MovieList,
    MovieDetail
)

urlpatterns = [
    url(r'^movies/', MovieList.as_view(), name='movie-list'),
    url(r'^movie/(?P<pk>\d+)', MovieDetail.as_view(), name='movie-detail'),
]