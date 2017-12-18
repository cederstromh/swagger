from rest_framework import serializers
from swagger_app.models import Music


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        # fields = '___all___'
        fields = ('id', 'song', 'singer', 'last_modify_date', 'created')
