from django.urls import path,include
from . import views
from django.conf import settings
from rest_framework import routers
from .views import *



app_name = 'tudoapi'

router = routers.DefaultRouter()
router.register('User', views.UserViewset),
router.register('Commodity',views.CommodityViewset),
urlpatterns =[

]
urlpatterns += router.urls 