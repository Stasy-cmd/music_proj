from rest_framework import serializers
from music.models import Track, Selection
from user.serializers import UserSerializer


class TrackSerializer(serializers.ModelSerializer):
    stared_user = UserSerializer(many=True)

    class Meta:
        model = Track
        read_only_fields = ('id',)
        fields = (
            'id',
            'name',
            'author',
            'release_date',
            'genre',
            'duration_in_seconds',
            'album',
            'logo',
            'track_file',
            'stared_user',
        )


class StaredTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        read_only_fields = ('id',)
        fields = (
            'id',
            'name',
            'author',
            'release_date',
            'genre',
            'duration_in_seconds',
            'album',
            'logo',
            'track_file',
        )


class SelectionDetailSerializer(serializers.ModelSerializer):
    items = TrackSerializer(many=True)
    owner = serializers.SlugRelatedField(
        slug_field="email",
        read_only=True,
    )

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionSerializer(serializers.ModelSerializer):
    items = TrackSerializer(many=True)
    owner = UserSerializer()

    class Meta:
        model = Selection
        fields = ('id', 'items', 'owner')
