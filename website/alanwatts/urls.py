from django.urls import path
from alanwatts import views

urlpatterns = [
    path('', views.index, name='index'),
    path('life/', views.life , name='life'),
    path('videos/', views.videos, name='videos')
]
