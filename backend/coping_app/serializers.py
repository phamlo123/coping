from dataclasses import Field
import typing
from rest_framework import serializers
from coping_app.models.user import CustomUser
from coping_app.models.company import Company
from coping_app.models.internship import Internship
from coping_app.models.post import Post
from coping_app.models.comment import Comment


class UserSerializer(serializers.Serializer):
    internships = serializers.PrimaryKeyRelatedField(many=True, queryset=Internship.objects.all())
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'year', 'college', 'number_coops_completed', 'linkedin']

    def create(self, validated_data) -> CustomUser:
        return CustomUser.create(**validated_data)
    
    def update(self, instance, validated_data) -> CustomUser:
        return instance

class CompanySerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    class Meta:
        model = Company
        fields = ['id', 'name']

    def create(self, validated_data):
        return Company.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return Company.update(instance, validated_data)
    
class InternshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internship
        fields = ['id', 'owner', 'company', 'review', 'pay', 'title', 'co_op_num', 'cycle', 'tasks', 'drug_test']
    owner = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data):
        return Internship.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return Internship.objects.update(instance, validated_data)

class PostSerializer(serializers.Serializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Post
        fields = ['id', 'owner', 'content', 'tags']
    
    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return Post.objects.update(instance, validated_data)
    

class CommentSerializer(serializers.Serializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    post_id = serializers.ReadOnlyField(source='post.id')
    class Meta:
        model = Post
        fields = ['id', 'owner', 'post_id', 'content']
    
    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)




    