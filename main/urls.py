from django.urls import path
from .views import *


urlpatterns = [
    path('get-akademiya/', get_akademiya_view),
    path('get-banner/', get_banner_view),
    path('get-banner-video/', get_banner_video_view),
    path('get-players/', get_players_view),
    path('get-shop/', get_shop_view),
    path('get-stadium-info/', get_stadium_info_view),
    path('get-logo/', get_logo_view),
    path('get-information/', get_information_view),
    path('get-administrator/', get_administrator_view),
    path('get-coaches/', get_coaches_view),
    path('get-history/', get_history_view),
    path('get-goal/', get_goal_view),
    path('get-recommendations/', get_recommendations_view),
    path('get-Training/', get_Training_view),
    path('tables/', tables),
]                                                                   