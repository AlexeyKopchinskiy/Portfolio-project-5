from django.urls import path
from . import views

urlpatterns = [
    path("reader/", views.reader_dashboard, name="reader_dashboard"),
    path("author/", views.author_dashboard, name="author_dashboard"),
    path("patron/", views.patron_dashboard, name="patron_dashboard"),
]
