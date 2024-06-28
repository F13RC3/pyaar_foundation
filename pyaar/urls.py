from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("causes/", views.causes, name="causes"),
    path("contact/", views.contact, name="contact"),
    path("donate/", views.donate, name="donate"),
    path("event/", views.event, name="event"),
    path("gallery/", views.gallery, name="gallery"),
    path("blog/", views.blog, name="blog"),
]