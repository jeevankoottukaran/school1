from . import views
from django.urls import path

urlpatterns = [

    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('details',views.details,name='details'),
    path('button',views.button,name='button'),
    path('details1', views.details1, name='details1'),

]