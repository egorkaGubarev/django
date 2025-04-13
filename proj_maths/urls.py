from django.contrib import admin
from django.urls import path
from proj_maths import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello', views.hello),
    path('hello/<str:name>', views.hello),
    path('', views.index),
    path('terms-list', views.terms_list),
    path('add-term', views.add_term),
    path('send-term', views.send_term),
    path('stats', views.show_stats),
    path('result', views.result),
    path('game', views.quiz_view),
    path('results', views.results_view)
]
