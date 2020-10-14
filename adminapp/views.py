from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


# Users

@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    pass


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    title = 'пользователи'
    users_list = ShopUser.objects.all()
    content = {
        'title': title,
        'objects': users_list,
    }
    return render(request, 'adminapp/users.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    pass


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    pass


# Categories

@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    pass


@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    title = 'категории'
    categories_list = ProductCategory.objects.all()
    content = {
        'title': title,
        'objects': categories_list,
    }
    return render(request, 'adminapp/categories.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_update(request, pk):
    pass


@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, pk):
    pass


# Products

@user_passes_test(lambda u: u.is_superuser)
def product_create(request, pk):
    pass


@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    title = 'продукты'
    category_item = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category=category_item)
    content = {
        'title': title,
        'objects': products_list,
        'category': category_item,
    }
    return render(request, 'adminapp/products.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product(request, pk):
    pass


@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    pass


@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, pk):
    pass
