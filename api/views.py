from django.shortcuts import render
import requests
from .models import Product
from django.db.models import Q
from django.core.paginator import EmptyPage,Paginator,PageNotAnInteger
from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Count

url = "https://search.paytm.com/v2/search?userQuery=Micromax+TV&page_count=5&items_per_page=50"
# Create your views here.

def get_paytm_data():
    get_paytm_data = requests.get(url).json()
    print("++++++++++++++++++++++")
    product_data = {}
    product_list = []
    for product_item in get_paytm_data['grid_layout']:
        product_data['name'] = product_item['name']
        product_data['url'] = product_item['url']
        product_data['image'] = product_item['image_url']
        product_data['price'] = product_item['actual_price']
        product_list.append(product_data.copy())
    return product_list

def product_list(request):
    products = get_paytm_data()
    duplicate_obj = Product.objects.filter(name=products)
    for item in products:
        if not Product.objects.filter(name=item['name']).exists():
            product_obj = Product.objects.create(**item)
            product_obj.save()
    prd_list=Product.objects.all()
    query=request.GET.get("q")
    if query:
        prd_list=prd_list.filter(Q(name__icontains=query) | Q(price__icontains=query)).distinct()
    paginator=Paginator(prd_list,50)
    page_number=request.GET.get('page')
    try:
        prd_list=paginator.page(page_number)
    except PageNotAnInteger:
        prd_list=paginator.page(1)
    except EmptyPage:
        prd_list=paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'products': products,'prd_list':prd_list})