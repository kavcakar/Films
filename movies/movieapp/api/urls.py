from django.urls import path
from movieapp.api import views as api_views

urlpatterns = [
    path('contains/', api_views.ContainListCreateAPIView.as_view(), name='contain-list'),
    path('contains/<int:pk>', api_views.ContainDetailAPIView.as_view(), name='contain-detail')
]


                  ### FUNCTION BASED Views###
# urlpatterns = [
#     path('contains/', api_views.contain_list_create_api_view, name='contain-list'),
#     path('contains/<int:pk>', api_views.contain_detail_api_view, name='contain-detail')
# ]
