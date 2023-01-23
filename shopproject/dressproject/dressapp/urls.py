from . import views
from django.urls import path
app_name='dressapp'

urlpatterns = [
 path('', views.allPrctCat,name='allPrctCat'),
    path('<slug:c_slug>/',views.allPrctCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='prctCatdetail')
    ]