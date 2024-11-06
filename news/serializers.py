from rest_framework import serializers
from .models import Post

class Postserializers(serializers.ModelSerializer):
    def create(self, validated_data):
        post= Post.objects.create(**validated_data)
        post.save()
        
        
    class Meta:
        model=Post
        fields =['id','title','content']