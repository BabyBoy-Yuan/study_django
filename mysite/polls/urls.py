from django.urls import path

from . import views
app_name = "polls"
# urlpatterns = [
#     # es: /polls/
#     path('', views.index, name='index'),
#     # es: /polls/5
#     path('<int:question_id>/', views.detail, name='detail'),
#     # es: /polls/5/result
#     path('<int:question_id>/result/', views.results, name='results'),
#     # es: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

urlpatterns = [
    # es: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # es: /polls/5
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # es: /polls/5/result
    path('<int:pk>/result/', views.ResultsView.as_view(), name='results'),
    # es: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]