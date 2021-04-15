from django.urls import path
from .views import list_raffles, add_raffles, delete_raffles


urlpatterns = [
    path("", list_raffles, name="list-raffles"),
    path("add/", add_raffles, name="add-raffles"),
    path("<int:raffle_pk>/delete/", delete_raffles, name="delete-raffles"),
]