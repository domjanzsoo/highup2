from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('skills/', views.skills, name="skills"),
    path('skills/<str:pk>/', views.skill, name="skill"),
    path('update-skill/<str:pk>/', views.updateSkill, name="update-skill"),
    path('delete-skill/<str:pk>/', views.deleteSkill, name="delete-skill"),
    path('create-skill/', views.createSkill, name="create-skill")
]