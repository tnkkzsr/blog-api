from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Post,Category

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ("id","title")

class PostSerializer(ModelSerializer):
    
    category = PrimaryKeyRelatedField(write_only=True, queryset=Category.objects.all(), required=False)

    class Meta:
        model = Post
        fields = ("id","title","content","header_image","created_at","updated_at","category","author")
        read_only_fields = ("author",)

    def create(self, validated_data):
        category = validated_data.pop("category", None)
        validated_data["author"] = self.context["request"].user
        post = Post.objects.create(category=category,**validated_data)
        return post
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["category"] = CategorySerializer(instance.category).data if instance.category else None
        return representation