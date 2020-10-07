from django.shortcuts import render
from django.urls import reverse

from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm
from django.contrib import auth
from django.http import HttpResponseRedirect


def login(request):
    title = 'авторизация'
    login_form = ShopUserLoginForm(data=request.POST or None)

    next_url = request.GET.get('next', '')

    content = {
        'title': title,
        'login_form': login_form,
        'next': next_url,
    }

    # проверяю авторизован или нет, если авторизован, то на главную перекидываю, если нет то показываю форму
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('main'))
    else:
        if request.method == 'POST' and login_form.is_valid():
            username = request.POST['username']
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                if 'next' in request.POST.keys():
                    return HttpResponseRedirect(request.POST['next'])
                return HttpResponseRedirect(reverse('main'))

        return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


def register(request):
    title = 'регистрация'
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))

    else:
        register_form = ShopUserRegisterForm()
    content = {
        'title': title,
        'register_form': register_form
    }
    return render(request, 'authapp/register.html', content)


def edit(request):
    title = 'редактирование'
    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)

    content = {
        'title': title,
        'edit_form': edit_form
    }

    return render(request, 'authapp/edit.html', content)