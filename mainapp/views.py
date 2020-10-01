from django.shortcuts import render

from mainapp.models import Product, ProductCategory, Contacts

links_menu = [
    {'href': 'products_all', 'name': 'все'},
    {'href': 'products_home', 'name': 'дом'},
    {'href': 'products_office', 'name': 'офис'},
    {'href': 'products_modern', 'name': 'модерн'},
    {'href': 'products_classic', 'name': 'классика'},
]


def main(request):
    title = 'главная'
    products_list = Product.objects.all()[:3]
    content = {'title': title, 'products': products_list}
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    content = {
        'title': title,
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    title = 'контакты'
    contacts_list = Contacts.objects.all()[:3]
    content = {
        'title': title,
        'contacts': contacts_list
    }
    return render(request, 'mainapp/contact.html', content)