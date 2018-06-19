from django.urls import path, include
from . import views

app_name = 'weatherapi'
urlpatterns = [
    path('api/', include('weatherapi.api.urls', namespace='app:api')),
    path('', views.home),
    path('clear-data/', views.clear_data, name='clear-data'),
]