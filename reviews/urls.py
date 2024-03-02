from django.urls import path

from . import views

urlpatterns = [
     path("", views.ReviewView.as_view()),
     path("thank-you", views.ThankYouView.as_view()),
     path("reviews", views.ReviewsListView.as_view() , name = 'review_list'),
     path("reviews/favorite", views.AddFavorite.as_view()),
     path("reviews/<int:pk>", views.SingleReviewView.as_view())  #pk means the primary key
]