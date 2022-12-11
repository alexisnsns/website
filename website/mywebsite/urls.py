
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('alanwatts.urls')),
    path('life/',TemplateView.as_view(template_name='life.html'), name='life'),
    path('videos/',TemplateView.as_view(template_name='videos.html'), name='videos'),

]
