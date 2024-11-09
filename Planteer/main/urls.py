from django.urls import path
from . import views
app_name='main'
urlpatterns = [
    path('', views.contact_view, name='contact_view'),
    path('messages/', views.contact_messages_view, name='contact_messages_view'),
]