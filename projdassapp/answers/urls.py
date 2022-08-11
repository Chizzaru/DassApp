from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from answers import views


urlpatterns = [
    path('answers/',views.AnswerList.as_view()),
    path('answers/<int:pk>/',views.AnswerDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
