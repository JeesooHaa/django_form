from django.urls import path
from . import views

app_name = 'articles'

# /articles/__
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
]
