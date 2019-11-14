from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
     # ex: /polls/5/
    path('<int:id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:id>/vote/', views.vote, name='vote'),
    path('<int:id>/getRecap/', views.getRecap, name='getRecap'),
    path('upload/csv/', views.upload_csv, name='upload_csv'),
]