"""bookwar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from core import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('basket', views.Basket.as_view(), name='basket'),
    path('delivery', views.Delivery.as_view(), name='delivery'),
    path('discounts', views.Discounts.as_view(), name='discounts'),
    path('about_me', views.AboutMe.as_view(), name='about_me'),
    path('payment', views.Payment.as_view(), name='payment'),
    path('bonuses', views.Bonuses.as_view(), name='bonuses'),
    path('sign_up', views.SignUp.as_view(), name='sign_up'),
    path('ass', views.LogIn.as_view(), name='login'),

    path('add_basket/<int:item_id>', views.AddBasket.as_view()),
    path('remove_from_basket/<int:item_id>', views.RemoveFromBasket.as_view()),
    path('confirm_order', views.ConfirmOrder.as_view()),
    path('category/<int:category_id>', views.Category.as_view()),



    path('', views.IndexPageView.as_view()),
]
