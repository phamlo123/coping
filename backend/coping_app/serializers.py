import typing
from rest_framework import serializers
from coping_app.models.user import CustomUser
from coping_app.models.company import Company
from coping_app.models.internship import Internship
from coping_app.models.post import Post
from coping_app.models.comment import Comment


class UserSerializer(serializers.Serializer):
    # id = serializers.IntegerField(read_only=True)
    # username = serializers.CharField(max_length=200, allow_blank=False, =True)
    # year = serializers.CharField(max_length=100, allow_blank=True, required=True)
    # college = serializers.CharField(max_length=100, allow_blank=True, required=False)
    # number_coops_completed = serializers.IntegerField(required=False, allow_blank=True)
    # linkedin = serializers.CharField(max_length=100, required=False, allow_blank=True)
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'year', 'college', 'number_coops_completed', 'linkedin']

    def create(self, validated_data) -> CustomUser:
        return CustomUser.create(**validated_data)
    
    def update(self, instance, validated_data) -> CustomUser:
        return instance

class CompanySerializer(serializers.Serializer):

    def create(self, validated_data):
        return Company.create(validated_data)

    def update(self, instance, validated_data):
        return Company.update(instance, validated_data)

class InternshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internship
        fields = ['id', 'user', 'company', 'review', 'pay', 'title', 'co_op_num', 'cycle', 'task', 'drug_test']
    user = serializers.ReadOnlyField(source='user.username')


    def create(self, validated_data):
        return Internship.create(validated_data)

    def update(self, instance, validated_data):
        return Internship.update(instance, validated_data)

class PostSerializer(serializers.Serializer):
    def create(self, validated_data):
        return Post.create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    

class CommentSerializer(serializers.Serializer):
    def create(self, validated_data):
        return Comment.create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)




    