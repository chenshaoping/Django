from django.urls import path
from . import views
app_name = 'restfull'

urlpatterns = [
    path('getTrees',views.getTrees),
    path('getTreesPost',views.getTreesPost),
]