from django.urls import path
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='category/'), name='go-to-django'),
    path('category/', views.ListCategory.as_view(), name="list-category"),
    path('category/add/', views.CreateCategory.as_view(), name="create-category"),
    path('category/<int:pk>/', views.CategoryDetails.as_view(), name="category-details"),
    path('product/', views.ListProducts.as_view(), name="list-products"),
    path('product/<int:pk>/', views.ProductsDetails.as_view(), name="products-details"),
    path('product/add/', views.CreateProduct.as_view(), name="create-product"),
    path('supply/', views.ListDelivery.as_view(), name="list-delivery"),
    path('supply/<int:pk>/', views.SupplyDetails.as_view(), name="supply-details"),
    path('supply/add/', views.SupplyCreate.as_view(), name="create-supply"),
    path('supply/<int:supply_id>/add/', views.delivery_memory_create, name="create-delmem"),
    path('descent/', views.ListDescent.as_view(), name="list-descent"),
    path('descent/<int:pk>/', views.DescentDetails.as_view(), name="descent-details"),
    path('descent/add/', views.DescentCreate.as_view(), name="create-descent"),
    path('descent/<int:descent_id>/add/', views.descent_memory_create, name="create-desmem"),
    path('search/', views.search, name="search"),
]
