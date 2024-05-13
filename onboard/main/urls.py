from django.urls import path
from . import views

urlpatterns = [
    path("", views.main),
    path("board", views.onboard),
    path("get-next-question/", views.get_next_question),
]
