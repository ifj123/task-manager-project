from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from tasks.views import task_list  # ✅ Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('tasks/', include('tasks.urls')),
    path('', task_list, name='home'),  # ✅ Now it will work
    path('users/', include('django.contrib.auth.urls')),
]
