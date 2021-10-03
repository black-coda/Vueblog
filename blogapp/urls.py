from django.urls import path
from . import views

app_name = 'blogapp'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<slug:post>/', views.post_details, name='post_details'),
]