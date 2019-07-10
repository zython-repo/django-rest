from rest_framework import serializers
from .models import BoardList

class ListSerializer(serializers.ModelSerializer):
    tag = serializers.PrimaryKeyRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = BoardList
        fields = '__all__'
        
    def get_created_at(self, instance):
        return instance.created_at.strftime('%B %d, %Y')
