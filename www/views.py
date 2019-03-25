from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render
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

            if username is not None and password is not None:
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return JsonResponse({'ok': 'Успешная авторизация'})
                    else:
                        return JsonResponse({'error': 'Ваш аккаунт заблокирован'})
                else:
                    return JsonResponse({'error': 'Неверный логин или пароль'})
            else:
                return JsonResponse({'error': 'Пустой логин или пароль'})
        else:
            return JsonResponse({'error': 'Неверный запрос'})

    def register(self, request):
        pass