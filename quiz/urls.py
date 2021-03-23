from django.urls import path
from .views import (QuizListView, quiz_view, quiz_result)


urlpatterns = [
    path('',  QuizListView.as_view(), name='quiz_list'),
    path('<pk>/', quiz_view, name='quiz_view'),
    path('<pk>/result', quiz_result, name='quiz_result'),
]
