from django.urls import path

from postings.views import (
    OperatingListView,
    OperatingDetailView,
    OperatingCommentView
)

urlpatterns = [
    path("/operatings", OperatingListView.as_view()),
    path("/operatings/detail", OperatingDetailView.as_view()),
    path("/operatings/detail/<int:posting_id>", OperatingDetailView.as_view()),
    path("/operatings/comment", OperatingCommentView.as_view())
]
