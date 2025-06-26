from django.urls import path
from . import views

urlpatterns = [
    # example route
    path("create/", views.create_post, name="create_post"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
]
