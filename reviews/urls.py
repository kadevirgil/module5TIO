from django.urls import path

from . import views 

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("confirmation", views.ConfirmationView.as_view()),
    path("review_list", views.ReviewListView.as_view()),
    path("reviews/favorite", views.AddFavorite.as_view()),
    path("review_details/<int:pk>", views.ReviewDetailsView.as_view())
]
