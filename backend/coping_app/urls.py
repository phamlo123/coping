from django.urls import path
from coping_app import views
from rest_framework.urlpatterns import format_suffix_patterns
from coping_app.views import UserViewSet, InternshipViewSet, CompanyViewSet, PostViewSet, CommentViewSet


internship_list = InternshipViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

internship_detail = InternshipViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

company_list = CompanyViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

company_detail = CompanyViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

post_list = PostViewSet.as_view({
    'get': 'list'
})

post_detail = PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', views.api_root),
    path('users/', user_list, name="user-list"),
    path('users/<int:pk>/', user_detail, name="user-detail"),
    path('internships/', internship_list, name="internship-list"),
    path('internships/<int:pk>/', internship_detail, name="internship-detail"),
    path('companies/', company_list, name="company-list"),
    path('companies/<int:pk>/', company_detail, name="company-detail"),
    path('posts/', post_list, name="post-list")
    path('posts/<int:pk>', post_detail, name="post-detail")
]
urlpatterns = format_suffix_patterns(urlpatterns)
