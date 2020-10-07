from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory, Contacts

import random


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    return []


def get_hot_product():
    products_list = Product.objects.all()
    return random.sample(list(products_list), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category_id=hot_product.category_id).exclude(pk=hot_product.pk)[:3]
    return same_products


def main(request):
    title = 'главная'

    # print(request.resolver_match)

    products_list = Product.objects.all()[:3]
    content = {'title': title, 'products': products_list, 'basket': get_basket(request.user)}
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    title = 'продукты'
    links_menu = ProductCategory.objects.all()

    # print(request.resolver_match)

    if pk is not None:
        if pk == 0:
            products_items = Product.objects.all()
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products_items = Product.objects.filter(category=category).order_by('-price')

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products_items,
            'basket': get_basket(request.user),
        }
        return render(request, 'mainapp/products_list.html', content)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
        'hot_product': hot_product,
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    title = 'контакты'
    contacts_list = Contacts.objects.all()[:3]
    content = {
        'title': title,
        'contacts': contacts_list,
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/contact.html', content)


def product(request, pk):
    product_item = get_object_or_404(Product, pk=pk)
    title = product_item.name
    content = {
        'title': title,
        'product': product_item,
        'basket': get_basket(request.user),
        'links_menu': ProductCategory.objects.all(),
        'same_products': get_same_products(product_item)
    }

    return render(request, 'mainapp/product.html', content)