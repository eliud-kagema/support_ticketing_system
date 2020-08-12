from django.urls import path
from . import views

app_name = 'ticketing'
urlpatterns = [
    path('', views.index, name='index'),
    path('clients/index', views.clients, name='clients_index'),
    path('support/index', views.support, name='support_index'),
    path('admin/index', views.administrator, name='admin_index'),
]
