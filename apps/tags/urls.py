from django.urls import path
from . import views

urlpatterns = [
    path('tags/', views.list_tags, name='list-tags'),
    path('tags/<int:id/', views.detail_tags, name='detail-tags'),
]