from rest_framework import serializers
from rating.models import Movie, Genre


class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = [
            'name'
        ]


class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    
    class Meta:
        model = Movie
        fields = [
            'id',
            'name',
            'director',
            'popularity',
            'imdb_score',
            'genre'
        ]
    
    def create(self, validated_data):
        genres_data = validated_data.pop('genre')
        movie = Movie.objects.create(**validated_data)
        for genre_data in genres_data:
            Genre.objects.create(movie=movie, **genre_data)
        return movie
        
    def update(self, instance, validated_data):
        genres_data = validated_data.pop('genre')
        genres = (instance.genre).all()
        genres = list(genres)
        instance.name = validated_data.get('name', instance.name)
        instance.director = validated_data.get('director', instance.director)
        instance.popularity = validated_data.get('popularity', instance.popularity)
        instance.imdb_score = validated_data.get('imdb_score', instance.imdb_score)
        instance.save()

        for genre_data in genres_data:
            genre = genres.pop(0)
            genre.name = genre_data.get('name', genre.name)
            genre.save()
        return instance
