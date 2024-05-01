from django.urls import path
from . import views

urlpatterns = [
    path('save-data/', views.save_survey_response, name='save-data'),
]
