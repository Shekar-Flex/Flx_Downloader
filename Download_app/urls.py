from django.urls import path
from django.views import View
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('youdou',views.youdou,name="youdou"),
    path('youfun',views.youfun,name="youfun"),
    path('instadou',views.instadou,name="instadou"),
    path('insvdofun',views.insvdofun,name="insvdofun"),
    path('inspicfun',views.inspicfun,name="inspicfun")
]