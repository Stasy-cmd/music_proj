from django.urls import path

from music import views

urlpatterns = [
    path('track/all/', views.TrackView.as_view()),
    path('track/<int:pk>/', views.TrackRetrieveView.as_view()),
    path('track/<slug:post_slug>/', views.TrackRetrieveView.as_view()),
    path('track/<int:pk>/favorite/', views.StaredTrackView.as_view()),
    path('track/favorite/all/', views.StaredTracksListView.as_view()),
    path('track/favorite/', views.StaredTracksView.as_view()),
    path('selection/', views.SelectionListView.as_view()),
    path('selection/<int:pk>/', views.SelectionRetrieveView.as_view()),
    path('selection/<int:pk>/update/', views.SelectionUpdateView.as_view()),
    path('selection/create/', views.SelectionCreateView.as_view()),
    path('selection/<int:pk>/delete/', views.SelectionDestroyView.as_view()),
]
