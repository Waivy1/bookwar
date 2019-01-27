from django.db import models

class User(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone = models.IntegerField(null=True)


class Categories(models.Model):
    name = models.CharField(max_length=30)


class Item(models.Model):
    #id = ....
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    categories_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    picture = models.CharField(max_length=255, null=True, default=None)

class Basket(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)





