from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from choices import views

urlpatterns = [
    path('choices/',views.ChoiceList.as_view()),
    path('choices/<int:pk>/',views.ChoiceDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)