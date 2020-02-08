from django.urls import reverse
from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="NAZWA",
        help_text="Pełna nazwa produktu"
         )
    quantity = models.IntegerField(
        verbose_name="ILOŚĆ",
    )
    price = models.FloatField(
        verbose_name="CENA",

    )
    kind = models.CharField(
        verbose_name="TYP",
        max_length=200,
        help_text="Typ produktu"
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        verbose_name="KATEGORIA",
    )

    class Meta:
         ordering = ['name','quantity','price','kind']
    
    def get_absolute_url(self):
      return reverse('products-details', args=[self.pk])

    def __str__(self):
        return f"Produkt {self.name} z rodzaju {self.kind} w cenie {self.price} dostępny w ilości {self.quantity}"

class Category(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name="Nazwa",
        help_text="Nazwa kategori"
    )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']

    def get_absolute_url(self):
      return reverse('list-category')
    
    def __str__(self):
        return self.name

class Supply(models.Model):
    supply_date=models.DateTimeField(
        default=timezone.now,
        verbose_name="DATA DOSTAWY",
        )
    products = models.ManyToManyField(
        Product,
        through='Delivery_memory',
    )
    

    class Meta:
         ordering = ['supply_date']

    def get_absolute_url(self):
      return reverse('supply-details', args=[self.pk])

    def __str__(self):
        return f"Dostawa z dnia : {self.supply_date}"




class Delivery_memory(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    supply =  models.ForeignKey(Supply, on_delete = models.CASCADE)
    quantity = models.IntegerField()

class Descent(models.Model):
    descent_date = models.DateTimeField(
        default=timezone.now,
        verbose_name="DATA ZEJŚCIA",
        )
    products = models.ManyToManyField(
        Product,
        through='Descent_memory',
    )
    

    class Meta:
         ordering = ['descent_date']
    
    def get_absolute_url(self):
      return reverse('descent-details', args=[self.pk])

    def __str__(self):
        return f"Produkt  wydany : {self.descent_date}"

class Descent_memory(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    descent =  models.ForeignKey(Descent, on_delete = models.CASCADE)
    quantity = models.IntegerField()