from django.urls import path

from . import views

# MOST important Template tagging key word
app_name = 'autionapp'

urlpatterns = [
    # path('', views.index, name='index'),
    # '' is the home page ofr autionapp
    # path('',views.auctionlist, name ='auctionlist'),
    path('BuyerReg/',views.FormBuyerReg, name='FormBuyerReg'),
    path('bid/',views.bid_submit, name='bid'),
    path('auctionlist/',views.auctionlist, name='auctionlist'),
    path('register/',views.register, name='register'),
    path('user_login/',views.user_login,name='user_login'),

]
