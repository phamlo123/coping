from dataclasses import Field
import typing
from rest_framework import serializers
from coping_app.models.user import CustomUser
from coping_app.models.company import Company
from coping_app.models.internship import Internship
from coping_app.models.post import Post
from coping_app.models.comment import Comment
from typing import Optional

class UserSerializer(serializers.ModelSerializer):
    # internships = serializers.PrimaryKeyRelatedField(many=True, queryset=Internship.objects.all())
    # posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'year', 'college', 'number_coops_completed', 'linkedin', 'internships']

    def create(self, validated_data) -> CustomUser:
        return CustomUser.create(**validated_data)
    
    def update(self, instance, validated_data) -> CustomUser:
        return instance

class CompanySerializer(serializers.ModelSerializer):
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

    def create(self, validated_data) -> Optional[Internship]:
        return Internship.objects.create(**validated_data)

    def update(self, instance, validated_data) -> Optional[Internship]:
        instance.review = validated_data.get("review", instance.review)
        instance.pay = validated_data.get("pay", instance.pay)
        instance.title = validated_data.get("title", instance.title)
        instance.cycle = validated_data.get("cycle", instance.cycle)
        instance.tasks = validated_data.get("tasks", instance.tasks)
        instance.drug_test = validated_data.get("drug_test", instance.drug_test)
        try:
            instance.save()
        except:
            return
        return instance

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    #TODO: need to take care of comments that belong to a post
    # post_comments = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all())
    class Meta:
        model = Post
        fields = ['id', 'owner', 'title', 'content', 'tags', 'post_comments']
        depth = 1
    
    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return Post.objects.update(instance, validated_data)
    

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    post = serializers.PrimaryKeyRelatedField(required=True, queryset=Post.objects.filter())
    class Meta:
        model = Post
        fields = ['id', 'owner', 'content', 'post']
        depth = 1
    
    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)




    