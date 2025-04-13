from django.urls import path
from proj_astron import views

urlpatterns = [
    path('', views.index),
    path('terms-list', views.stars_list),
    path('add-term', views.add_star),
    path('send-term', views.send_star),
    path('stats', views.show_stats),
    path('game', views.quiz_view),
    path('results', views.results_view)
]
