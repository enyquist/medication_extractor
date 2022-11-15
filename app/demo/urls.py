# third party libraries
from demo import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="demo-home"),
    path("", views.demo, name="demo-demo"),
]
