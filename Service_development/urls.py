from django.urls import path

from Service_development import views
from Service_development.apps import ServiceDevelopmentConfig
from Service_development.views import *

app_name = ServiceDevelopmentConfig.name

urlpatterns = [
    path('clients/', views.client_list, name='client_list'),
    path('clients/create/', views.create_client, name='create_client'),
    path('clients/view/<int:client_id>/', views.view_client, name='view_client'),
    path('mailing-lists/create/', views.create_mailing_list, name='create_mailing_list'),
    path('mailing-lists/view/<int:mailing_list_id>/', views.view_mailing_list, name='view_mailing_list'),
    path('mailing-lists/view/<int:mailing_list_id>/logs/', views.view_mailing_logs, name='view_mailing_logs'),
    path('mailing-lists/send/<int:mailing_list_id>/', views.send_message, name='send_message'),
]
