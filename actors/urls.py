from django.urls import path
from . import views


urlpatterns = [
    path('actors/', views.ActorCreateListView.as_view(), name='actors'),
    path('actor/<int:pk>/', views.ActorRetrieveUpdateDestroyView.as_view(), name='actors-edit'),
]
