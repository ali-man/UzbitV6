from django.contrib.auth import authenticate, login, logout
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
            username = request.GET.get('username', None)
            password = request.GET.get('password', None)
            # print(username)
            # print(password)

            if username is not None and password is not None:
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        print(1)
                        # return JsonResponse({'ok': 'Успешная авторизация'})
                        return redirect('/')
                    else:
                        return JsonResponse({'error': 'Ваш аккаунт заблокирован'})
                else:
                    return JsonResponse({'error': 'Неверный логин или пароль'})
            else:
                return JsonResponse({'error': 'Пустой логин или пароль'})
        else:
            return JsonResponse({'error': 'Неверный запрос'})

    @staticmethod
    def logout(request):
        logout(request)
        print(request)
        # return JsonResponse({'ok': 'Вы разлогинились'})
        return redirect('/')

    @staticmethod
    def register(request):
        pass