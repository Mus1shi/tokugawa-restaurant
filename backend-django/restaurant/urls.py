from django.urls import path
from .views import (
    home, menu, contact, history, reservations, send_contact,
    like_comment, dislike_comment
)

urlpatterns = [
    path('', home, name='home'),
    path('menu/', menu, name='menu'),
    path('contact/', contact, name='contact'),
    path('history/', history, name='history'),
    path('reservations/', reservations, name='reservations'),
    path('send_contact/', send_contact, name='send_contact'),
    path('like/<int:comment_id>/', like_comment, name='like_comment'),
    path('dislike/<int:comment_id>/', dislike_comment, name='dislike_comment'),
]
