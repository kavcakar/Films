from django.urls import path
from movieapp.api import views as api_views

urlpatterns = [
    path('contains/', api_views.contain_list_create_api_view, name='contain-list'),
]
