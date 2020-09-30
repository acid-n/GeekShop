from django.shortcuts import render
from django.urls import reverse

from authapp.forms import ShopUserLoginForm
from django.contrib import auth
from django.http import HttpResponseRedirect


def login(request):
    title = 'вход'
    login_form = ShopUserLoginForm(data=request.POST)
    content = {
        'title': title,
        'login_form': login_form
    }

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('main'))
    else:
        if request.method == 'POST' and login_form.is_valid():
            username = request.POST['username']
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main'))

        return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))
