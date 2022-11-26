
from django.urls import path
from webapp.views.base import IndexView
from webapp.views.photos import PhotoCreate, PhotoView



urlpatterns= [
    path("", IndexView.as_view(), name='index'),
    path('photo/add', PhotoCreate.as_view(), name="photo_add"),
    path('photo/<int:pk>/', PhotoView.as_view(), name="photo_detail")
]