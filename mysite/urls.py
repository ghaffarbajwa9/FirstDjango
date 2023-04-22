from django.contrib import admin
from django.urls import include, path
from mysite import views

urlpatterns = [
    path("", views.home),
    # path("about-us/", views.aboutUs),
    # path("portfolio/", views.portfolio),
    # path("contact-us/", views.contactUs),
    # path("course/<courseid>", views.courseDetails),
    path("polls/", include("polls.urls")),

    path('admin/', admin.site.urls),
]
