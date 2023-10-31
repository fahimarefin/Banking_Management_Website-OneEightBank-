from django.contrib import admin
from django.urls import path
from Home import views
from django.contrib.auth.views import LoginView
#from .views import account_details


urlpatterns = [
    #path('admin/', admin.site.urls),
    path("",views.index,name='index'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("contact",views.contact,name='contact'),
    path("devs",views.devs,name='devs'),
    path("portfolioFahim",views.portfolioFahim,name='portfolioFahim'),
    path("portfolioAni",views.portfolioAni,name='portfolioAni'),
    path("portfolioSumya",views.portfolioSumya,name='portfolioSumya'),
    path("personalBanking",views.personalBanking,name='personalBanking'),
    path("personalBankingForm",views.personalBankingForm,name='personalBankingForm'),
    path("prepaidcard",views.prepaidcard,name='prepaidcard'),
    path("debitcard",views.debitcard,name='debitcard'),
    path("signup",views.signup,name='signup'),
    path('log_in/', views.log_in, name='log_in'),
    path('index_after_signin', views.index_after_signin, name='index_after_signin'),
    path('profile',views.profile,name='profile'),
    path('changepass',views.changepass,name='changepass'),
    path('deposit',views.deposit,name='deposit'),
    path('withdraw',views.withdraw,name='withdraw'),
    path('check_balance',views.check_balance,name='check_balance'),
    path('money_transfer/', views.transfer, name='transfer'),
    path('balance/<int:account_id>/', views.balance, name='balance')



   
  
]


