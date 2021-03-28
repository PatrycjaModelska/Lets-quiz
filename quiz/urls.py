from django.urls import path
from .views import (QuizListView, quiz_view, quiz_result, quiz_result_details)


urlpatterns = [
    path('',  QuizListView.as_view(), name='quiz_list'),
    path('<pk>/', quiz_view, name='quiz_view'),
    path('<pk>/<str:user>/result', quiz_result, name='quiz_result'),
    path('<pk>/<str:user>/result/details', quiz_result_details, name='quiz_result_details'),
]