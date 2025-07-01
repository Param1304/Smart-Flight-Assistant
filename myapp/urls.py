from django.urls import path
from .views import home, delay_predictor, co2_footprint, delay_analysis, about, statistics, compare_airlines
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', home, name='home'),
    path('delay_predictor/', delay_predictor, name='delay_predictor'),
    # path('live_tracking/', live_tracking, name='live_tracking'),
    path('compare_airlines/', compare_airlines, name='compare_airlines'),
    path('co2_footprint/', co2_footprint, name='co2_footprint'),    
    path('delay_analysis/', delay_analysis, name='delay_analysis'),
    path('about/', about, name='about'),
    path('statistics/', statistics, name="statistics"),
    
]