from django.urls import path
from . import views

urlpatterns = [
    path("", views.main),
    path("board", views.onboard),
    path("update_questions/", views.update_questions),
]
