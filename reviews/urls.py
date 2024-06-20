from django.urls import path

from . import views 

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("confirmation", views.confirmation)
]
