from django.contrib import admin
from django.urls import path, include

app_name = 'blogapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls', namespace='blogapp')),
]
