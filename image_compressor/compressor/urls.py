from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_image, name='upload_image'),
    path('download/<int:image_id>/', views.download_image, name='download_image'),
]
