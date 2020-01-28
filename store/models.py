from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(
        max_length=200,
        help_text=("Pełna nazwa produktu")
         )
    quantity = models.IntegerField()
    price = models.IntegerField()
    kind = modes.CharField(
        max_length=200,
        help_text=("Typ produktu")
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
    )

    class Meta:
         ordering = ['name','quantity','price','kind']

    def __str__(self):
        return f"Produkt {self.name} z rodzaju {self.kind} w cenie {self.price} dostępny w ilości {self.quantity}"

class Category(models.Model):
    name = models.CharField(
        max_length=200
        unique=true,
        verbose_name=("Nazwa"),
        help_text=("Nazwa kategori")
    )

    class Meta:
        verbose_name = ("Category")
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Supply(models.Model):
    supply_date=models.DateTimeField(default=timezone.now)
    product = models.ManyToManyField(
        Product,
        through='Delivery_memory',
    )
    quantity = models.IntegerField()

    class Meta:
         ordering = ['supply_date','product','quantity']

    def __str__(self):
        return f"Produkt {self.product} dostarczony : {self.supply_date} w ilości {self.quantity}"



class Delivery_memory(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    supply =  models.ForeignKey(Supply, on_delete = models.CASCADE)

class Descent(models.model):
    descent_date = models.DateTimeField(default=timezone.now)
    product = models.ManyToManyField(
        Product,
        through='Descent_memory',
    )
    quantity = models.IntegerField()

    class Meta:
         ordering = ['descent_date','product','quantity']

    def __str__(self):
        return f"Produkt {self.product} wydany : {self.supply_date} w ilości {self.quantity}"

class Descent_memory(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    descent =  models.ForeignKey(Descent, on_delete = models.CASCADE)