from django.urls import path
from .views import *

urlpatterns = [
    path('', sentiment_analysis, name='sentiment_analysis')
]