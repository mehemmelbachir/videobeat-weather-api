from django.urls import path
from .views import OutputDataView, InputDataView
from django.views.decorators.cache import cache_page
from django.conf import settings

CACHE_TTL = settings.CACHE_TTL


app_name = 'api'
urlpatterns = [
    path('weather-list/', cache_page(CACHE_TTL)(OutputDataView.as_view()), name = 'weather-list'),
    path('input-list/', cache_page(CACHE_TTL)(InputDataView.as_view()), name = 'input-list'),
]