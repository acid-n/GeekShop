from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory, Contacts

import random


def get_hot_product():
    products_list = Product.objects.all().select_related('category')
    return random.sample(list(products_list), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category_id=hot_product.category, is_active=True).\
                        exclude(pk=hot_product.pk).select_related('category')[:3]
    return same_products


def main(request):
    title = 'главная'

    # print(request.resolver_match)

    products_list = Product.objects.all().select_related('category')[:3]
    content = {'title': title, 'products': products_list}
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None, page=1):
    title = 'продукты'
    links_menu = ProductCategory.objects.all()

    # print(request.resolver_match)

    if pk is not None:
        if pk == 0:
            category = {
                'pk': 0,
                'name': 'все',
            }
            products = Product.objects.all().order_by('price').select_related('category')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        paginator = Paginator(products, 4)  # 4 - это количество товаров на странице
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products_paginator,
        }
        return render(request, 'mainapp/products_list.html', content)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
        'hot_product': hot_product,
    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    title = 'контакты'
    contacts_list = Contacts.objects.all()[:3]
    content = {
        'title': title,
        'contacts': contacts_list,
    }
    return render(request, 'mainapp/contact.html', content)


def product(request, pk):
    product_item = get_object_or_404(Product, pk=pk)
    title = product_item.name
    content = {
        'title': title,
        'product': product_item,
        'links_menu': ProductCategory.objects.all().select_related('category'),
        'same_products': get_same_products(product_item)
    }

    return render(request, 'mainapp/product.html', content)
