from rest_framework import serializers
from movies.models import Movie
from django.db.models import Avg
from genres.serializers import GenreSerailizer
from actors.serializers import ActorSerializer


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year < 1987:
            raise serializers.ValidationError(
                'A data não pode ser anterior a 1980')
        return value

    def validate_resume(self, value):
        if len(value) < 20:
            raise serializers.ValidationError(
                'O Campo resumo não pode ser menos que 20 caracteres.'
            )
        return value


class MovieListDetailsSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    genre = GenreSerailizer()
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = [
            'id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume'
            ]

    def get_rate(sel, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if rate:
            return round(rate, 1)
        return None
