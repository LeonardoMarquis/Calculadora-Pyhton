from django.urls import path
from .views import index, privacy_policy, user_terms

urlpatterns = [
    path('', index),
    path('privacy_policy', privacy_policy),
    path('user_terms', user_terms),
]