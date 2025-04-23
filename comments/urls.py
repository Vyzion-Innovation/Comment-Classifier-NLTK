from django.urls import path
from .views import comment_view

urlpatterns = [
    path('', comment_view, name='comment_form'),
    path('submit/', comment_view, name='submit_comment'),
]
