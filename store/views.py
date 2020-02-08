from django.urls import reverse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .forms import DeliveryMemoryForm, DescentMemoryForm
from .models import Product, Category, Supply, Descent, Delivery_memory, Descent_memory
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class ListCategory(ListView):
    model = Category
    template_name = 'store/category.html'
    extra_context = {
        'title': "Lista Kategori",
    }
    context_object_name = 'category_list'

class CategoryDetails(DetailView):
    model = Category
    template_name = 'store/category_details.html'
    context_object_name = 'category'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = self.object.name
        return context

class CreateCategory(LoginRequiredMixin, CreateView):
  model = Category
  fields = ['name']
  template_name = 'store/create_category.html'
  extra_context = {
    'title': "Dodaj nową kategorię:"
  }



class ListProducts(ListView):
    model = Product
    template_name = 'store/products.html'
    extra_context = {
        'title': "Lista Produktów",
    }
    context_object_name = 'products_list'


class ProductsDetails(DetailView):
    model = Product
    template_name = 'store/products_details.html'
    context_object_name = 'product'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = self.object.name
        return context

class CreateProduct(LoginRequiredMixin, CreateView):
  model = Product
  fields = ['name', 'price', 'kind', 'quantity', 'category']
  template_name = 'store/create_product.html'
  extra_context = {
    'title': "Dodaj nowy produkt:"
  }

class ListDelivery(ListView):
    model = Supply
    template_name = 'store/delivery.html'
    extra_context = {
        'title': "Lista dostaw",
    }
    context_object_name = 'delivery_list'

class SupplyDetails(DetailView):
    model = Supply
    template_name = 'store/supply.html'
    context_object_name = 'supply'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = self.object.supply_date
        return context

class SupplyCreate(CreateView):
    model = Supply
    fields = ['supply_date']
    template_name = 'store/supply_add.html'
    extra_context = {
        'title': "Dodaj dostawę"
    }
    def get_success_url(self):
        return reverse('create-delmem', args=[self.object.pk])
@login_required

def delivery_memory_create(request, supply_id):
    # 1 pobrac supply
    supply = get_object_or_404(Supply, pk=supply_id)

    # formularz
    if request.method == "POST":
        form = DeliveryMemoryForm(request.POST)
        
        if form.is_valid():
            obj = form.save()
            obj.product.quantity += obj.quantity
            obj.product.save()
            return redirect(supply.get_absolute_url())
    
    else:
        form = DeliveryMemoryForm(initial={'supply': supply.pk})
    
    context = {
        'title': 'Dodawanie szczegóły dostawy',
        'form': form,
    }

    return render(request, 'store/create_delivery.html', context)

class ListDescent(ListView):
    model = Descent
    template_name = 'store/descent_list.html'
    extra_context = {
        'title': "Lista zejść towaru",
    }
    context_object_name = 'descent_list'

class DescentDetails(DetailView):
    model = Descent
    template_name = 'store/descent.html'
    context_object_name = 'descent'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = self.object.descent_date
        return context


class DescentCreate(CreateView):
    model = Descent
    fields = ['descent_date']
    template_name = 'store/descent_add.html'
    extra_context = {
        'title': "Dodaj zejście"
    }
    def get_success_url(self):
        return reverse('create-desmem', args=[self.object.pk])

@login_required

def descent_memory_create(request, descent_id):
    # 1 pobrac supply
    descent = get_object_or_404(Descent, pk=descent_id)

    # formularz
    if request.method == "POST":
        form = DescentMemoryForm(request.POST)
        
        if form.is_valid():
            obj = form.save()
            obj.product.quantity -= obj.quantity
            obj.product.save()
            return redirect(descent.get_absolute_url())
    
    else:
        form = DescentMemoryForm(initial={'descent': descent.pk})
    
    context = {
        'title': 'Dodawanie szczegóły zejścia',
        'form': form,
    }

    return render(request, 'store/create_descent.html', context)

def search(request):
    term = ''


    if request.method == 'GET' and 'term' in request.GET:
        # term = form.cleaned_data['term']
        ser = Product.objects.filter(name__icontains=request.GET['term'])
        context = {
            'title': 'Wynik wyszukiwania : ',
            'product_list': ser , 
        }

    return render(request, 'store/search_view.html', context)
