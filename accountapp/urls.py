from django.urls import path

from accountapp.views import hello_world
# 이렇게 써두면 좋다
app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world')
]