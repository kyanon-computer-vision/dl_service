from rest_framework import serializers
from .models import Profile
from apps.api.core.constants import STC_DEFAUL_PROFILE_IMG

class ProfileSerializer(serializers.ModelSerializer):
    username    = serializers.CharField(source='user.username')
    bio         = serializers.CharField(allow_blank=True, required=False)
    image       = serializers.SerializerMethodField()
    
    class Meta:
        model = Profile
        fields = ('username', 'bio', 'image',)
        read_only_fields = ('username',)

    def get_image(self, obj):
        if obj.image:
            return obj.image
        
        return STC_DEFAUL_PROFILE_IMG
