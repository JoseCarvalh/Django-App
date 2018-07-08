from django.urls import include, path
from . import views

app_name = 'Users'

urlpatterns = [
    path('', views.index),
    path('add/', include('add.urls'), name='add'),
    path('list/', include('list.urls'), name='list'),
]
