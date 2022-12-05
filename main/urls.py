
from . import views
from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views


app_name = "main"


urlpatterns = [
    path('', views.index, name="homepage"),
    path('add_company/', views.add_company, name="add_company"),
    path('buy_stocks/', views.test_buy_stocks, name="buy_stocks"),
    
    path('get_portfolio/', views.get_portfolio, name="get_portfolio"),
] 
