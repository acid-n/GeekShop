from django.shortcuts import render, get_object_or_404

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
            'products': products_items
        }
        return render(request, 'mainapp/products_list.html', content)

    same_products = Product.objects.all()[3:5]
    content = {'title': title, 'links_menu': links_menu, 'same_products': same_products}
    return render(request, 'mainapp/products.html', content)


def contact(request):
    title = 'контакты'
    contacts_list = Contacts.objects.all()[:3]
    content = {
        'title': title,
        'contacts': contacts_list
    }
    return render(request, 'mainapp/contact.html', content)
