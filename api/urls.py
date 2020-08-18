from django.contrib import admin
from django.urls import path,include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products',  views.product_list,name='product_list'),
]

app_name = 'api'