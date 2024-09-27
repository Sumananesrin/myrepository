from django.urls import path
from .import views

urlpatterns=[
    path('',views.hello,name='home'),
    path('index',views.members,name='index'),
    path('context',views.geeks_view,name='context'),
    path('forrr',views.forr_loop,name='for'),
    path('haiii', views.forr_loop, name='for'),
    path('register', views.register, name='register'),
    path('login',views.logi,name='logi'),
    path('collections',views.collections,name='collections'),
    path('logout', views.logout, name='logout'),







]

















