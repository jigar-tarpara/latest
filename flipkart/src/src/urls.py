"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from adminpanel.views import adminsite
from home.views import emptycart,cart_refresh,orderconfirm,wish,qtykart,order_display,checkout,total,payment,delete_product,refresh,count,cartpage,updateqty,cartadd,home,subcat,produc,single,register,login,logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^adminsite',adminsite),
    url(r'^$',home),
    url(r'^index.html$',home),
    url(r'^subcat/',subcat),
    url(r'^product',produc),
    url(r'^single',single),
    url(r'^register',register),
    url(r'^login',login),
    url(r'^logout',logout),
    url(r'^cartpage',cartpage),
    url(r'^cart',cartadd),
    url(r'^updateqty',updateqty),
    url(r'^count',count),
    url(r'^delete_product',delete_product),
    url(r'^refresh',refresh),
    url(r'^checkout',checkout),
    url(r'^payment',payment),
    url(r'^total',total),
    url(r'^orde_confirm/$',orderconfirm),
    url(r'^order',order_display),
    url(r'^wish',wish),
    url(r'^qtykart',qtykart),
    url(r'^emptycart',emptycart),
    url(r'^cbart_refresh',cart_refresh),

]