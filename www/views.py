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
        # if request.method == 'GET':
        data = {
            'ok': 'working!'
        }
        return JsonResponse(data)

    def register(self, request):
        pass