from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View


class HomePageViews(View):
    def get(self, request):

        return render(request, 'www/home.html', locals())

    def post(self, request):
        pass


class AjaxQuery:

    @staticmethod
    def login(request):
        if request.method == 'GET':
            return redirect('/')

        if request.method == 'POST':
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)


            if username is not None and password is not None:
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        messages.success(request, 'Вы успешно авторизовались!')
                        return redirect('/')
                    else:
                        messages.error(request, 'Ваш аккаунт заблокирован')
                        return redirect('/')
                else:
                    messages.error(request, 'Неверный логин или пароль')
                    return redirect('/')
            else:
                messages.error(request, 'Пустой логин или пароль')
                return redirect('/')
        else:
            messages.error(request, 'Неверный запрос')
            return redirect('/')

    @staticmethod
    def logout(request):
        logout(request)
        messages.success(request, 'Вы успешло разлогинились!')
        return redirect('/')

    @staticmethod
    def register(request):
        if request.method == "GET":
            return redirect('/')

        if request.method == "POST":
            username = request.POST.get('username', None)
            email = request.POST.get('email', None)
            password1 = request.POST.get('password1', None)
            password2 = request.POST.get('password2', None)

            if (username and email and password1 and password2) is not None:
                try:
                    search_username = User.objects.get(username=username)
                except User.DoesNotExist:
                    search_username = None

                if search_username is None:
                    User.objects.create(
                        username=username,
                        email=email,
                        password=make_password(password2)
                    )
                    user = authenticate(username=username, password=password2)
                    login(request, user)

                    messages.success(request, 'Вы успешно зарегестрировались!')
                    messages.success(request, 'Вы успешно авторизованы!')
                    return redirect('/')

                if search_username is not None:
                    messages.error(request, 'Пользователь с таким именем уже зарегестрирован')
                    return redirect('/')
