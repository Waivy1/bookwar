from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
import random
import datetime

from core import models


class IndexPageView(View):
    def get(self, request, *args, **kwargs):
        date = datetime.datetime.now()

        books = models.Item.objects.all()
        categories = models.Categories.objects.all()

        return render(request, 'index.html', {
            'hour': date.hour,
            'minute': date.minute,
            'books': books,
            'categories': categories
        })




class Basket(View):
    def get(self, request):

        basket = models.Basket.objects.filter(user_id=request.session.get('user_id')) #get some -> [...]
        # basket == [{item_id=1, user_id=1}, {item_id=2, user_id=1}, {item_id=11, user_id=1}, ...]
        categories = models.Categories.objects.all()  #get all -> [....]

        return render(request, 'basket.html', {
            'user_basket': basket,
            'categories': categories

        })

class AddBasket(View):
    def get(self, request, item_id):
        item = models.Item.objects.get(id=item_id)  #get only one -> obj
        user = models.User.objects.get(id=request.session.get('user_id'))

        new_item_in_basket = models.Basket(user_id=user, item_id=item) #create
        new_item_in_basket.save()

        return redirect('/')   #перенаправленя на головну

class RemoveFromBasket(View):
    def get(self, request, item_id):
        item = models.Item.objects.get(id=item_id)
        user = models.User.objects.get(id=request.session.get('user_id'))

        remove_item_from_basket = models.Basket.objects.filter(user_id=user, item_id=item).first()
        remove_item_from_basket.delete()

        return redirect('/basket')

class ConfirmOrder(View):
    def get(self, request):
        basket_items = models.Basket.objects.filter(user_id=request.session.get('user_id'))

        for i in basket_items: #[obj1, obj2]
            print(f'{i.item_id.name} , id: {i.item_id.id}')


        basket_items.delete()


        return redirect('/basket')

class Delivery(View):
    def get(self, request):
        return HttpResponse('''
        delivery works 8.00 - 23.00
        monday - friday
        ''')

class Discounts (View):
    def get(self, request):
        return HttpResponse('there are some books with discounts')

class AboutMe(View): #camel case
    def get(self, request):
        categories = models.Categories.objects.all()
        return render(request, 'about_me.html', {
            'categories': categories
        }) # sneaky case


class Payment(View):
    def get (self, request):
        return HttpResponse('способи оплати')

class Item(View):
    def get(self, request, name):

        return HttpResponse('hi {}'.format(name))

class Bonuses(View):
    def get (self, request):
        return HttpResponse('bonuses')

class SignUp(View):
    def get (self, request):
        return render(request, 'not_exithtml')

    def post(self, request):
        print(request.POST) # {'email': 'kek', 'password': 567, 'csrf': 'aaaaaaaa'}

        login = request.POST['email']
        password = request.POST['password']

        new_user = models.User(login=login, password=password)
        new_user.save()

        return redirect('/')

class LogIn(View):
    def get(self, request):

        if request.session.get('user_id'): # get returns value or None if not exists
            return redirect('/')

        return render(request, 'not_exithtml')

    def post(self, request):
        input_login = request.POST['email'] #post це властивість. request is an object. it has post. post is a dict
        input_password = request.POST['password']

        user = models.User.objects.get(login=input_login, password=input_password)

        request.session['user_id'] = user.id  # writes user.id to user_id key

        return redirect('/')

class Category(View):
    def get(self, request, category_id):

        books = models.Item.objects.filter(categories_id=category_id)
        categories = models.Categories.objects.all()

        return render(request, 'index.html', {
            'books': books,
            'categories': categories
        })













