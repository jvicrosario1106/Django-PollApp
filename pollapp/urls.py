from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = 'home'),
    path("vote/<str:pk>/", views.vote, name = 'vote'),
    path("result/<str:pk>/", views.result, name = 'result'),

]