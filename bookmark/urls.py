from django.contrib import admin
from django.urls import path, include

from . import views
app_name = "bookmark"
urlpatterns = [
    path("", views.BookmarkLV.as_view(), name ="index"),
    path("<int:pk>/", views.BookmarkDV.as_view(), name="detail"), # genericview 에서는 pk로 받음 .
]
