from django.urls import re_path
from hello import views


urlpatterns = [
  re_path(r'^hello-world/$' ,views.hello_view_func),
]