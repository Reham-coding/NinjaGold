from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('goldCal/<str:which_form>', views.goldCal),
    path('reset', views.reset)
]