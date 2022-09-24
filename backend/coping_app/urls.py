from django.urls import path
from coping_app import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.api_root),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('internships/', views.InternshipList.as_view()),
    path('internships/<int:pk>/', views.InternshipList.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
