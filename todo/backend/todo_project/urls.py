from django.contrib import admin
from django.urls import include, path # new
from todos.views import DetailTodo, ListTodo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todos.urls')), # new
]
