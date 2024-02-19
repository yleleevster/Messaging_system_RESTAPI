from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_users),
    path('users/<int:user_id>/', views.specific_user),
    path('messages/', views.messages),
    path('specific-message/<int:message_id>/', views.specific_message),
    path('all-messages/<int:user_id>/', views.all_user_messages),
    path('all-unread-messages/<int:user_id>/', views.all_user_unread_messages),
]
