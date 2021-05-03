from django.urls import path

from .views import check_task, make_task

urlpatterns = [
    path('screenshot/', make_task),
    path('check/<int:pk>', check_task),
]
