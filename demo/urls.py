"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import signin, vip, signup, passbook, report, productlist, products
from myapp.views import travel, signout, buy, qrcode, memberset, modify, ranklist ,daily

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/', signin, name=""),
    path('member/', vip, name=""),
    path('signup/', signup, name=""),
    path('passbook/', passbook, name=""),
    path('question/', report, name=""),
    path('productlist/', productlist, name=""),
    path('daily/', daily, name=""),
    path('travel/', travel, name=""),
    path('products/', products, name=""),
    path('signout/', signout, name=""),
    path('buy/', buy, name=""),
    path('qrcode/', qrcode, name=""),
    path('memberset/', memberset, name=""),
    path('modify/', modify, name=""),
    path('ranklist/', ranklist, name=""),
]
